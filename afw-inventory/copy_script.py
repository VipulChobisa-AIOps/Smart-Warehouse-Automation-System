import os
import shutil

src_root = r"E:\vipul\files\afw"
dst_root = r"C:\Users\vipul\OneDrive\Documents\vipul-chobisa-portfolio\repositories\afw-inventory"

copied = 0
skipped = 0
failed = 0

for root, dirs, files in os.walk(src_root):
    # Calculate relative path
    rel_path = os.path.relpath(root, src_root)
    if rel_path == ".":
        target_dir = dst_root
    else:
        target_dir = os.path.join(dst_root, rel_path)

    # Ensure target directory exists
    if not os.path.exists(target_dir):
        os.makedirs(target_dir, exist_ok=True)

    for f in files:
        if f.startswith("~$"):
            skipped += 1
            continue

        s_file = os.path.join(root, f)
        d_file = os.path.join(target_dir, f)

        try:
            shutil.copy2(s_file, d_file)
            copied += 1
        except Exception as e:
            # If standard copy fails due to path length > 260, try UNC prefix
            try:
                unc_s = "\\\\?\\" + os.path.abspath(s_file)
                unc_d = "\\\\?\\" + os.path.abspath(d_file)
                shutil.copy2(unc_s, unc_d)
                copied += 1
            except Exception as e2:
                print(f"FAILED: {s_file} -> {e2}")
                failed += 1

print(f"Summary: Copied={copied}, Skipped={skipped}, Failed={failed}")
