class FileLib:
    def file_to_lines(self, filename):
        '''filenameをテキストモードで開き, 行ごとにリストに格納して返す関数'''

        # linesに行ごとに読み込む
        with open(filename, 'rt', encoding='utf-8') as fp:
            lines = fp.readlines()
        
        # 行末から改行文字 '\n' を取り除く
        for i, line in enumerate(lines):
            lines[i] = line.strip('\n')
        
        return lines.copy()