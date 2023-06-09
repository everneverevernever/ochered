from tkinter import *
from sqlite3 import *
from tkinter import ttk

def ochered_view():
    def get_data_from_database():
        # здесь код для извлечения данных из базы данных
        # например, можно использовать модуль sqlite3 для работы с SQLite
        with connect('mydatabase.db') as db:
            cursor = db.cursor()
            cursor.execute("SELECT id FROM mytable")
            row = cursor.fetchall()
            column1_data = row[0]
            column2_data = row[1]
            column3_data = row[2]
            column4_data = row[3]
            return column1_data, column2_data, column3_data, column4_data


    def refresh():
        column1_data, column2_data, column3_data, column4_data = get_data_from_database()
        new_text = f"Column 1: {column1_data} | Column 2: {column2_data} | Column 3: {column3_data}"
        number1_l.config(text=new_text)


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