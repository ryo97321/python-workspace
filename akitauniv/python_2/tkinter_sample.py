import tkinter

# フレーム1（最上位フレーム）
frame1 = tkinter.Tk()
frame1.title('Frame1')
frame1.geometry("400x400")

# フレーム2（子フレーム）
frame2 = tkinter.Frame(frame1)

# ラベル1, 2（フレーム2に配置）
label1 = tkinter.Label(frame2, text="This is the Label_1.")
label2 = tkinter.Label(frame2, text="This is the Label_2.")

# ラベル3（フレーム1に配置）
label3 = tkinter.Label(frame1, text="This is the Label_3.")

# ラベル1, 2をフレーム2に配置
label1.pack(side=tkinter.LEFT)
label2.pack(side=tkinter.RIGHT)

# フレーム2を表示
frame2.grid()

# ラベル3をフレーム1に表示
label3.grid()

frame1.mainloop()
