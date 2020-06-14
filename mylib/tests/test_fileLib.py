# coding:utf-8

import unittest

from classes.fileLib import FileLib

class file_to_lines_test(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    # ファイルの内容がアルファベットのみのとき
    def test_alphabet_only(self):
        lines_correct = ['abc', 'def', 'ghi']
        fileLib = FileLib()
        lines_result = fileLib.file_to_lines('tests/data/alphabet_only.txt')
        self.assertEqual(lines_correct, lines_result)

    # ファイルの内容が日本語のみのとき
    def test_japanese_only(self):
        lines_correct = ['おはよう', 'こんにちは', 'こんばんわ']
        fileLib = FileLib()
        lines_result = fileLib.file_to_lines('tests/data/japanese_only.txt')
        self.assertEqual(lines_correct, lines_result)