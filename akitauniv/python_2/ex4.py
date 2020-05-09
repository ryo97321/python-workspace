with open('test.txt', 'rt') as fin:
    file = fin.read()

with open('test_copy.txt', 'wt') as fout:
    fout.write(file)