from tkinter import *
import sqlite3
from tkinter import ttk

def ochered_view():
    root = Tk()
    root.title('Отображение очереди')
    root.minsize(800, 450)

    frame_number = Frame(root, width=150, height=150, bg='white')
    frame_number.place(x=0, y=0)

    frame_window = Frame(root, width=150, height=150, bg='white')
    frame_window.place(x=400, y=0)

    number_in_ochered = ttk.Label(frame_number, text="Номер в очереди")
    number_in_ochered.grid(row=1, column=2, sticky='w', padx=10, pady=10)

    window_in_ochered = ttk.Label(frame_window, text="Окно")
    window_in_ochered.grid(row=1, column=2, sticky='w', padx=10, pady=10)

    #Лейблы номера в очереди
    number1_l = ttk.Label(frame_number, text="1")
    number2_l = ttk.Label(frame_number, text="2")
    number3_l = ttk.Label(frame_number, text="3")
    number4_l = ttk.Label(frame_number, text="4")

    #Расположение лейблов номера на фрейме frame_number
    number1_l.grid(row=2, column=0, sticky='w', padx=10, pady=10)
    number2_l.grid(row=3, column=0, sticky='w', padx=10, pady=10)
    number3_l.grid(row=4, column=0, sticky='w', padx=10, pady=10)
    number4_l.grid(row=5, column=0, sticky='w', padx=10, pady=10)

    #Лейблы окна к которому подойти
    window1_l = ttk.Label(frame_window, text="1")
    window2_l = ttk.Label(frame_window, text="2")
    window3_l = ttk.Label(frame_window, text="3")
    window4_l = ttk.Label(frame_window, text="4")

    #Расположение лейблов окна к которму подойти на фрейме frame_window
    window1_l.grid(row=2, column=0, sticky='w', padx=10, pady=10)
    window2_l.grid(row=3, column=0, sticky='w', padx=10, pady=10)
    window3_l.grid(row=4, column=0, sticky='w', padx=10, pady=10)
    window4_l.grid(row=5, column=0, sticky='w', padx=10, pady=10)

    root.mainloop()


ochered_view()