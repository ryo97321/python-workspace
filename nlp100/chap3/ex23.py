import json
import gzip
import re

with gzip.open('jawiki-country.json.gz', 'rt', encoding='utf-8_sig') as f:
    obj = json.loads(f.readline())
    while(obj):
        try:
            obj = json.loads(f.readline())

            pattern = '=='
            for line in obj['text'].split('\n'):
                if pattern in line:
                    pat_by_sec = ''.join([r'=' for i in range(int(line.count('=') / 2))])
                    sec = len(pat_by_sec) - 1
                    tab = ''.join(['\t' for i in range(sec - 1)])
                    print('{}{}. {}'.format(tab, sec, line.replace('=', '')))
        except:
            obj = f.readline()