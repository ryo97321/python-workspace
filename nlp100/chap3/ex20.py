import json
import gzip

with gzip.open('jawiki-country.json.gz', 'rt', encoding='utf-8_sig') as f:
    obj = json.loads(f.readline())
    while(obj):
        try:
            obj = json.loads(f.readline())
            if obj['title'] == "イギリス":
                break
        except:
            obj = f.readline()