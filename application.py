import tkinter as tk
from main import *

class Window(object):
    def __init__(self, title, geometry):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(geometry)
        self.titleLabel = tk.Label(self.root, text="Enter Digits of Pi:", font=("Arial", 25))
        self.piEntry = tk.Entry(self.root, font=("Arial", 25), width=round(int(geometry.split("x")[0]) * 3 / 4))
        self.nameLabel = tk.Label(self.root, text="Student Name:", font=("Arial", 25))
        self.nameEntry = tk.Entry(self.root, font=("Arial", 25), width=round(int(geometry.split("x")[0]) * 3 / 4))
        self.submitButton = tk.Button(self.root, text="Submit", font=("Arial", 25), command=self.submitStudentAttempt)
        self.titleLabel.pack()
        self.piEntry.pack()
        self.nameLabel.pack()
        self.nameEntry.pack()
        self.submitButton.pack()

    def submitStudentAttempt(self):
        name = self.nameEntry.get()
        digits = self.piEntry.get()
        self.nameEntry.delete(0, tk.END)
        self.nameEntry.insert(0, "")
        self.piEntry.delete(0, tk.END)
        self.piEntry.insert(0, "")
        correctDigits = check_student_attempt(digits)
        write_highest_pi_value("students/"+name+".txt", name, correctDigits)

    def update(self):
        self.root.update()

window1 = Window("Pi Checker Application", "300x300")
while True:
    window1.update()