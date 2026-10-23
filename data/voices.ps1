Add-Type -AssemblyName System.Speech
$syn = New-Object System.Speech.Synthesis.SpeechSynthesizer
"--- installed voices ---"
$syn.GetInstalledVoices() | ForEach-Object {
  $vi = $_.VoiceInfo
  "{0} | {1} | {2} | enabled={3}" -f $vi.Name, $vi.Gender, $vi.Culture, $_.Enabled
}
$syn.Dispose()
