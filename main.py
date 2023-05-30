from tkinter import *
import sqlite3

root = Tk()
root.title("Очередь с регистрацией")

queue = []
next_number = 1


def add_to_queue():
    global next_number

    queue.append(next_number)
    queue_number_label.config(text=next_number)
    next_number += 1

    conn = sqlite3.connect('mydatabase.db')

    # Добавление данных
    cursor = conn.cursor()
    entry_name_get = queue_name.get()
    cursor.execute("""Update mytable set 'name' = ? where id = ? """, (entry_name_get, next_number))

    # Сохранение изменений
    conn.commit()




# добавим элементы интерфейса
label = Label(root, text="Вы стоите в очереди под номером:")
label.pack()

queue_number_label = Label(root, text="")
queue_number_label.pack()

queue_name = Entry(root)
queue_name.pack()


button = Button(root, text="Встать в очередь")
button.pack()
button.config(command=add_to_queue)

root.mainloop()
