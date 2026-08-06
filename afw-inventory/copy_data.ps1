$source = 'E:\vipul\files\afw'
$dest = 'c:\Users\vipul\OneDrive\Documents\vipul-chobisa-portfolio\repositories\Smart-Warehouse-Automation-System\afw-inventory'

Get-ChildItem -Path $source -Recurse | ForEach-Object {
    if ($_.Name -like '~$*') { return }
    $rel = $_.FullName.Substring($source.Length)
    $target = $dest + $rel
    
    $longSource = "\\?\" + $_.FullName
    $longTarget = "\\?\" + $target

    if ($_.PSIsContainer) {
        if (-not [System.IO.Directory]::Exists($longTarget)) {
            [System.IO.Directory]::CreateDirectory($longTarget) | Out-Null
        }
    } else {
        $parent = [System.IO.Path]::GetDirectoryName($longTarget)
        if (-not [System.IO.Directory]::Exists($parent)) {
            [System.IO.Directory]::CreateDirectory($parent) | Out-Null
        }
        try {
            [System.IO.File]::Copy($longSource, $longTarget, $true)
        } catch {
            Write-Host "Failed to copy $($_.FullName): $_"
        }
    }
}

Write-Host "Extended long path copy complete!"
