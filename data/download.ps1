$ErrorActionPreference = "Continue"
$root = "C:\Users\jibra\Desktop\1\KAI"
$log  = Join-Path $root "data\download.log"
$ids  = Get-Content (Join-Path $root "data\ids.txt") | Where-Object { $_.Trim() -ne "" }
"START $(Get-Date -Format o)  count=$($ids.Count)" | Out-File -Append -Encoding utf8 $log
$i = 0
foreach ($id in $ids) {
    $i++
    $out = Join-Path $root "videos\$id.%(ext)s"
    "=== [$i/$($ids.Count)] $id  $(Get-Date -Format HH:mm:ss) ===" | Out-File -Append -Encoding utf8 $log
    $ytargs = @(
        "-f","bv*[height<=1080]+ba/b",
        "--merge-output-format","mp4",
        "--write-info-json","--write-thumbnail",
        "--no-warnings","--no-playlist",
        "--retries","5","--fragment-retries","10",
        "--sleep-requests","0.4",
        "-o",$out,
        "https://www.youtube.com/watch?v=$id"
    )
    & yt-dlp @ytargs *>&1 | Out-File -Append -Encoding utf8 $log
    "[exit $LASTEXITCODE] $id" | Out-File -Append -Encoding utf8 $log
}
"DONE $(Get-Date -Format o)" | Out-File -Append -Encoding utf8 $log

