Add-Type -AssemblyName System.Speech
$syn = New-Object System.Speech.Synthesis.SpeechSynthesizer
$syn.SelectVoice("Microsoft David Desktop")
$syn.Rate = 1
$syn.Volume = 100
$out = "C:\Users\jibra\Desktop\1\KAI\audio"
$lines = @(
 "Everyone buying a GPU for local AI is measuring the wrong number.",
 "Twenty four gigabytes of VRAM doesn't run a twenty four gigabyte model. The weights are only half. The other half is the KV cache, and it grows with every token of context.",
 "A twenty four gig model at thirty two K context needs six more gigabytes. So the card that fits it, doesn't.",
 "It spills into system RAM at a tenth of the speed. Forty tokens a second becomes four.",
 "Sixteen gigs, comfortable at eight K. Twenty four, fine at thirty two K. Forty eight, real work.",
 "Above seventy B, you're not buying VRAM. You're buying bandwidth.",
 "So stop asking how many gigabytes. Ask how many tokens per second you need, and buy the smallest card that still holds your context."
)
for ($i = 0; $i -lt $lines.Count; $i++) {
  $n = $i + 1
  $path = Join-Path $out ("seg{0}.wav" -f $n)
  $syn.SetOutputToWaveFile($path)
  $syn.Speak($lines[$i])
  $syn.SetOutputToNull()
  "seg$n written"
}
$syn.Dispose()
