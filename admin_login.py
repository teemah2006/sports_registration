#admin login page
from tkinter import *
from tkinter import ttk
import customtkinter
from PIL import Image
import pywinstyles
from CTkMessagebox import CTkMessagebox
import sqlite3
from project.model import get_fixtures,update_fix_table,add_to_leader_board,add_point
import random
from tkcalendar import *
class Admin(customtkinter.CTkFrame):
    def __init__(self,master):
        super(Admin,self).__init__(master=master)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.canva = customtkinter.CTkCanvas(self, height=525, width=630, background='white')
        # canva.configure(bg= 'light blue')
        self.canva.grid(row=0, column=0, rowspan=33, columnspan=4, sticky='nsew')
        self.bg_image = customtkinter.CTkImage(Image.open('./images/adminbg.JPG'),size=(900,700))
        self.lbl_image = customtkinter.CTkLabel(self.canva,image=self.bg_image,text=' ')
        self.lbl_image.grid(row=0,column=0,sticky = 'w')
        self.logo_image = customtkinter.CTkImage(Image.open('./images/adminlogo.JPG'), size=(70, 70))
        self.lbl_logo = customtkinter.CTkLabel(self.canva, image=self.logo_image, text=' ',compound='top')
        self.lbl_logo.grid(row=0, column=1,columnspan=2,padx=(0,80),pady=(0,300))
        self.canva.grid_rowconfigure(0, weight=1)
        self.canva.grid_columnconfigure(0, weight=1)

        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.username_ent = customtkinter.CTkEntry(self.canva,placeholder_text='Username',width=230,height=37,bg_color='white')
        self.username_ent.grid(row=0,column=1,padx=(0,80),pady=(0,80))

        self.password_ent = customtkinter.CTkEntry(self.canva, placeholder_text='Password', width=230,height=37, bg_color='white',show="*")
        self.password_ent.grid(row=0, column=1, padx=(0, 80), pady=(100, 0))

        self.login_btn = customtkinter.CTkButton(self.canva,text_color='white',text='LOGIN'
                                                 ,bg_color='white',fg_color='orange',hover_color='dark orange',command=self.process)
        self.login_btn.grid(row=0, column=1, padx=(0, 80), pady=(250, 0))

    def process(self):
        if self.username_ent.get() and self.password_ent.get():
            with sqlite3.connect('application.db') as conn:
                cursor = conn.cursor()
                rs = cursor.execute("SELECT username,password from admin")
                rs_list = list(rs.fetchall())

                if self.username_ent.get() == rs_list[0][0]:
                    if self.password_ent.get() == rs_list[0][1]:
                        CTkMessagebox(title='SUCCESS', message='Login successful!', icon='check', option_1='OK',
                                      button_color='orange', button_hover_color='dark orange')
                        self.admin_page()
                    else:
                        self.lbl_error = customtkinter.CTkLabel(self.canva,text_color='red',text='Invalid Username or Password',bg_color='white')
                        self.lbl_error.grid(row=0, column=1, padx=(0, 80), pady=(180, 0))
                else:
                    self.lbl_error = customtkinter.CTkLabel(self.canva, text_color='red',
                                                            text='Invalid Username or Password', bg_color='white')
                    self.lbl_error.grid(row=0, column=1, padx=(0, 80), pady=(180, 0))
        else:
            CTkMessagebox(title='ERROR',message='Enter complete data!',icon='cancel',option_1='OK',button_color='orange',button_hover_color='dark orange')

    def admin_page(self):
        self.tabview = customtkinter.CTkTabview(self.master, segmented_button_unselected_hover_color='dark orange',
                                           segmented_button_selected_color='orange',
                                           segmented_button_selected_hover_color='dark orange',fg_color='white')
        self.tabview.grid(row=0, column=0, sticky='nsew')
        self.tabview.grid()
        self.tabview.add('CREATE FIXTURE')
        self.tabview.add('INPUT SCORES')



        self.lbl_fixture = customtkinter.CTkLabel(self.tabview.tab('CREATE FIXTURE'),text='Enter team names: '
                                                  ,text_color='black',bg_color='white',font=("calibri",16,"bold"))
        self.lbl_fixture.grid(row=0,column=0,padx=(10,0))
        self.txt_names = customtkinter.CTkTextbox(self.tabview.tab('CREATE FIXTURE'),width=300,height=400,bg_color='white',fg_color='beige')
        self.txt_names.grid(row=1,column=0,padx=(10,0))
        self.lbl_fixture = customtkinter.CTkLabel(self.tabview.tab('CREATE FIXTURE'), text='Generated fixtures: '
                                                  , text_color='black', bg_color='white', font=("calibri", 16, "bold"))
        self.lbl_fixture.grid(row=0, column=1, padx=(30, 0))
        self.btn_create = customtkinter.CTkButton(self.tabview.tab('CREATE FIXTURE'),text_color='black',text='GENERATE'
                                                  ,bg_color='white',fg_color='orange',hover_color='dark orange',compound='right'
                                                  ,command=self.generate_fixture)
        self.btn_create.grid(row=2,column=1,padx=(0,80))
        self.txt_fixtures = customtkinter.CTkTextbox(self.tabview.tab('CREATE FIXTURE'),width=400,height=400,bg_color='white',fg_color='beige',font=("",15,"bold"))
        self.txt_fixtures.grid(row=1,column=1,padx=(30,10),sticky=E)

        self.lbl_date = customtkinter.CTkLabel(self.tabview.tab('CREATE FIXTURE'), text='Fix Date: '
                                                  , text_color='black', bg_color='white', font=("calibri", 16, "bold"))
        self.lbl_date.grid(row=0,column=3,sticky=W)
        self.fix_no = customtkinter.CTkTextbox(self.tabview.tab('CREATE FIXTURE'),width=40,height=40,bg_color='white',fg_color='beige',font=("",15,"bold"))
        self.fix_no.grid(row=0,column=4,sticky=W)
        self.fixno_btn = customtkinter.CTkButton(self.tabview.tab('CREATE FIXTURE'),text_color='black',text='OK'
                                                  ,bg_color='white',fg_color='orange',hover_color='dark orange',compound='right'
                                                  ,command=self.generate_date,width=30)
        self.fixno_btn.grid(row=1,column=5,pady=(0,380),sticky=E)
        self.btn_done = customtkinter.CTkButton(self.tabview.tab('CREATE FIXTURE'),text_color='black',text='Done'
                                                  ,bg_color='white',fg_color='orange',hover_color='dark orange',compound='right'
                                                  ,command=self.submit)
        self.btn_done.grid(row=3,column=5,pady=(10,0))

        style = ttk.Style()
        style.theme_use('default')
        #change treeview style
        style.configure('Treeview',
                        rowheight= 50,
                        fieldbackground='beige',
                        foreground='black',
                        background='beige',
                        font=('calibri','17'))
        #change selected color
        style.map('Treeview',background=[('selected','brown')])

        self. lbl_heading = customtkinter.CTkLabel(self.tabview.tab('INPUT SCORES'), text='Match Score Table '
                                                  , text_color='black', bg_color='white', font=("calibri", 19, "bold"))
        self.lbl_heading.grid(row=0,column=0,columnspan=3)
        self.fix_tab_list = get_fixtures()
        self.tab_data = [('No','Team1','Score1','Team2','Score2'),
                         ]
        for record in self.fix_tab_list:
            self.tab_data.append(record)
        self.tab_columns = self.tab_data[0]
        self.table = ttk.Treeview(self.tabview.tab('INPUT SCORES'),columns=self.tab_columns,show='headings')
        self.table.tag_configure('oddrow',background='beige')
        self.table.tag_configure('evenrow', background='orange')
        for i in self.tab_columns:
            self.table.heading(i,text=i)

            if i in ['Team1','Team2']:
                self.table.column(i,anchor='center',width=500)
            else:
                self.table.column(i, anchor='center')

        count = 0
        for i in range(1,len(self.tab_data)):
            if count%2 != 0:
                self.table.insert('',END,values=self.tab_data[i],tags=('oddrow',))
            else:
                self.table.insert('', END, values=self.tab_data[i], tags=('evenrow',))
            count+=1

        self.table.grid(row=1,column=0,sticky=W,padx=(10,0),rowspan=3,columnspan=3)
        self.table.bind("<Double-1>",self.double_clicked)

        self.scroll = Scrollbar(self.tabview.tab('INPUT SCORES'),command=self.table.yview,orient=VERTICAL)
        self.table.configure(yscrollcommand = self.scroll.set)
        self.table.grid_rowconfigure(0,weight=1)
        self.table.grid_columnconfigure(0, weight=1)
        self.scroll.grid(row=1,column=4,sticky=NS,padx=(0,0),rowspan=3)

        self.lbl_empty = customtkinter.CTkLabel(self.tabview.tab('INPUT SCORES'),
                                                     text=' '
                                                     , text_color='black', bg_color='white',
                                                     font=("calibri", 16, "bold"))
        self.lbl_empty.grid(row=4, column=0, columnspan=2, sticky=W)

        self.lbl_multiplier = customtkinter.CTkLabel(self.tabview.tab('INPUT SCORES'), text='Enter point multiplier value: '
                                                  , text_color='black', bg_color='white', font=("calibri", 16, "bold"))
        self.lbl_multiplier.grid(row=5,column=0,columnspan=2,sticky=W)

        self.ent_multiplier = customtkinter.CTkEntry(self.tabview.tab('INPUT SCORES'),width=50,bg_color='white')
        self.ent_multiplier.grid(row=5,column=1,sticky=W)

        self.btn_done2 = customtkinter.CTkButton(self.tabview.tab('INPUT SCORES'), text_color='black', text='Done'
                                                , bg_color='white', fg_color='orange', hover_color='dark orange',
                                                compound='right'
                                                , command=self.get_table_updated)
        self.btn_done2.grid(row=6, column=1, pady=(10, 0))




    def generate_fixture(self):
        if self.txt_names.get('1.0',END):
            teams = self.txt_names.get('1.0',END).split('\n')
            teams.pop(-1)
            random.shuffle(teams)  # Shuffle the team list
            fixtures = []

            for i in range(0, len(teams), 2):
                try:
                    fixtures.append(f'{teams[i]} vs {teams[i + 1]}')
                except IndexError:
                    fixtures.append(f'{teams[i]} has a bye')
            self.txt_fixtures.delete('0.0',END)
            for fixture in fixtures:
                self.txt_fixtures.insert('0.0',f'{fixture}\n')
    def generate_date(self):
        fix_no = int(self.fix_no.get('1.0', END))
        self.ent_fix = {}
        self.btn_fix = list(range(fix_no))
        var = list(range(fix_no))
        i = 0

        pady = 370
        if self.fix_no.get('1.0', END):
            for row in range(fix_no):

                pady -= 70
                self.ent_fix[row] = customtkinter.CTkEntry(self.tabview.tab('CREATE FIXTURE')
                                               , bg_color='white',
                                               width=200
                                               )
                self.ent_fix[row].grid(row=1, column=5, pady=(0, pady))
                print(f'{row} before button')
                var[i] = row
                self.btn_fix[row] = customtkinter.CTkButton(self.tabview.tab('CREATE FIXTURE'), text_color='black',
                                                        text=f'set date for fixture {row+1}'
                                                        , bg_color='white', fg_color='orange',
                                                        hover_color='dark orange',
                                                        compound='right',command=lambda:self.date_picker(fix_no,self.btn_fix[row].grid_info()['pady'])
                                                        )
                if pady < 0:
                    self.btn_fix[row].grid(row=2, column=3, pady=(0, 150))
                else:
                    self.btn_fix[row].grid(row=1, column=3, pady=(0, pady))
                i += 1
                print(f'{row} after button')


    def date_picker(self,row,pad):
        window = customtkinter.CTk()
        window.title("DATE")
        window.geometry("400x300")
        self.cal = Calendar(window,selectmode='day',year=2024,month=3)
        self.cal.pack(pady=20)
        self.btn_getdate = customtkinter.CTkButton(window,text='OKAY',text_color='black', fg_color='orange',
                                                        hover_color='dark orange',command=lambda:self.grab_date(row,pad))
        self.btn_getdate.pack(pady=20)
        window.mainloop()

    def grab_date(self,fix_no,pad):
        # fix_no = int(self.fix_no.get('1.0', END))
        for row in range(fix_no):
            if self.ent_fix[row].grid_info()['pady'] == pad:
                print(f'{row} passed to grab_date')
                self.ent_fix[row].delete(0,END)
                self.ent_fix[row].insert(0,self.cal.get_date())
    def submit(self):
        if self.txt_fixtures.get('1.0',END):
            stat = False
            for ent in range(int(self.fix_no.get('1.0', END))):
                if self.ent_fix[ent].get():
                    stat = True
            if stat:
                fixture = self.txt_fixtures.get('1.0',END).split('\n')
                fixture.pop(-1)
                fixture.pop(-1)
                print(fixture)
                for i in range(len(fixture)):
                    com = fixture[i].split('vs')
                    print(com)
                    team1 = com[0]
                    team2 = com[1]
                    date = self.ent_fix[i].get()
                    point = 0

                    with sqlite3.connect('application.db') as con:
                        cursor = con.cursor()

                        table_query = '''CREATE TABLE IF NOT EXISTS
                                               FIXTURES (ID INTEGER primary key autoincrement,Date BLOB, Team1 TEXT, Score1 NUMERIC, Team2 TEXT,Score2 NUMERIC
                                               )'''

                        con.execute(table_query)

                        cursor.execute('''insert into FIXTURES (Date,Team1,Score1,Team2,Score2) Values(?,?,?,?,?)
                                                                 ''', (date,team1,'',team2,''))
                        con.commit()
                    for x in com:
                        add_to_leader_board(x,point)
                self.clear()
            else:
                CTkMessagebox(title='ERROR', message='Enter complete data!', icon='cancel', option_1='OK',
                              button_color='orange', button_hover_color='dark orange')
        else:
            CTkMessagebox(title='ERROR', message='Enter complete data!', icon='cancel', option_1='OK',
                          button_color='orange', button_hover_color='dark orange')
    def clear(self):
        self.txt_names.delete('0.0',END)
        self.txt_fixtures.delete('0.0',END)
        for ent in range(int(self.fix_no.get('1.0', END))):
            self.ent_fix[ent].delete(0,END)

    def double_clicked(self,event):
        #identify the region that was double clicked
        region_clicked = self.table.identify_region(event.x,event.y)
        if region_clicked != "cell":
            return

        #which item was double clicked?
        #e.g: #1,#2
        column = self.table.identify_column(event.x)
        #get the column index in the values list by
        col_index = int(column[1:]) - 1
        # column #1 will become 0 , column #3 will become 2

        #this will get the id of the selected row e.g: 001,002
        selected_id = self.table.focus()
        # this will get a dictionary information of the row selected
        selected_values = self.table.item(selected_id)

        if column == '#3' or column == '#5':

            selected_item = selected_values.get('values')[col_index]

            #so now to get the exact size of the selected cell, we use bbox method which accepts the item id and column
            column_box = self.table.bbox(selected_id,column)
            print(column_box)
            #it will return x coordinate,y coordinate, width and height as a tuple
            ent_edit = Entry(self.table)
            #recording the selected id an column index
            ent_edit.ed_column_index = col_index
            ent_edit.ed_item_id = selected_id

            #to not make the original item in that cell disapear when you double click
            ent_edit.insert(0,selected_item)
            ent_edit.select_range(0,END)

            ent_edit.focus()

            ent_edit.bind('<FocusOut>',self.focus_out)
            ent_edit.bind('<Return>',self.enter_pressed)
            ent_edit.place(x=column_box[0],y=column_box[1],h=column_box[3],w=column_box[2])
    def focus_out(self,event):
        #the event passed is the widget that's been focused out
        #so we destroy the widget so the entry won't show once you click out of the cell.
        event.widget.destroy()

    def enter_pressed(self,event):
        new_text = event.widget.get()

        #such as I001
        selected_id = event.widget.ed_item_id
        print(selected_id)

        #such as 1,2
        column_index = event.widget.ed_column_index

        current_values = self.table.item(selected_id).get('values')
        current_values[column_index] = new_text
        self.table.item(selected_id,values=current_values)
        print(current_values)
        event.widget.destroy()

    def get_table_updated(self):
        rows = self.fix_tab_list
        for i in range(len(rows)):
            i = i+1
            x = f'I00{str(i)}'
            values = self.table.item(x).get('values')
            ID = values[0]
            score1 = values[2]
            score2 = values[4]
            update_fix_table(ID,score1,score2)

            #also update the leader board
            if score2 != '' and score1 != '' :
                if self.ent_multiplier.get():
                    team1 = values[1]
                    team2 = values[3]
                    point1 = score1 * eval(self.ent_multiplier.get())
                    point2 = score2 * eval(self.ent_multiplier.get())

                    add_point(point2,team2)
                    add_point(point1,team1)
                else:
                    CTkMessagebox(title='ERROR', message='Enter complete data!', icon='cancel', option_1='OK',
                                  button_color='orange', button_hover_color='dark orange')



