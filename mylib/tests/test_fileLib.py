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
        lines_correct = ['おはよう', 'こんにちは', 'こんばんは']
        fileLib = FileLib()
        lines_result = fileLib.file_to_lines('tests/data/japanese_only.txt')
        self.assertEqual(lines_correct, lines_result)

    # ファイルの中にアルファベットと日本語が混在しているとき
    def test_alphabet_and_japanese(self):
        lines_correct = ['abc', 'おはよう', 'def', 'こんにちは', 'ghi', 'こんばんは']
        fileLib = FileLib()
        lines_result = fileLib.file_to_lines('tests/data/alphabet_and_japanese.txt')
        self.assertEqual(lines_correct, lines_result)

    # ファイルの中に空行があるとき
    def test_include_empty_line(self):
        lines_correct = ['abc', '', 'def']
        fileLib = FileLib()
        lines_result = fileLib.file_to_lines('tests/data/include_empty_line.txt')
        self.assertEqual(lines_correct, lines_result)