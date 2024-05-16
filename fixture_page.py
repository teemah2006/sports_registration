from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import customtkinter
from project.model import get_ac_fixtures
from tkcalendar import DateEntry
import sqlite3
from CTkMessagebox import CTkMessagebox
from PIL import Image,ImageTk
import pywinstyles
class Fixture(customtkinter.CTkFrame):

    def __init__(self, master):
        super(Fixture, self).__init__(master)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid()
        self.canva = Canvas(self, bg='white', height=525, width=630)
        self.canva.grid(row=0, column=0, rowspan=28, columnspan=4, sticky='nsew')
        self.img = customtkinter.CTkImage(Image.open('./images/teampg.JPG'), size=(1500, 900))
        self.lbl_image = customtkinter.CTkLabel(self.canva, image=self.img)
        self.lbl_image.grid(row=0, column=0, sticky='nsew')

        self.canva.grid_rowconfigure(0, weight=1)
        self.canva.grid_columnconfigure(0, weight=1)
        self.create_widgets()
    def create_widgets(self):
        # self.lbl_title = customtkinter.CTkLabel(self, text="Fixtures this week",
        #                                         font=("", 20, 'bold'), bg_color='black', text_color='white')
        # self.lbl_title.grid(row=0, column=0, columnspan=3, pady=(0, 0))
        self.fixtures = get_ac_fixtures()
        space=' '
        pad = 50
        my_font = customtkinter.CTkFont(family='calibri',size=19)
        time_font = customtkinter.CTkFont(family='calibri',size=14)
        row = 0
        style = ttk.Style()
        style.configure('My.txt', relief='groove')
        for match in self.fixtures:
            if row%2 == 0:
                self.txt_fixtures = customtkinter.CTkTextbox(self.lbl_image, width=900, height=70,
                                                             bg_color='white', fg_color='orange', font=("Helvetica", 19),corner_radius=10)
            else:
                self.txt_fixtures = customtkinter.CTkTextbox(self.lbl_image, width=900, height=70,
                                                             bg_color='white', fg_color='beige',
                                                             font=("Helvetica", 19), corner_radius=10)
            self.txt_fixtures.grid()
            self.lbl_team1 = customtkinter.CTkLabel(self.txt_fixtures,text_color='black',bg_color='white',text=match[2],font=('calibri',20))
            pywinstyles.set_opacity(self.lbl_team1, color='white')
            self.lbl_team1.grid(row=0,column=0,sticky=W,padx=(10,0))

            self.lbl_vs = customtkinter.CTkLabel(self.txt_fixtures,text_color='black',bg_color='white',text='VS',font=('calibri',20))
            pywinstyles.set_opacity(self.lbl_vs, color='white')
            self.lbl_vs.grid(row=0, column=0, sticky=W, padx=(260, 0))

            self.lbl_team2 = customtkinter.CTkLabel(self.txt_fixtures, text_color='black', bg_color='white',
                                                    text=match[4], font=('calibri', 20))
            pywinstyles.set_opacity(self.lbl_team2, color='white')
            self.lbl_team2.grid(row=0, column=0, sticky=W, padx=(460, 0))

            self.lbl_date = customtkinter.CTkLabel(self.txt_fixtures, text_color='black', bg_color='white',
                                                    text=f'Date: {match[1]}', font=('calibri', 20))
            pywinstyles.set_opacity(self.lbl_date, color='white')
            self.lbl_date.grid(row=0, column=1, sticky=W, padx=(0,10))
            # self.txt_fixtures.configure(font=my_font)
            # self.txt_fixtures.insert('-1.0',f'{match[2]} {'vs':^100} {match[4]} {match[1]:>40}\n')
            # #self.txt_fixtures.configure(font=time_font)
            # self.txt_fixtures.insert('5.0',f'{'12:00':^100}')
            self.txt_fixtures.configure(state='disabled')

            pywinstyles.set_opacity(self.txt_fixtures,color='white')
            self.txt_fixtures.grid(row=0,column=0,sticky=N,pady=(pad,0))
            pad += 80
            row += 1
