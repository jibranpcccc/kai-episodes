import io
import os

K = r'C:\Users\jibra\Desktop\1\KAI'
lines = []
for tag in ('segA', 'segB'):
    p = os.path.join(K, 'proof', 'BYTE-EP09-export-%s.mp4' % tag).replace('\\', '/')
    lines.append("file '%s'" % p)
out = os.path.join(K, 'proof', 'concat_list.txt')
io.open(out, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines) + '\n')
print(io.open(out, encoding='utf-8').read())
