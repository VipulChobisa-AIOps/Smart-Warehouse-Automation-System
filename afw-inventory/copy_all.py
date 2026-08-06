import os
import shutil

source_base = r"E:\vipul\files\afw"
target_base = r"C:\Users\vipul\OneDrive\Documents\vipul-chobisa-portfolio\repositories\Smart-Warehouse-Automation-System\afw-inventory"

count = 0
errors = 0

for root, dirs, files in os.walk(source_base):
    rel = os.path.relpath(root, source_base)
    if rel == ".":
        target_dir = target_base
    else:
        target_dir = os.path.join(target_base, rel)
    
    unc_target_dir = "\\\\?\\" + os.path.abspath(target_dir)
    
    if not os.path.exists(unc_target_dir):
        try:
            os.makedirs(unc_target_dir, exist_ok=True)
        except Exception as e:
            print(f"Mkdir error {unc_target_dir}: {e}")
            
    for f in files:
        if f.startswith("~$"):
            continue
        s_path = os.path.join(root, f)
        t_path = os.path.join(target_dir, f)
        
        unc_s = "\\\\?\\" + os.path.abspath(s_path)
        unc_t = "\\\\?\\" + os.path.abspath(t_path)
        
        try:
            shutil.copy2(unc_s, unc_t)
            count += 1
        except Exception as e:
            try:
                shutil.copy2(s_path, t_path)
                count += 1
            except Exception as e2:
                print(f"Error copying {f}: {e2}")
                errors += 1

print(f"DONE! Successfully copied {count} files with {errors} errors.")

