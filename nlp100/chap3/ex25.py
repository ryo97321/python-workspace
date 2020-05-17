import json
import gzip
import re

with gzip.open('jawiki-country.json.gz', 'rt', encoding='utf-8_sig') as f:
    obj = json.loads(f.readline())
    while(obj):
        try:
            obj = json.loads(f.readline())

            basic_info = {}
            pattern = r' = '
            for line in obj['text'].split('\n'):
                if pattern in line:
                    # print(line)
                    basic_info[line.split(' = ')[0].replace('|', '')] = line.split(' = ')[1]
            print(basic_info)
        except:
            obj = f.readline()
        