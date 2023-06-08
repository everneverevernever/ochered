from tkinter import *
from tkinter import ttk
import sqlite3

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


    ochered_window = Tk()
    ochered_window.title('Отображение очереди')
    ochered_window.minsize(800, 450)

    frame_number = Frame(ochered_window, width=150, height=150, bg='white')
    frame_number.place(x=0, y=0)

    frame_window = Frame(ochered_window, width=150, height=150, bg='white')
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

def ochered_zapis():
    def add_to_queue():
        global next_number

        queue.append(next_number)
        queue_number_label.config(text=next_number)
        next_number += 1

        conn = sqlite3.connect('mydatabase.db')

        # Добавление данных
        cursor = conn.cursor()
        entry_name_get = queue_name.get()
        insert_inf = (entry_name_get,)
        query = (""" INSERT INTO mytable(name) VALUES (?)""")

        cursor.execute(query, insert_inf)

        # Сохранение изменений
        conn.commit()

    window_zapis = Tk()
    window_zapis.title("Очередь с регистрацией")

    queue = []
    next_number = 1

    # добавим элементы интерфейса
    label = Label(window_zapis, text="Вы стоите в очереди под номером:")
    label.pack()

    queue_number_label = Label(window_zapis, text="")
    queue_number_label.pack()

    queue_name = Entry(window_zapis)
    queue_name.pack()

    button = Button(window_zapis, text="Встать в очередь")
    button.pack()
    button.config(command=add_to_queue)


# Создаем главное окно приложения
root = Tk()
root.geometry('450x400')
root.title('Моя программа')

# Создаем два фрейма
left_frame = Frame(root, bd=2, relief='groove')
left_frame.place(x=20, y=20, width=400, height=200)

# Создаем кнопки на левом фрейме
button1 = ttk.Button(left_frame, text='Просмотр очереди', command=ochered_view)
button1.pack(pady=20)
button2 = ttk.Button(left_frame, text='Запись в очередь', command=ochered_zapis)
button2.pack(pady=20)

# Создаем кнопку выход на нижнем фрейме
button3 = ttk.Button(left_frame, text='Выход', command=root.destroy)
button3.pack(pady=20)

# Запускаем главный цикл
root.mainloop()