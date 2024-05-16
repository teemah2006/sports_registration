#main page
from tkinter import *
from tkinter import ttk
from fixture_page import Fixture
from PIL import Image
import pywinstyles
from sport_reg_form import Application
from player_form import Player_app
from coach_form import Coach_app
import customtkinter
from admin_login import Admin
from leader_board import Board
class Landing_page(customtkinter.CTkFrame):
    def __init__(self, master):
        super(Landing_page,self).__init__(master)
        self.sport = StringVar()
        self.registrar = StringVar()
        self.no_players = StringVar()
        self.no_coach = StringVar()
        self.level = StringVar()
        self.age = IntVar()
        self.grid()
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.canva = customtkinter.CTkCanvas(self, height=625, width=630)
        self.img = customtkinter.CTkImage(Image.open('./images/sport_background.JPG'),size=(1500,900))
        ti = self.img

        #self.canva.pack(expand=YES, fill=BOTH)
        #self.canva.grid(row=0,column=0,sticky= 'nsew')

        self.lbl_image = customtkinter.CTkLabel(self,image=self.img,text=' ')
        self.lbl_image.grid(row=0,column=0,sticky = 'nsew')
        # self.canva.grid_rowconfigure(0, weight=1)
        # self.canva.grid_columnconfigure(0, weight=1)
        # self.lbl_image.grid_rowconfigure(0,weight=1)
        # self.lbl_image.grid_columnconfigure(0,weight=1)


        # #canva.configure(bg= 'light blue')
        # canva.grid(row=0,column=0,rowspan=25,columnspan=5,sticky= 'nsew')

        self.menu()
        self.create_widgets()

    def create_widgets(self):
        self.lbl_title = customtkinter.CTkLabel(self.lbl_image,text= 'WELCOME TO INTERNATIONAL SPORTS FESTIVAL REGISTRATION PORTAL',bg_color='black',font=("Times New Roman",19,"bold"),text_color='white')
        self.lbl_title.grid(row=0, column=0, columnspan=3,padx=(20,20),pady=(20),sticky = N)
        pywinstyles.set_opacity(self.lbl_title, color="black")
        #self.canva.create_text(1500, 400, text='WELCOME TO NATIONAL SPORTS FESTIVAL REGISTRATION PORTAL', anchor='center',fill='white')


        self.lbl_registrar = customtkinter.CTkLabel(self.lbl_image, text= 'Select Category'.upper(), font=("calibri", 17,'bold'),bg_color='black',text_color='white',width=250)
        self.lbl_registrar.grid(row=0,column=0,pady=(0,450))
        pywinstyles.set_opacity(self.lbl_registrar, color="black")
        icon = customtkinter.CTkImage(Image.open('./images/team_icon.webp'), size=(30, 30))
        self.btn_team = customtkinter.CTkButton(self.lbl_image, text_color='black', text='  TEAM',image=icon, bg_color='black',
                                                fg_color='beige', width=250,command=self.team_frame,hover_color='yellow')
        self.btn_team.grid(row=0, column=0, pady=(10, 200), padx=(90, 100))
        icon = customtkinter.CTkImage(Image.open('./images/coach_icon.jpg'), size=(30, 30))
        self.btn_coach = customtkinter.CTkButton(self.lbl_image, text_color='black',image=icon, text='  COACH', bg_color='black',
                                                 fg_color=('beige', 'yellow'), width=250,command=self.coach_frame,hover_color='yellow')
        self.btn_coach.grid(row=0, column=0, pady=(50, 100), padx=(90, 100))
        icon = customtkinter.CTkImage(Image.open('./images/player_icon.png'), size=(30, 30))
        self.btn_player = customtkinter.CTkButton(self.lbl_image, text_color='black',image=icon, text='  PLAYER', bg_color='black',
                                                  fg_color=('beige', 'yellow'), width=250,command=self.player_frame,hover_color='yellow')
        self.btn_player.grid(row=0, column=0, pady=(100, 0), padx=(90, 100))

        # self.cmb_registrar = customtkinter.CTkComboBox(self.lbl_image, width= 230, variable=self.registrar, values=['coach','player','Team'],bg_color='black')
        # self.cmb_registrar.grid(row=0,column=0,columnspan=3,pady=(25,5))
        # self.btn_next = customtkinter.CTkButton(self.lbl_image, text='NEXT',
        #                                         command=self.next_frame)
        # self.btn_next.grid(row=7,column=3,columnspan=3,pady=(5,5))

    def player_frame(self):
                app = Player_app(self.master)
                app.grid(row=0, column=0, sticky='nsew')

                app.tkraise()
                # window.tkraise(app)
                # window.mainloop()
    def coach_frame(self):
                app = Coach_app(self.master)
                app.grid(row=0, column=0, sticky='nsew')
                app.tkraise()
    def team_frame(self):
                app = Application(self.master)
                app.grid(row=0, column=0, sticky='nsew')
                app.tkraise()

    def back(self):
        # app = Application(self.master)
        # app.grid(row=0, column=0,sticky= 'nsew')
        self.grid(row=0,column=0,sticky='nsew')
        self.tkraise()
    # def process(self):
    #     pass
    def menu(self):
        app = Fixture(self.master)
        app.grid(row=0, column=0, sticky='nsew')
        admin = Admin(self.master)
        admin.grid(row=0,column=0,sticky='nsew')
        board = Board(self.master)
        board.grid(row=0, column=0, sticky='nsew')
        menubar = Menu(self)
        filemenu = Menu(menubar)
        filemenu.add_command(label='Match fixtures',font=(" ",'12'),command=app.tkraise)
        filemenu.add_command(label='Leader Board',font=(" ",'12'),command=board.tkraise)
        menubar.add_command(label='Register',command=self.tkraise)
        menubar.add_cascade(label='View',menu=filemenu)
        menubar.add_command(label='Admin Login', command=admin.tkraise)
        window.config(menu=menubar)

customtkinter.set_appearance_mode('light')
#customtkinter.set_default_color_theme('Red')
window = customtkinter.CTk()
window.title("MULTI-VENUE SPORTS REGISTRATION FORM")
window.geometry("680x725")
window.grid_rowconfigure(0,weight=1)
window.grid_columnconfigure(0,weight=1)

#window.iconbitmap('C:/Users/HP/Downloads/icon3.PNG')


#using iconphoto() to create icon
# icon = PhotoImage(file='C:/Users/HP/Downloads/sport_icon.PNG')
# window.iconphoto(False,icon)
# if "__name__" == "main":

app= Landing_page(window)
app.grid(row=0,column=0,sticky= 'nsew')

# canva = Canvas(app,  height=300, width=300)
# canva.grid(row=0,column=0)
#img = PhotoImage(file= 'C:/Users/HP/Downloads/sport_icon.PNG')
#
# canva.create_image(row=0,column=0,image=img)


app.tkraise()
# app.mainloop()
window.mainloop()
