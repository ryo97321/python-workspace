import json
import gzip
import re

with gzip.open('jawiki-country.json.gz', 'rt', encoding='utf-8_sig') as f:
    obj = json.loads(f.readline())
    while(obj):
        try:
            obj = json.loads(f.readline())
            for line in obj['text'].split('\n'):
                if 'Category' in line:
                    print(line)
        except:
            obj = f.readline()