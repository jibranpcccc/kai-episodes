$ErrorActionPreference = "Continue"
$root = "C:\Users\jibra\Desktop\1\KAI"
$log  = Join-Path $root "data\extract.log"
$dl   = Join-Path $root "data\download.log"
"EXTRACT START $(Get-Date -Format o)" | Out-File -Encoding utf8 $log

$deadline = (Get-Date).AddMinutes(40)
while ((Get-Date) -lt $deadline) {
    if (Select-String -Path $dl -Pattern "^DONE " -Quiet) { break }
    Start-Sleep -Seconds 8
}
$ids = Get-Content (Join-Path $root "data\ids.txt") | Where-Object { $_.Trim() -ne "" }
foreach ($id in $ids) {
    $mp4 = Join-Path $root "videos\$id.mp4"
    if (-not (Test-Path $mp4)) { "[skip] $id (no mp4)" | Out-File -Append -Encoding utf8 $log; continue }
    $dir = Join-Path $root "frames\$id"
    New-Item -ItemType Directory -Force -Path $dir | Out-Null
    $have = @(Get-ChildItem $dir -Filter *.jpg -ErrorAction SilentlyContinue).Count
    if ($have -gt 50) {
        "[ok] $id already $have frames" | Out-File -Append -Encoding utf8 $log
    } else {
        $t0 = Get-Date
        & ffmpeg -hide_banner -loglevel error -i $mp4 -vf "fps=2" -q:v 3 -start_number 0 ("{0}\%06d.jpg" -f $dir) *>&1 | Out-File -Append -Encoding utf8 $log
        $n = @(Get-ChildItem $dir -Filter *.jpg).Count
        "[frames] $id = $n  in $([int]((Get-Date)-$t0).TotalSeconds)s" | Out-File -Append -Encoding utf8 $log
    }
    $sc = Join-Path $root "data\scenes_$id.txt"
    if (-not (Test-Path $sc)) {
        & ffmpeg -hide_banner -loglevel info -i $mp4 -vf "select='gt(scene,0.22)',showinfo" -an -f null - 2> $sc
        "[scene] $id done" | Out-File -Append -Encoding utf8 $log
    }
}
"EXTRACT DONE $(Get-Date -Format o)" | Out-File -Append -Encoding utf8 $log
