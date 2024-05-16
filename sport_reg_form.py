#team page
from tkinter import *
from tkinter import ttk
import customtkinter
from PIL import Image
import pywinstyles
from CTkMessagebox import CTkMessagebox
import sqlite3
from project.model import get_country
class Application(customtkinter.CTkFrame):

    def __init__(self, master):
        super(Application,self).__init__(master)

        self.sport = StringVar()
        self.country = StringVar()
        self.no_players = IntVar()
        self.no_coach = IntVar()
        self.level = StringVar()
        self.age = StringVar()
        # self.grid_rowconfigure(0, weight=1)
        # self.grid_columnconfigure(0, weight=1)
        self.grid()
        self.canva = customtkinter.CTkCanvas(self, height=525, width=630,background='white')
        #canva.configure(bg= 'light blue')
        self.canva.grid(row=0,column=0,rowspan=33,columnspan=4,sticky= 'nsew')
        self.img = customtkinter.CTkImage(Image.open('./images/playerbg.JPG'),size=(1500,900))
        self.lbl_image = customtkinter.CTkLabel(self.canva,image=self.img)
        self.lbl_image.grid(row=0,column=0,sticky='nsew')
        self.canva.grid_rowconfigure(0, weight=1)
        self.canva.grid_columnconfigure(0, weight=1)
        self.create_widgets()

    def create_widgets(self):
        self.lbl_title = customtkinter.CTkLabel(self,text= "Team's Registration Form",font=("calibri",20,"bold"),bg_color='black',text_color='white')
        self.lbl_title.grid(row= 0, column= 0,columnspan=4)
        pywinstyles.set_opacity(self.lbl_title,color='black')

        self.lbl_teamname = customtkinter.CTkLabel(self, text='Team Name:', font=("calibri", 16,'bold'),bg_color='black',text_color='white')
        self.lbl_teamname.grid(row= 1, column= 0, sticky= W,padx= (5,5))
        pywinstyles.set_opacity(self.lbl_teamname, color='black')
        self.ent_teamname = customtkinter.CTkEntry(self, width= 300,bg_color='black')
        self.ent_teamname.grid(row= 2, column= 0, sticky = W,padx= (5,5))
        pywinstyles.set_opacity(self.ent_teamname, color='black')

        self.lbl_country = customtkinter.CTkLabel(self, text= 'Country', font=("calibri", 16,'bold'),bg_color='black',text_color='white')
        self.lbl_country.grid(row= 1, column= 2, sticky= W)
        pywinstyles.set_opacity(self.lbl_country, color='black')
        self.cmb_country = customtkinter.CTkComboBox(self, width= 230, variable=self.country, values=get_country(),bg_color='black')
        self.cmb_country.grid(row= 2, column= 2, sticky= W)
        pywinstyles.set_opacity(self.cmb_country, color='black')

        # empty space
        # self.lbl_empty = customtkinter.CTkLabel(self, text="",bg_color='black')
        # self.lbl_empty.grid(row=3, column=0,padx= (5,5))
        # pywinstyles.set_opacity(self.lbl_empty, color='black')
        #
        # #separator
        # self.horizontal_sep = ttk.Separator(self, orient='horizontal')
        # self.horizontal_sep.grid(row= 5, column= 0,columnspan=4,sticky= 'we',padx= (5,5))


        #sports
        # self.lbl_sports = customtkinter.CTkLabel(self, text="Sport (select only one)", font=("", 16,'bold'),bg_color='black',text_color='white')
        # self.lbl_sports.grid(row= 6, column= 0, sticky= W,padx= (5,5))
        # pywinstyles.set_opacity(self.lbl_sports, color='black')
        # self.rad_fball = customtkinter.CTkRadioButton(self,text='Football', variable=self.sport,value='Football',text_color='white',bg_color='black',font=('',12))
        # self.rad_fball.grid(row= 7, column= 0, sticky =W,padx= (5,5))
        # pywinstyles.set_opacity(self.rad_fball, color='black')
        # self.rad_bball =customtkinter.CTkRadioButton(self,text='Basketball', variable=self.sport,value='Basketball',text_color='white',bg_color='black',font=('',12))
        # self.rad_bball.grid(row=7, column=1, sticky=W)
        # pywinstyles.set_opacity(self.rad_bball, color='black')
        # self.rad_cricket = customtkinter.CTkRadioButton(self,text='Cricket', variable=self.sport,value='Cricket',text_color='white',bg_color='black',font=('',12))
        # self.rad_cricket.grid(row=7, column=2, sticky=W)
        # pywinstyles.set_opacity(self.rad_cricket, color='black')
        # self.rad_vball = customtkinter.CTkRadioButton(self,text='Volleyball', variable=self.sport,value='Volleyball',text_color='white',bg_color='black',font=('',12))
        # self.rad_vball.grid(row=7, column=3, sticky=W)
        # pywinstyles.set_opacity(self.rad_vball, color='black')
        # self.lbl_empty = customtkinter.CTkLabel(self, text=" ", bg_color='black')
        # self.lbl_empty.grid(row=8, column=0, padx=(5, 5))
        # pywinstyles.set_opacity(self.lbl_empty, color='black')
        # self.rad_baseball = customtkinter.CTkRadioButton(self,text='Baseball', variable=self.sport,value='Baseball',text_color='white',bg_color='black',font=('',12))
        # self.rad_baseball.grid(row=9, column=0, sticky=W,padx= (5,5))
        # pywinstyles.set_opacity(self.rad_baseball, color='black')
        # self.rad_tennis = customtkinter.CTkRadioButton(self,text='Tennis', variable=self.sport,value='Tennis',text_color='white',bg_color='black',font=('',12))
        # self.rad_tennis.grid(row=9, column=1, sticky=W)
        # pywinstyles.set_opacity(self.rad_tennis, color='black')
        # self.rad_swimming = customtkinter.CTkRadioButton(self,text='Swimming', variable=self.sport,value='Swimming',text_color='white',bg_color='black',font=('',12))
        # self.rad_swimming.grid(row=9, column=2, sticky=W)
        # pywinstyles.set_opacity(self.rad_swimming, color='black')
        # self.rad_boxing = customtkinter.CTkRadioButton(self,text='Boxing', variable=self.sport,value='Boxing',text_color='white',bg_color='black',font=('',12))
        # self.rad_boxing.grid(row=9, column=3, sticky=W)
        # pywinstyles.set_opacity(self.rad_boxing, color='black')
        # self.rad_fball.select()


        self.horizontal_sep = ttk.Separator(self, orient='horizontal')
        self.horizontal_sep.grid(row=3, column=0,columnspan= 4,sticky= 'ew',padx= (5,5))
        # self.lbl_empty = customtkinter.CTkLabel(self, text=" ",bg_color='black')
        # self.lbl_empty.grid(row=4, column=0,padx= (5,5))
        # pywinstyles.set_opacity(self.lbl_empty, color='black')

        self.lbl_player_no = customtkinter.CTkLabel(self, text= 'No of players', font=("calibri", 16,'bold'),bg_color='black',text_color='white')
        self.lbl_player_no.grid(row= 4, column= 0, sticky= W,padx= (5,5))
        pywinstyles.set_opacity(self.lbl_player_no, color='black')

        self.cmb_player_no = customtkinter.CTkComboBox(self, variable=self.no_players,values=list(str(i) for i in range(1,31)), width= 130,height=10,bg_color='black')
        self.cmb_player_no.grid(row= 4, column= 0, sticky= E,padx= (5,5))
        pywinstyles.set_opacity(self.cmb_player_no, color='black')

        self.lbl_coach_no = customtkinter.CTkLabel(self, text='No of coaches', font=("calibri", 16,'bold'),bg_color='black',text_color='white')
        self.lbl_coach_no.grid(row=4, column=2, sticky=W)
        pywinstyles.set_opacity(self.lbl_coach_no, color='black')
        self.cmb_coach_no = customtkinter.CTkComboBox(self, variable=self.no_coach,values=list(str(i) for i in range(1,4)), width= 130,height=10,bg_color='black')
        self.cmb_coach_no.grid(row=4, column=3, sticky=W,padx=(0,30))
        pywinstyles.set_opacity(self.cmb_coach_no, color='black')

        # self.lbl_empty = customtkinter.CTkLabel(self, text=" ",bg_color='black')
        # self.lbl_empty.grid(row=9, column=0,padx= (5,5))
        #pywinstyles.set_opacity(self.lbl_empty, color='black')

        self.lbl_age = customtkinter.CTkLabel(self, text= 'Age group', font=("calibri", 16,'bold'),bg_color='black',text_color='white')
        self.lbl_age.grid(row=5, column=0, sticky=W,padx= (5,5))
        pywinstyles.set_opacity(self.lbl_age, color='black')
        self.cmb_age = customtkinter.CTkComboBox(self, variable=self.age,values=['4-9','10-16','17-20','21-above'], width= 130,height=10,bg_color='black')
        #self.cmb_age['values'] = ['4-9','10-16','17-20','21-above']
        self.cmb_age.grid(row=5, column=0, sticky= E,padx= (5,5))

        self.lbl_level = customtkinter.CTkLabel(self, text= 'Level', font=("calibri", 16,'bold'),bg_color='black',text_color='white')
        self.lbl_level.grid(row=5, column=2, sticky=W)
        pywinstyles.set_opacity(self.lbl_level, color='black')
        self.cmb_level = customtkinter.CTkComboBox(self, variable=self.level,values=['District', 'State', 'National'], width= 130,height=10,bg_color='black')
        #self.cmb_level['values'] = ['District', 'State', 'National']
        self.cmb_level.grid(row=5, column=3, sticky= W,padx=(0,30))

        self.lbl_mail = customtkinter.CTkLabel(self, text='Mailing Address:', font=("calibri", 16,'bold'),bg_color='black',text_color='white')
        self.lbl_mail.grid(row=6, column=0, sticky=W,padx= (5,5))
        pywinstyles.set_opacity(self.lbl_mail, color='black')
        self.ent_mail = customtkinter.CTkEntry(self, width= 600,bg_color='black')
        self.ent_mail.grid(row=7, column=0, columnspan=4, sticky=W,padx= (5,5))
        pywinstyles.set_opacity(self.ent_mail, color='black')


        self.lbl_comment = customtkinter.CTkLabel(self, text='Additional comment(optional):', font=("calibri", 16,'bold'),bg_color='black',text_color='white')
        self.lbl_comment.grid(row=8, column=0, sticky= W,padx= (5,5))
        pywinstyles.set_opacity(self.lbl_comment, color='black')
        self.txt_comment = customtkinter.CTkTextbox(self, width=600,bg_color='black')
        self.txt_comment.grid(row=9, column=0, columnspan=4,sticky=W,padx= (5,5))
        pywinstyles.set_opacity(self.txt_comment, color='black')
        # self.lbl_empty = customtkinter.CTkLabel(self, text=" ",bg_color='black')
        # self.lbl_empty.grid(row=10, column=0,padx= (5,5))
        # pywinstyles.set_opacity(self.lbl_empty, color='black')
        self.btn_clear = customtkinter.CTkButton(self, text='CLEAR FORM', command=self.clear,fg_color='orange',bg_color='black',hover_color='dark orange')
        self.btn_clear.grid(row= 10, column= 0,columnspan=2,padx= (5,5))
        icon = customtkinter.CTkImage(Image.open('./images/submit_icon.JPG'))
        self.btn_submit = customtkinter.CTkButton(self, text='  SUBMIT',image=icon, command=self.process,
                                                  fg_color='orange', bg_color='black',hover_color='dark orange')
        self.btn_submit.grid(row=10, column=2, padx=(5, 5))
        icon = customtkinter.CTkImage(Image.open('./images/back_icon.JPG'),size=(30,30))
        self.btn_back = customtkinter.CTkButton(self, image=icon,text='', command=self.back, bg_color='black',fg_color='orange',hover_color='dark orange',width=8)
        self.btn_back.grid(row=0, column=0,sticky=W)

    def clear(self):
        self.ent_teamname.delete(0, END)
        self.country.set('')
        #self.rad_fball.select()
        self.cmb_player_no.set('')
        self.cmb_coach_no.set('')
        self.cmb_age.set('')
        self.cmb_level.set('')
        self.ent_mail.delete(0,END)
        self.txt_comment.delete(1.0,END)
    #this is how to create another frame in same window
    # def next_frame(self):
    #     registrar = self.cmb_registrar.get()
    #     if registrar == 'player':
    #         app= Player_app(self.master)
    #         app.grid(row=0, column=0,sticky= 'nsew')
    #         btn_back = customtkinter.CTkButton(app, text='BACK', command=self.back,bg_color='light blue')
    #         btn_back.grid(row=0, column=0, sticky=W)
    #         btn_submit = customtkinter.CTkButton(app, text='Submit', command=self.process,
    #                                                   bg_color='light blue')
    #         btn_submit.grid(row=26, column=0, sticky=W, padx=(5, 5))
    #         app.tkraise()
    #         # window.tkraise(app)
    #         # window.mainloop()
    #     elif registrar == 'coach':
    #         app = Coach_app(self.master)
    #         app.grid(row=0, column=0, sticky= 'nsew')
    #         btn_back = customtkinter.CTkButton(app, text='BACK', command=self.back,bg_color='light blue')
    #         btn_back.grid(row=0, column=0, sticky= W)
    #         self.btn_submit = customtkinter.CTkButton(app, text='Submit', command=self.process,
    #                                                   bg_color='light blue')
    #         self.btn_submit.grid(row=24, column=0, sticky=W, padx=(5, 5))
    #         app.tkraise()
    def back(self):
        self.grid_forget()
    def process(self):
        valid_data= []
        teamname = self.validation(self.ent_teamname.get())
        if teamname != False:
            valid_data.append(teamname)
        country = self.validation(self.country.get())
        if country != False:
            valid_data.append(country)
        # sport = self.validation(self.sport.get())
        # if sport != False:
        #     valid_data.append(sport)
        age_group = self.validation(self.age.get())
        if age_group != False:
            valid_data.append(age_group)
        no_players = self.validation(self.no_players.get())
        if no_players != False:
            valid_data.append(no_players)
        no_coaches = self.validation(self.no_coach.get())
        if no_coaches != False:
            valid_data.append(no_coaches)
        level = self.validation(self.level.get())
        if level != False:
            valid_data.append(level)
        mail = self.validation(self.ent_mail.get())
        if mail != False:
            valid_data.append(mail)
        add_comment = self.validation(self.txt_comment.get('1.0',END))
        if add_comment != False:
            valid_data.append(add_comment)
        if len(valid_data) >= 7:
            with sqlite3.connect('application.db') as con:
                cursor = con.cursor()

                table_query = '''CREATE TABLE IF NOT EXISTS
                                       TEAM (ID INTEGER primary key autoincrement,TeamName TEXT unique,Country INTEGER not null references country(ID), Age_group TEXT, Player_no INTEGER,Coach_no INTEGER,Level TEXT,Mail TEXT,
                                       Comment TEXT
                                       )'''

                con.execute(table_query)
                if len(valid_data) > 7:
                    cursor.execute('insert into TEAM(TeamName,Country,Age_group,Player_no,Coach_no,Level,Mail,Comment) values(?,?,?,?,?,?,?,?)',
                                   (teamname,country,age_group,no_players,no_coaches,level,mail,add_comment))
                elif len(valid_data) == 7:
                    cursor.execute('insert into TEAM(TeamName,Country,Age_group,Player_no,Coach_no,Level,Mail) values(?,?,?,?,?,?,?)'
                                   ,(teamname,country, age_group, no_players, no_coaches, level, mail))
                con.commit()
            CTkMessagebox(title='SUBMISSION SUCCESSFUL',
                            message='you have successfully registered for the International sports festival',
                            icon='check',
                            option_1='OK')
            self.clear()

        else:
            CTkMessagebox(title='SUBMISSION FAILED',message='some necessary fields are yet to be filled! ',
                          icon='warning',option_1='OK')

    def validation(self, data):
        if data:
            return data
        else:
            return False





# customtkinter.set_appearance_mode('light')
# customtkinter.set_default_color_theme('blue')
# window = customtkinter.CTk()
# window.title("MULTI-VENUE SPORTS REGISTRATION FORM")
# window.geometry("680x625")
#
# window.grid()
# #using iconphoto() to create icon
# icon = PhotoImage(file='C:/Users/HP/Downloads/sport_icon.PNG')
# window.iconphoto(False,icon)
# # if "__name__" == "main":
# app= Application(window)
# app.grid(row= 0, column =0, rowspan= 3, columnspan= 5, sticky= 'nsew')
# app.tkraise()
# # app.mainloop()
# window.mainloop()
