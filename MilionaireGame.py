from tkinter import *
from tkinter import ttk
import random


def lose_screen(a):
    a.destroy()
    lose = Toplevel()
    lose.title("Ви програли")
    lose.geometry("900x600+325+100")
    lose.config(background="dark blue")
    lose_label = Label(lose, text="Ви програли", font=("Comic Sans MS", 20), background="dark blue",
                       foreground="yellow")
    lose_label.pack(pady=50)


question_first1 = {"В якому році було проголошено незалежність України": ["1991", "1992", "1990", "1941"],
                       "Як звали коня Александра Македонського": ["Мустанг", "Буцефал", "Спіріт", "Плотва"],
                       "Хто засновник компанії Apple": ["Біл Гейст", "Ілон Макс", "Стів Джобс", "Марк Цукерберг"]}


def check_answer():
    if check == question_first1["В якому році було проголошено незалежність України"][0]:
        print("Вірно")
    else:
        lose_screen()


def first_question(previous_window):
    previous_window.destroy()
    screen1 = Toplevel(prog)
    screen1.title("Перше питання")
    screen1.geometry("900x600+325+100")
    screen1.config(background="dark blue")
    game_label = Label(screen1, text="Перше питання", font=("Comic Sans MS", 20), background="dark blue",
                       foreground="yellow")
    random_question1 = random.choice(list(question_first1.keys()))
    question_label = Label(screen1, text=random_question1, font=("Comic Sans MS", 20), background="dark blue",
                           foreground="yellow")
    game_label.pack(pady=50)
    question_label.pack(pady=50)
    answer_button1 = Button(screen1, text=question_first1[random_question1][1],
                            font="arial", width=10)
    answer_button1.place(x=50, y=400)
    answer_button2 = Button(screen1, text=question_first1[random_question1][0],
                            width=10, font="arial")
    answer_button2.place(x=50, y=450)
    answer_button3 = Button(screen1, text=question_first1[random_question1][2],
                            width=10, font="arial")
    answer_button3.place(x=740, y=400)
    answer_button4 = Button(screen1, text=question_first1[random_question1][3],
                            width=10, font="arial")
    answer_button4.place(x=740, y=450)


def back_to_main(window):
    window.destroy()
    prog.deiconify()


def start_game():
    prog.withdraw()
    new_window = Toplevel(prog)
    new_window.title("Дерево питань")
    new_window.geometry("900x600+325+100")
    new_window.config(background="dark blue")

    game_label = Label(new_window, text="Дерево питань", font=("Comic Sans MS", 20), background="dark blue",
                       foreground="white")
    game_label.pack(pady=50)
    start_button = Button(new_window, text="Почати", font="Arial", width=10, command=lambda: first_question(new_window))
    start_button.place(x=400, y=400)
    back_button = Button(new_window, text="Назад", font="Arial", width=10, command=lambda: back_to_main(new_window))
    back_button.place(x=400, y=500)


def records():
    prog.withdraw()
    records_window = Toplevel(prog)
    records_window.title("Рекорди")
    records_window.geometry("900x600+325+100")
    records_window.config(background="dark blue")
    game_label = Label(records_window, text="Рекорди", font=("Comic Sans MS", 20), background="dark blue",
                       foreground="white")
    game_label.pack(pady=50)
    back_button = Button(records_window, text="Назад", font="Arial",
                         command=lambda: back_to_main(records_window))
    back_button.place(x=400, y=500)


prog = Tk()
prog.title("Хто хоче стати міліонером")
prog.geometry("900x600+325+100")
prog.resizable(width=False, height=False)
prog.config(background="dark blue")
main_text = Label(prog, text="Хто хоче стати міліонером!?", background="dark blue", foreground="yellow",
                  font=("Comic Sans MS", 30, "bold", "italic"))
main_text.place(x=230, y=100)
button_start = Button(prog, text="Почати гру!", font="Arial", width=10, command=lambda: start_game())
button_start.place(x=380, y=300)
button_records = Button(prog, text="Рекорди", font="Arial", width=10, command=lambda: records())
button_records.place(x=380, y=350)
button_exit = Button(prog, text="Вихід", font="Arial", width=10, command=lambda: prog.quit())
button_exit.place(x=380, y=400)

prog.mainloop()
