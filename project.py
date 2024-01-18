import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *

class GradeWindow:
    def __init__(self, master):
        self.master = master
        master.title("Atzīmju ievade")
        master.configure(bg="white")
        self.subjects = ["alg.prog", "la", "mat", "dat.gr", "dat.arh"]
        self.work_types = ["Lab.d", "Ēksāmens", "Tests", "Pr.d"]
        self.grades = {}
        self.create_widgets()

    def create_widgets(self):
        self.greeting_label = Label(self.master, text="Laipni lūdzam atzīmju ievades programmā!", bg="white", fg="black", font=("arial", 16))
        self.greeting_label.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

     #prieksemta nosaukumi
        self.subject_labels = []
        for i, subject in enumerate(self.subjects):
            label = Label(self.master, text=subject, bg="white", fg="black", font=("arial", 14))
            label.grid(row=1, column=i, padx=10, pady=10)
            self.subject_labels.append(label)

#darba veidu nosaukumi
        self.work_type_labels = []
        for i, work_type in enumerate(self.work_types):
            label = Label(self.master, text=work_type, bg="white", fg="black", font=("arial", 14))
            label.grid(row=i+2, column=0, padx=10, pady=10)
            self.work_type_labels.append(label)

#Atz.ievades laukumi
        self.grade_entries = {}
        for i, subject in enumerate(self.subjects):
            for j, work_type in enumerate(self.work_types):
                entry = Entry(self.master, bg="white", fg="black", font=("arial", 14), width=5)
                entry.grid(row=j+2, column=i+1, padx=10, pady=10)
                self.grade_entries[(subject, work_type)] = entry

        self.save_button = Button(self.master, text="Saglabāt atzīmes", bg="white", fg="black", font=("arial", 14), command=self.save_grades)
        self.save_button.grid(row=6, column=0, columnspan=5, padx=10, pady=10)

 #atz.saglab
    def save_grades(self):
        for key, entry in self.grade_entries.items():
            subject, work_type = key
            grade = entry.get()
            if grade:
                grade = float(grade)
                if subject not in self.grades:
                    self.grades[subject] = {}
                self.grades[subject][work_type] = grade

        self.master.destroy()

#atz.ieraks.excel
def write_grades_to_excel(grades, filename, factor):
    df = pd.DataFrame(grades)
    df = df * factor
    df.to_excel(filename)

#grafiks un vid.atz
def plot_average_grades(grades, filename):
    df = pd.DataFrame(grades)
    averages = df.mean()

  #krāsa grafikam 
    colors = []
    for average in averages:
        if average < 4:
            colors.append("red")
        else:
            colors.append("green")

 #grafiks
    plt.figure(figsize=(10, 6))
    plt.bar(averages.index, averages, color=colors)
    plt.xlabel("Priekšmets", fontsize=14)
    plt.ylabel("Vidējā atzīme", fontsize=14)
    plt.title("Vidējās atzīmes priekšmetos", fontsize=16)
    plt.ylim(0, 10)
    plt.savefig(filename)

root = Tk() #gal.logs
grade_window = GradeWindow(root)
root.mainloop() #pal. notik. apstr. ciklu
grades = grade_window.grades
excel_filename = "C:\\Users\\user\\Documents\\grades.xlsx"
factor = 1
write_grades_to_excel(grades, excel_filename, factor)
plot_filename = "C:\\Users\\user\\Documents\\average_grades.png"
plot_average_grades(grades, plot_filename)