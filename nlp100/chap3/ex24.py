import json
import gzip
import re

with gzip.open('jawiki-country.json.gz', 'rt', encoding='utf-8_sig') as f:
    obj = json.loads(f.readline())
    while(obj):
        try:
            obj = json.loads(f.readline())
            for line in obj['text'].split('\n'):
                if 'ファイル' in line:
                    print(line.split(':')[1].split('|')[0])
        except:
            obj = f.readline()