import tkinter

root = tkinter.Tk()
root.title('Sample2')
root.geometry("400x400")

def clicked():
    print("Button is clicked.")

button = tkinter.Button(root, text=" ボタン", command=clicked)
button.grid()

root.mainloop()