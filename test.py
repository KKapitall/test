#Составить тест из пяти вопросов. На каждый вопрос должно быть 4 ответа.Вывести результаты теста: сколько правильных и неправильных ответов, сколько % правильных ответов.
from tkinter import messagebox
import tkinter as tk
import customtkinter
class testapp:
    def __init__(self,master) -> None:
        self.master = master
        self.questions = ["Как называется столица Италии?", "Как называется столица Франции?"]
        self.answers = [["Рим", "Милан", "Неаполь", "Турин"], ["Париж", "Марсель", "Лион", "Тулуза"]]
        self.correct_answers = ["a", "a"]
        self.current_question = 0
        self.user_answers = []
        self.button_pressed = tk.BooleanVar()
        self.button_pressed.set(False)
        self.check = True
        for i in range(len(self.questions)):
            self.user_answers.append(customtkinter.StringVar())

        self.setup_uestions()
    def setup_uestions(self):
        self.voprosi = customtkinter.CTkLabel(self.master, text = self.questions[self.current_question])
        self.voprosi.pack()
        self.knopka_a =customtkinter.CTkRadioButton(self.master,text = self.answers[self.current_question][0],variable=self.user_answers[self.current_question], value="a")
        self.knopka_a.pack()
        self.knopka_b =customtkinter.CTkRadioButton(self.master,text = self.answers[self.current_question][1],variable=self.user_answers[self.current_question], value="b")
        self.knopka_b.pack()
        self.knopka_d =customtkinter.CTkRadioButton(self.master,text = self.answers[self.current_question][2],variable=self.user_answers[self.current_question], value="c")
        self.knopka_d.pack()
        self.knopka_c =customtkinter.CTkRadioButton(self.master,text = self.answers[self.current_question][3],variable=self.user_answers[self.current_question], value="d")
        self.knopka_c.pack()
        self.knopka = customtkinter.CTkButton(self.master,text = "ответить", command=self.check_answers)
        self.knopka.pack()
        self.endtest = customtkinter.CTkButton(self.master,text = "завершить тест", command=self.EndTest)
        self.endtest.pack()

    def EndTest(self):
        root.destroy()
        correct = sum(1 for i in range(len(self.questions)) if self.user_answers[i].get() == self.correct_answers[i])
        incorrect = len(self.questions) - correct
        percent = (correct / len(self.questions)) * 100
        messagebox.showinfo("Результаты", f"Правильных ответов: {correct}\nНеправильных ответов: {incorrect}\nПроцент правильных ответов: {percent:.2f}%")



    def check_answers(self):
        if self.user_answers[self.current_question].get() == self.correct_answers[self.current_question]:
            messagebox.showinfo("Ответ", "Вы ответили правильно!")
        else:
            messagebox.showinfo("Ответ", "Вы ответили неправильно. Попробуйте еще раз.")
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.voprosi.configure(text=self.questions[self.current_question])
            self.knopka_a.configure(text=self.answers[self.current_question][0], variable=self.user_answers[self.current_question])
            self.knopka_b.configure(text=self.answers[self.current_question][1], variable=self.user_answers[self.current_question])
            self.knopka_c.configure(text=self.answers[self.current_question][2], variable=self.user_answers[self.current_question])
            self.knopka_d.configure(text=self.answers[self.current_question][3], variable=self.user_answers[self.current_question])
        else:
            self.EndTest()
            correct = sum(1 for i in range(len(self.questions)) if self.user_answers[i].get() == self.correct_answers[i])
            incorrect = len(self.questions) - correct
            percent = (correct / len(self.questions)) * 100
            messagebox.showinfo("Результаты", f"Правильных ответов: {correct}\nНеправильных ответов: {incorrect}\nПроцент правильных ответов: {percent:.2f}%")
    


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
root = customtkinter.CTk()
app= testapp(root)
root.mainloop()