import PySimpleGUI as sg

sg.theme('Dark Blue 3')

layout = [
    [sg.Text('Python GUI')],
    [sg.Text('名前', size=(15, 1)), sg.InputText('oo〇xxx')],
    [sg.Text('住所', size=(15, 1)), sg.InputText('△△△△村')],
    [sg.Text('電話番号', size=(15, 1)), sg.InputText('xxx-xxx-xxx')],
    [sg.Submit(button_text='実行ボタン')]
]

window = sg.Window('住所を入力', layout)

while True:
    event, values = window.read()

    if event is None:
        print('exit')
        break

    if event == '実行ボタン':
        show_message = "名前" + values[0] + "が入力されました。\n"
        show_message += "住所" + values[1] + "が入力されました。\n"
        show_message += "電話番号" + values[2] + "が入力されました。"
        print(show_message)

        sg.popup(show_message)

window.close()