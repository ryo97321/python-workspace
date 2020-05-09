'''COVID-19のCSVを読み込み, ユーザーの要求に応じて回答するプログラム'''

import csv
from collections import defaultdict
import PySimpleGUI as sg

# ある日・都道府県の感染者数（ex. PREF_DAY_INFECTED[('岩手県', '1/20/2020')] = 0）
PREF_DAY_INFECTED = defaultdict(int)

# ある都道府県の合計感染者数（ex. PREF_TOTAL_INFECTED['岩手県'] = 0）
PREF_TOTAL_INFECTED = defaultdict(int)


def make_dict():
    '''CSVファイルを読み込み辞書を作成する'''
    global PREF_DAY_INFECTED
    global PREF_TOTAL_INFECTED

    with open('COVID-19.csv', 'rt', encoding='utf-8_sig') as file:
        cin = csv.reader(file)

        for i, row in enumerate(cin):
            if i == 0:
                continue

            pref_index = 9
            date_index = 7
            pref = row[pref_index]
            date = row[date_index]

            PREF_DAY_INFECTED[(pref, date)] += 1
            PREF_TOTAL_INFECTED[pref] += 1


def parse_date(date):
    '''dateを辞書用に変換する（2020/4/30 -> 4/30/2020）'''
    date_parts = date.split('/')
    year = date_parts[0]
    month = date_parts[1]
    day = date_parts[2]

    return month + '/' + day + '/' + year


if __name__ == '__main__':
    make_dict()

    sg.theme('Dark Blue 3')
    layout = [
        [sg.Text('日付', size=(15, 1), key='-DATE_TEXT-'), \
            sg.InputText('2020/4/30', key='-DATE_INPUTTEXT-')],
        [sg.Text('都道府県名', size=(15, 1), key='-PREF_TEXT-'), \
            sg.InputText('東京都', key='-PREF_INPUTTEXT-')],
        [sg.Submit(button_text='表示')]
    ]

    window = sg.Window('感染者数表示アプリ', layout)

    while True:
        event, values = window.read()
        if event is None:
            break

        if event == '表示':
            date_obj = window['-DATE_INPUTTEXT-']
            pref_obj = window['-PREF_INPUTTEXT-']

            date_obj_value = date_obj.get()
            pref_obj_value = pref_obj.get()

            if date_obj_value == '':
                show_message = pref_obj_value + 'の合計感染者数は ' \
                    + str(PREF_TOTAL_INFECTED[pref_obj_value]) + 'です。'
            else:
                key = (pref_obj_value, parse_date(date_obj_value))
                show_message = date_obj_value + ' : ' + pref_obj_value \
                    + ' の感染者数は ' + str(PREF_DAY_INFECTED[key]) + 'です。'

            sg.popup(show_message)

    window.close()
