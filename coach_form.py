# coach page
from tkinter import *
from tkinter import filedialog
import customtkinter
from project.model import get_country
from tkcalendar import DateEntry
import sqlite3
from CTkMessagebox import CTkMessagebox
from PIL import Image,ImageTk
import pywinstyles
class Coach_app(customtkinter.CTkScrollableFrame):

    def __init__(self, master):
        super(Coach_app, self).__init__(master,corner_radius=0,fg_color='transparent')
        self.gender = StringVar()
        self.level = StringVar()
        self.country = StringVar()
        #self.grid_rowconfigure(0, weight=1)
        #self.grid_columnconfigure(0, weight=1)

        self.grid()
        self.canva = Canvas(self, bg='light blue',height=625, width=630)
        #canva.configure(bg='light blue')
        self.canva.grid(row=0, column=0, rowspan=28, columnspan= 4,sticky= 'nsew')
        self.img = customtkinter.CTkImage(Image.open('./images/playerbg.JPG'), size=(1500, 900))
        # tkimage=self.img.create_scaled_photo_image(1,'dark')
        # self.canva.create_image(40,10,anchor='nw',image=tkimage)
        self.lbl_image = customtkinter.CTkLabel(self.canva, image=self.img)
        self.lbl_image.grid(row=0, column=0, sticky='nsew')
        self.canva.grid_rowconfigure(0, weight=1)
        self.canva.grid_columnconfigure(0, weight=1)
        self.create_widgets()

    def create_widgets(self):
        self.lbl_title = customtkinter.CTkLabel(self, text="Coach's Registration Form",
                                                font=("", 20, 'bold'), bg_color='black', text_color='white')
        self.lbl_title.grid(row=0, column=0, columnspan=3, pady=(20, 0))
        #pywinstyles.set_opacity(self.lbl_title, color="black")
        # self.btn_back = Button(self, text= 'Back',command=self.back)
        # self.btn_back.grid(row=0, column=0, sticky=W)

        # self.lbl_empty = Label(self, text="", bg='black')
        # self.lbl_empty.grid(row=1, column=0,padx= (5,5))

        # Name
        self.lbl_name = customtkinter.CTkLabel(self, text='Name: ', font=("calibri", 19), bg_color='black',
                                               text_color='white')
        self.lbl_name.grid(row=1, column=0, sticky=W, padx=(5, 5))
        #pywinstyles.set_opacity(self.lbl_name, color="blue")
        # self.canva.create_text(80, 50, fill="white", font="calibri 19",
        #                         text="Name:")
        self.ent_name = customtkinter.CTkEntry(self, width=230, bg_color='black', placeholder_text='First')
        self.ent_name.grid(row=2, column=0, columnspan=2, sticky=W, padx=(5, 5))

        self.ent_lname = customtkinter.CTkEntry(self, width=230, bg_color='black', placeholder_text='Last')
        self.ent_lname.grid(row=2, column=2, sticky=W, padx=(5, 5))

        # DOB
        self.lbl_dob = customtkinter.CTkLabel(self, text='D.O.B:', font=("calibri", 19), bg_color='black',
                                              text_color='white')
        self.lbl_dob.grid(row=3, column=0, sticky=W, padx=(5, 5))
        #pywinstyles.set_opacity(self.lbl_dob, color="black")
        self.ent_dob = customtkinter.CTkEntry(self, width=230, bg_color='black', placeholder_text='YYYY-MM-DD')
        self.ent_dob.grid(row=4, column=0, sticky=NW, padx=(5, 5))

        # style = ttk.Style(self)
        # style.theme_use("default")
        # self.date_dob = Calendar(self, selectmode='day', locale='en_US', disabledforeground='red',
        #        cursor="hand2", background=customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"][1],
        #        selectbackground=customtkinter.ThemeManager.theme["CTkButton"]["fg_color"][1],date_pattern='y-mm-dd')
        # self.date_dob.grid(row=4, column=2, sticky=W,padx= (5,5))
        # date = self.date_dob.cget('selectmod')
        # self.ent_dob.delete(0)
        # self.ent_dob.insert(1,string=date)

        # Email
        self.lbl_email = customtkinter.CTkLabel(self, text='Email:', font=("calibri", 19), bg_color='black',
                                                text_color='white')
        self.lbl_email.grid(row=5, column=0, sticky=W, padx=(5, 5))
        #pywinstyles.set_opacity(self.lbl_email, color="black")
        self.ent_email = customtkinter.CTkEntry(self, width=400, bg_color='black',
                                                placeholder_text='example26@gmail.com')
        self.ent_email.grid(row=6, column=0, columnspan=2, sticky=W, padx=(5, 5))

        # Phone
        self.lbl_phone = customtkinter.CTkLabel(self, text='Phone:', font=("calibri", 19), bg_color='black',
                                                text_color='white')
        self.lbl_phone.grid(row=7, column=0, sticky=W, padx=(5, 5))
        #pywinstyles.set_opacity(self.lbl_phone, color="black")
        self.ent_phone = customtkinter.CTkEntry(self, width=400, bg_color='black')
        self.ent_phone.grid(row=8, column=0, columnspan=2, sticky=W, padx=(5, 5))

        # Address
        self.lbl_address = customtkinter.CTkLabel(self, text='Address:', font=("calibri", 19), bg_color='black',
                                                  text_color='white')
        self.lbl_address.grid(row=9, column=0, sticky=W, padx=(5, 5))
        #pywinstyles.set_opacity(self.lbl_address, color="black")
        self.ent_address = customtkinter.CTkEntry(self, width=600, bg_color='black')
        self.ent_address.grid(row=10, column=0, columnspan=3, sticky=W, padx=(5, 5))

        # City
        self.lbl_city = customtkinter.CTkLabel(self, text='City:', font=("calibri", 19), bg_color='black',
                                               text_color='white')
        self.lbl_city.grid(row=11, column=0, sticky=W, padx=(5, 5))
        #pywinstyles.set_opacity(self.lbl_city, color="black")
        self.lbl_region = customtkinter.CTkLabel(self, text='Region:', font=("calibri", 19), bg_color='black',
                                                 text_color='white')
        self.lbl_region.grid(row=11, column=2, sticky=W, padx=(5, 5))
        #pywinstyles.set_opacity(self.lbl_region, color="black")
        self.ent_city = customtkinter.CTkEntry(self, width=230, bg_color='black')
        self.ent_city.grid(row=12, column=0, columnspan=2, sticky=W, padx=(5, 5))
        self.ent_region = customtkinter.CTkEntry(self, width=230, bg_color='black')
        self.ent_region.grid(row=12, column=2, columnspan=2, sticky=W, padx=(5, 5))

        # postal
        self.lbl_postal = customtkinter.CTkLabel(self, text='Postal/Zip code', font=("calibri", 19), bg_color='black',
                                                 text_color='white')
        self.lbl_postal.grid(row=13, column=0, columnspan=2, sticky=W, padx=(5, 5))
        #pywinstyles.set_opacity(self.lbl_postal, color="black")
        self.ent_postal = customtkinter.CTkEntry(self, width=230, bg_color='black')
        self.ent_postal.grid(row=14, column=0, columnspan=2, sticky=W, padx=(5, 5))

        # country
        self.lbl_country = customtkinter.CTkLabel(self, text='Country', font=("calibri", 19), bg_color='black',
                                                  text_color='white')
        self.lbl_country.grid(row=13, column=2, sticky=W, padx=(5, 5))
        #pywinstyles.set_opacity(self.lbl_country, color="black")
        self.dwd_country = customtkinter.CTkComboBox(self, variable=self.country, width=230,
                                                     values= get_country(), bg_color='black')
        # self.dwd_country['values'] = ['Nigeria', 'Ghana', 'Niger.', 'South Africa.', 'Cyprus', 'Uk', 'USA']
        self.dwd_country.grid(row=14, column=2, columnspan=2, sticky=W, padx=(5, 5))

        # self.country_dropdown =ttk.Combobox(self, textvariable=self.country)
        # self.country_dropdown.pack()
        # self.countries = [country.name for country in pycountry.countries]
        # self.countries.sort()
        # self.country_dropdown['values'] = countries
        # self.country_dropdown.grid(row= 14, column= 3, sticky= W)

        # Gender
        self.lbl_gender = customtkinter.CTkLabel(self, text='Gender:', font=("calibri", 19), bg_color='black',
                                                 text_color='white')
        self.lbl_gender.grid(row=15, column=0, sticky=W, padx=(5, 5))
        #pywinstyles.set_opacity(self.lbl_gender, color="black")
        self.rad_male = customtkinter.CTkRadioButton(self, text='Male', variable=self.gender, value='Male',
                                                     text_color='white', font=('', 12), bg_color='black')
        self.rad_male.grid(row=16, column=0, sticky=W, padx=(5, 5))
        #pywinstyles.set_opacity(self.rad_male, color="black")
        self.rad_female = customtkinter.CTkRadioButton(self, text='Female', variable=self.gender, value='Female',
                                                       text_color='white', font=('', 12), bg_color='black')
        self.rad_female.grid(row=16, column=1, sticky=W, padx=(5, 5))
        #pywinstyles.set_opacity(self.rad_female, color="black")
        self.rad_male.select()

        # hight and
        self.lbl_height = customtkinter.CTkLabel(self, text='Height(ft):', font=("calibri", 19), bg_color='black',
                                                 text_color='white')
        self.lbl_height.grid(row=18, column=0, sticky=W, padx=(5, 5))
        #pywinstyles.set_opacity(self.lbl_height, color="black")
        self.ent_height = customtkinter.CTkEntry(self, width=230, bg_color='black')
        self.ent_height.grid(row=19, column=0, columnspan=2, sticky=W, padx=(5, 5))

        # weight
        self.lbl_weight = customtkinter.CTkLabel(self, text='Weight(ibs):', font=("calibri", 19), bg_color='black',
                                                 text_color='white')
        self.lbl_weight.grid(row=18, column=2, sticky=W, padx=(5, 5))
        #pywinstyles.set_opacity(self.lbl_weight, color="black")
        self.ent_weight = customtkinter.CTkEntry(self, width=230, bg_color='black')
        self.ent_weight.grid(row=19, column=2, columnspan=2, sticky=W, padx=(5, 5))

        # fitness a
        self.lbl_fitcert = customtkinter.CTkLabel(self, text='Physical fitness cert.:', font=("calibri", 19),
                                                  bg_color='black', text_color='white')
        self.lbl_fitcert.grid(row=20, column=0, columnspan=2, sticky=W, padx=(5, 5))
        #pywinstyles.set_opacity(self.lbl_fitcert, color="black")

        self.ent_fitcert = customtkinter.CTkEntry(self, width=230, bg_color='black', placeholder_text='Attachment')
        self.ent_fitcert.grid(row=21, column=0, sticky=W, padx=(5, 5))
        self.btn_cert_img = customtkinter.CTkButton(self, text='Browse...', command=self.ft_cert_upload,
                                                    bg_color='black', fg_color='orange',hover_color='dark orange')
        self.btn_cert_img.grid(row=22, column=0, sticky=W, padx=(5, 5))

        # medicals
        # self.lbl_med = Label(self, text='Medical condition if any:', font=("", '16'),bg='light blue')
        # self.lbl_med.grid(row=20, column=2, columnspan=2, sticky=W,padx= (5,5))
        #
        # self.ent_medcert = customtkinter.CTkEntry(self, width= 230,bg_color='light blue',placeholder_text='Attachment')
        # self.ent_medcert.grid(row=21, column=2, sticky=W,padx= (5,5))
        # self.btn_medcert_img = customtkinter.CTkButton(self, text='Browse...', command=self.med_cert_upload,bg_color='light blue')
        # self.btn_medcert_img.grid(row=22, column=2, sticky=W,padx= (5,5))

        # Position and shirt info
        # self.lbl_position = Label(self, text='Position:', font=("", '16'),bg='light blue')
        # self.lbl_position.grid(row=23, column=0, sticky=W,padx= (5,5))
        # self.ent_position = customtkinter.CTkEntry(self, width= 230,bg_color='light blue')
        # self.ent_position.grid(row=24, column=0, sticky=W,padx= (5,5))
        # self.lbl_shirtno = Label(self, text='Shirt No:', font=("", '16'),bg='light blue')
        # self.lbl_shirtno.grid(row=23, column=2, sticky=W,padx= (5,5))
        # self.ent_shirtno = customtkinter.CTkEntry(self, width= 230,bg_color='light blue')
        # self.ent_shirtno.grid(row=24, column=2, sticky=W,padx= (5,5))

        # Additional space
        self.lbl_position = customtkinter.CTkLabel(self, text='', font=("calibri", 19), bg_color='black',
                                                   text_color='white')
        self.lbl_position.grid(row=25, column=0, columnspan=2, sticky=W, padx=(5, 5))
        #pywinstyles.set_opacity(self.lbl_position, color="black")

        # clear and submit bottens
        self.btn_reset = customtkinter.CTkButton(self, text='CLEAR FORM', command=self.reset, bg_color='black',
                                                 fg_color='orange',hover_color='dark orange')
        self.btn_reset.grid(row=26, column=2, sticky=W, padx=(5, 5))
        icon = customtkinter.CTkImage(Image.open('./images/submit_icon.JPG'))
        btn_submit = customtkinter.CTkButton(self, text='  SUBMIT',image=icon, command=self.process,
                                             bg_color='black', fg_color='orange',hover_color='dark orange')
        btn_submit.grid(row=26, column=0, sticky=W, padx=(5, 5))
        icon = customtkinter.CTkImage(Image.open('./images/back_icon.JPG'), size=(30, 30))
        self.btn_back = customtkinter.CTkButton(self, image=icon, text='', command=self.back, bg_color='black',
                                                fg_color='orange', hover_color='dark orange', width=8)
        self.btn_back.grid(row=0, column=0, sticky=NW)

    # def med_cert_upload(self):
    #         filetype = (
    #             ('JPG Files', '*.jpg'),
    #             ('PNG Files', '*.png'),
    #             ('JPEG Files', '*.jpeg')
    #         )
    #         filepath = filedialog.askopenfile(filetypes=filetype)
    #
    #         self.ent_medcert.delete(0, END)
    #         self.ent_medcert.insert(0, str(filepath.name))

    def ft_cert_upload(self):
            filetype = (
                ('JPG Files', '*.jpg'),
                ('PNG Files', '*.png'),
                ('JPEG Files', '*.jpeg')
            )
            filepath = filedialog.askopenfile(filetypes=filetype)
            self.ent_fitcert.delete(0, END)
            self.ent_fitcert.insert(0, str(filepath.name))

    def reset(self):
        self.ent_name.delete(0, END)
        self.ent_lname.delete(0, END)
        self.ent_dob.delete(0, END)
        self.ent_email.delete(0, END)
        self.ent_phone.delete(0, END)
        self.ent_address.delete(0, END)
        self.ent_city.delete(0, END)
        self.ent_region.delete(0, END)
        self.ent_postal.delete(0, END)
        self.dwd_country.set('')
        self.rad_male.select()
        self.ent_height.delete(0, END)
        self.ent_weight.delete(0, END)
        self.ent_fitcert.delete(0, END)
        #self.ent_medcert.delete(0, END)
    def process(self):
        valid_data = []
        firstname = self.validation(self.ent_name.get())
        if firstname != False:
            valid_data.append(firstname)

        lastname = self.validation(self.ent_lname.get())
        if lastname != False:
            valid_data.append(lastname)

        dob = self.validation(self.ent_dob.get())
        if dob != False:
            valid_data.append(dob)

        email = self.validation(self.ent_email.get())
        if email != False:
            valid_data.append(email)

        phone = self.validation(self.ent_phone.get())
        if phone != False:
            valid_data.append(phone)

        address = self.validation(self.ent_address.get())
        if address != False:
            valid_data.append(address)

        city = self.validation(self.ent_city.get())
        if city != False:
            valid_data.append(city)

        region = self.validation(self.ent_region.get())
        if region != False:
            valid_data.append(region)

        postal_zip = self.validation(self.ent_postal.get())
        if postal_zip != False:
            valid_data.append(postal_zip)

        country = self.validation(self.country.get())
        if country != False:
            valid_data.append(country)

        gender = self.validation(self.gender.get())
        if gender != False:
            valid_data.append(gender)

        height = self.validation(self.ent_height.get())
        if height != False:
            valid_data.append(height)

        weight = self.validation(self.ent_weight.get())
        if weight != False:
            valid_data.append(weight)

        fitcert = self.validation(self.ent_fitcert.get())
        if fitcert != False:
            valid_data.append(fitcert)

        if len(valid_data) == 14:
            with sqlite3.connect('application.db') as con:
                cursor = con.cursor()

                table_query = '''CREATE TABLE IF NOT EXISTS
                                       COACH (ID INTEGER primary key autoincrement,FirstName TEXT, LastName TEXT, DateOfBirth NUMERIC, Email INTEGER,Phone TEXT,Address TEXT,City BLOB,
                                       Region TEXT,PostalCode INTEGER,Country INTEGER not null references country(ID),Gender TEXT,Height NUMERIC,Weight NUMERIC,
                                       MedicalCertificate  BLOB
                                       )'''

                con.execute(table_query)

                cursor.execute('''insert into COACH (FirstName,LastName,DateOfBirth,Email,Phone,Address,
                                       City,Region,PostalCode,Country,Gender,Height,Weight,MedicalCertificate) Values(?,?,?,?,?,?,?,?,?,?,?,?,
                                       ?,?)
                                                         ''', (firstname, lastname, dob, email, phone, address,
                                                               city, region, postal_zip, country,
                                                               gender, height, weight, fitcert))
                con.commit()
            self.success()
            self.reset()

        else:
            self.error()

    def validation(self, data):
        if data:
            return data
        else:
            return False

    def error(self):
        CTkMessagebox(title='SUBMISSION FAILED',message='some necessary fields are yet to be filled!',icon='warning',option_1='OK')
    def success(self):
        CTkMessagebox(title='SUBMISSION SUCCESSFUL', message='you have successfully registered for the International sports festival',
                      icon='check',
                      option_1='OK')


    def back(self):
        self.grid_forget()