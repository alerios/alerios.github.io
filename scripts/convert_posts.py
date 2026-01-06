#!/usr/bin/env python3
from pathlib import Path
import sys
import re
root=Path('post')
out=Path('_posts')
out.mkdir(exist_ok=True)
files=list(root.glob('*.md.bak'))
count=0
for f in files:
    name=f.name[:-4]
    dest=out/(name)
    s=f.read_text()
    s=s.replace('images/','/img/')
    if s.startswith('---'):
        parts=s.split('---',2)
        if len(parts)>=3:
            fm=parts[1]
            rest=parts[2]
            if 'layout:' not in fm:
                fm = fm.strip()+"\nlayout: post\n"
            s='---\n'+fm+'\n---'+rest
    else:
        s='---\nlayout: post\n---\n'+s
    dest.write_text(s)
    print(f'Converted {f} -> {dest}')
    count+=1
print(f'Converted {count} files')
