from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
import os

class Parser():
    root = Tk()
    root.title('Parser')
    # root.geometry('200x250')

    def __init__(self, path_to_folder=fd.askdirectory()):
        self.str_to_write = ''
        self.path_to_folder = path_to_folder
        self.expansion = ['doc', 'docx', 'zip', 'rar', '7z', 'txt', 'py']
        self.choice_expansion = ''

    def serch_file(self):
        wook = 0
        for path, dirs, files in os.walk(self.path_to_folder):
            for file in files:
                x = file.split('.')
                if len(x) > 1:
                    if x[-1] == self.choice_expansion:
                        self.str_to_write = path+file
                        self.write_to_file()
                        wook +=1
        if wook < 1:
            messagebox.showinfo(title='Повідомлення', message='Нічого не знайдено')
            quit()
        else:
            quit()

    def write_to_file(self):
        with open(f'result {self.choice_expansion}.txt', 'a') as file:
            file.write(self.str_to_write + '\n')

    def expansion_choise(self, listbox):
        self.choice_expansion = self.expansion[listbox.curselection()[0]]
        listbox.destroy()
        self.btn_choise.destroy()

    def shell(self):
        variable = Variable(value=self.expansion)
        listbox = Listbox(listvariable=variable)
        listbox.grid()
        self.btn_choise = Button(text='Вибір формату', command=lambda: self.expansion_choise(listbox))
        self.btn_choise.grid()
        Button(text='Початок сканування', command=self.serch_file).grid()


if __name__ == '__main__':
    app = Parser()
    app.shell()
    mainloop()