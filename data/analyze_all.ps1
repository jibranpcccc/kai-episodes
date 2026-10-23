$ErrorActionPreference="Continue"
$root="C:\Users\jibra\Desktop\1\KAI"
$log=Join-Path $root "data\analyze.log"
"ANALYZE START $(Get-Date -Format o)" | Out-File -Encoding utf8 $log
foreach($d in (Get-ChildItem (Join-Path $root "frames") -Directory)){
    $vid=$d.Name
    $out=Join-Path $root "data\summary_$vid.json"
    if(Test-Path $out){ "[skip] $vid" | Out-File -Append -Encoding utf8 $log; continue }
    "[run] $vid" | Out-File -Append -Encoding utf8 $log
    & python (Join-Path $root "data\analyze_frames.py") $vid *>&1 | Out-File -Append -Encoding utf8 $log
}
"ANALYZE DONE" | Out-File -Append -Encoding utf8 $log
