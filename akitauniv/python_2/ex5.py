'''COVID-19のCSVを読み込み, ユーザーの要求に応じて回答するプログラム'''

import csv
from collections import defaultdict

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


if __name__ == '__main__':
    make_dict()

    print('どちらを表示しますか？')
    option = int(input('0. ある日のある都道府県の感染者数 / 1. ある都道府県の合計感染者数：'))

    input_pref = input('都道府県名（ex. 秋田県）：')
    if option == 0:
        input_date = input('日時（ex. 1/20/2020）：')
        tup = (input_pref, input_date)
        print("\n{} : {} の感染者数は {}人 です".format(input_date, input_pref, PREF_DAY_INFECTED[tup]))
    elif option == 1:
        print('\n{} の合計感染者数は {}人 です'.format(input_pref, PREF_TOTAL_INFECTED[input_pref]))
