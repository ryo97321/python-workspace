import json
import gzip
import re

head_pattern = r'\[\[Category:'
tail_pattern = r'\|?\*?\]\]'
with gzip.open('jawiki-country.json.gz', 'rt', encoding='utf-8_sig') as f:
    obj = json.loads(f.readline())
    while(obj):
        try:
            obj = json.loads(f.readline())
            for line in obj['text'].split('\n'):
                if 'Category' in line:
                    line = re.sub(head_pattern, '', line)
                    line = re.sub(tail_pattern, '', line)
                    print(line)
        except:
            obj = f.readline()