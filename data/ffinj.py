import os
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
src=open(os.path.join(ROOT,"EPISODE-02.html"),encoding="utf-8").read()
inj="""<script>
document.getElementById('start').style.display='none';
['hud','tc','cue'].forEach(function(i){var e=document.getElementById(i); if(e)e.style.display='none';});
var S=document.querySelectorAll('.scene')[3];
S.classList.add('active');
S.querySelectorAll('[data-in]').forEach(function(e){e.classList.add('on');});
S.querySelectorAll('.grow').forEach(function(e){e.classList.add('on');});
</script>"""
open(os.path.join(ROOT,"_ffscene.html"),"w",encoding="utf-8").write(src.replace("</body>",inj+"\n</body>"))
print("wrote _ffscene.html")
