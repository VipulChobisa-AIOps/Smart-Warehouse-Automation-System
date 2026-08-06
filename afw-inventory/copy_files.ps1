$sourceDir = "E:\vipul\files\afw"
$targetDir = "C:\Users\vipul\OneDrive\Documents\vipul-chobisa-portfolio\repositories\Smart-Warehouse-Automation-System\afw-inventory"

Write-Host "Copying items from $sourceDir to $targetDir..."

Get-ChildItem -Path $sourceDir | Where-Object { $_.Name -notlike '~$*' } | ForEach-Object {
    Write-Host "Copying $($_.Name)..."
    Copy-Item -Path $_.FullName -Destination $targetDir -Recurse -Force
}

Write-Host "Copy process finished."
