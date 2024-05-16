#landing page
from tkinter import *
from tkinter import ttk
from sport_reg_form import Application
from player_form import Player_app
from coach_form import Coach_app
import customtkinter

class Landing_page(customtkinter.CTkFrame):

    def __init__(self, master, height=225, width=230):
        super(Landing_page,self).__init__(master,width=width,height=height)

        self.sport = StringVar()
        self.registrar = StringVar()
        self.no_players = StringVar()
        self.no_coach = StringVar()
        self.level = StringVar()
        self.age = IntVar()
        self.grid()
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.canva = Canvas(self, height=225, width=230,background='white')
        self.img = PhotoImage(file= 'C:/Users/HP/Downloads/perfectbg2.PNG')
        #self.canva.pack(expand=YES, fill=BOTH)
        self.canva.grid(row=0,column=0,sticky= 'nsew')
        self.canva.grid_rowconfigure(0,weight=3)
        self.canva.grid_columnconfigure(0,weight=3)
        self.canva.create_image(500, 400, image=self.img, anchor='center')

        # #canva.configure(bg= 'light blue')
        # canva.grid(row=0,column=0,rowspan=25,columnspan=5,sticky= 'nsew')


        self.create_widgets()

    def create_widgets(self):
        self.lbl_title = Label(self.canva,text= 'WELCOME TO NATIONAL SPORTS FESTIVAL REGISTRATION PORTAL',font=("Times New Roman","20","bold"),background='white')
        self.lbl_title.grid(row=0, column=0,pady=(0,30),sticky=N)

        self.separator = ttk.Separator(self.canva,orient='vertical')
        self.separator.grid(row=0,column=0,sticky='ns',padx=(67,0),pady=(37,0))
        decription1 = """CATEGORY TEAM: registar as a team, play blahh
no need to register as individual players or
coach again since you are a team already """
        self.lbl_description1 = customtkinter.CTkLabel(self.canva,text=decription1,text_color='black',font=("calibri",16,"bold"))
        self.lbl_description1.grid(row=0,column=0,sticky=W,pady=(5,400),padx=(5,90))
        decription2 = """CATEGORY COACH: registar as a team, play blahh
        no need to register as individual players or
        coach again since you are a team already """
        self.lbl_description2 = customtkinter.CTkLabel(self.canva, text=decription2, text_color='black',
                                                       font=("calibri", 16, "bold"))
        self.lbl_description2.grid(row=0, column=0, sticky=W, pady=(100, 200), padx=(5, 90))
        decription3 = """CATEGORY PLAYER: registar as a team, play blahh
                no need to register as individual players or
                coach again since you are a team already """
        self.lbl_description3 = customtkinter.CTkLabel(self.canva, text=decription3, text_color='black',
                                                       font=("calibri", 16, "bold"))
        self.lbl_description3.grid(row=0, column=0, sticky=W, pady=(200, 0), padx=(5, 90))

        self.btn_team = customtkinter.CTkButton(self.canva,text_color='black',text='TEAM',bg_color='white',fg_color='beige',width=250)
        self.btn_team.grid(row=0,column=0,sticky=E,pady=(10,100),padx=(90,10))
        self.btn_coach = customtkinter.CTkButton(self.canva, text_color='black', text='COACH', bg_color='white',
                                                fg_color=('beige', 'yellow'), width=250)
        self.btn_coach.grid(row=0, column=0, sticky=E, pady=(50, 50), padx=(90, 10))
        self.btn_player = customtkinter.CTkButton(self.canva, text_color='black', text='PLAYER', bg_color='white',
                                                 fg_color=('beige', 'yellow'), width=250)
        self.btn_player.grid(row=0, column=0, sticky=E, pady=(100, 0), padx=(90, 10))

        # self.lbl_registrar = Label(self.canva, text= 'Select Category', font=("", '16','bold'))
        # self.lbl_registrar.grid(row=5,column=3,columnspan=3,pady=(5,5))
        # self.cmb_registrar = customtkinter.CTkComboBox(self.canva, width= 230, variable=self.registrar, values=['coach','player','Team'])
        # self.cmb_registrar.grid(row=6,column=3,columnspan=3,pady=(5,5))
        # self.btn_next = customtkinter.CTkButton(self.canva, text='NEXT',
        #                                         command=self.next_frame)
        # self.btn_next.grid(row=7,column=3,columnspan=3,pady=(5,5))

    def next_frame(self):
            registrar = self.cmb_registrar.get()
            if registrar == 'player':
                app = Player_app(self.master)
                app.grid(row=0, column=0, sticky='nsew')

                app.tkraise()
                # window.tkraise(app)
                # window.mainloop()
            elif registrar == 'coach':
                app = Coach_app(self.master)
                app.grid(row=0, column=0, sticky='nsew')


                app.tkraise()
            elif registrar == 'Team':
                app = Application(self.master)
                app.grid(row=0, column=0, sticky='nsew')


    def back(self):
        # app = Application(self.master)
        # app.grid(row=0, column=0,sticky= 'nsew')
        self.grid(row=0,column=0,sticky='nsew')
        self.tkraise()
    # def process(self):
    #     pass

customtkinter.set_appearance_mode('light')
#customtkinter.set_default_color_theme('blue')
window = customtkinter.CTk()
window.title("MULTI-VENUE SPORTS REGISTRATION FORM")
window.geometry("680x625")
window.grid_rowconfigure(0,weight=1)
window.grid_columnconfigure(0,weight=1)

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
