from tkinter import *
from tkinter import ttk
import customtkinter
from PIL import Image,ImageTk
import pywinstyles
from project.model import get_leader_board
class Board(customtkinter.CTkFrame):

    def __init__(self, master):
        super(Board, self).__init__(master)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid()
        self.canva = Canvas(self, bg='beige', height=525, width=630)
        self.canva.grid(row=0, column=0, rowspan=28, columnspan=4, sticky='nsew')

        self.img = customtkinter.CTkImage(Image.open('./images/images.JPEG'), size=(1500, 900))
        self.lbl_image = customtkinter.CTkLabel(self.canva, image=self.img,text=' ')
        self.lbl_image.grid(row=1, column=0,columnspan=4,sticky=N)
        self.icon= customtkinter.CTkImage(Image.open('./images/trophy.jpg').convert('RGBA'), size=(50, 50))
        self.canva.grid_rowconfigure(0, weight=1)
        self.canva.grid_columnconfigure(0, weight=1)

        self.create_widgets()

    def create_widgets(self):
        self.lbl_title = customtkinter.CTkLabel(self.canva,text_color='white',text='LEADER BOARD',bg_color='black',font=('calibri',20,'bold'))
        pywinstyles.set_opacity(self.lbl_title,color='black')
        self.lbl_title.grid(row=1,column=0,columnspan=3,sticky=N)

        self.lbl_icon = customtkinter.CTkLabel(self.canva, image=self.icon,text=' ',bg_color='orange')
        self.lbl_icon.grid(row=1,column=0,sticky=NW,padx=(350,0))
        self.lbl_icon2 = customtkinter.CTkLabel(self.canva, image=self.icon, text=' ', bg_color='orange')
        self.lbl_icon2.grid(row=1, column=0, sticky=NE, padx=(0, 350))

        style = ttk.Style()
        style.theme_use('default')
        # change treeview style
        style.configure('My.Treeview',
                        rowheight=70,
                        fieldbackground='beige',
                        foreground='black',
                        background='beige',font=('calibri','16'))
        style.configure('My.Treeview.Heading',background='brown',foreground='white',
                        relief='flat')
        # style.configure('My.Treeview.item',indicatorsize=20,padding=(50))
        # style.configure('My.Treeview.cell',background='blue')
        # change selected color
        style.map('My.Treeview', background=[('selected', 'brown')])
        # with Image.open('C:/Users/HP/Downloads/back_icon.JPG') as img:
        #     rank_image = ImageTk.PhotoImage(img)
        self.fix_tab_list = get_leader_board()
        self.tab_data = [('Rank', 'Team', 'Point'),
                         ]
        for record in self.fix_tab_list:
            self.tab_data.append(record)
        self.tab_columns = self.tab_data[0]
        self.table = ttk.Treeview(self, columns=self.tab_columns,style='My.Treeview')
        self.table.tag_configure('oddrow', background='beige')
        self.table.tag_configure('evenrow', background='orange')
        for i in self.tab_columns:
            self.table.heading(i, text=i)

            self.table.column(i, anchor='center',width=500)

        #medal = customtkinter.CTkImage(Image.open('C:/Users/HP/Downloads/medal.JPEG'), size=(50, 50))
        with Image.open('./images/medal2.jpg') as img:
            resize_img = img.resize((40,30))
            self.medal = ImageTk.PhotoImage(resize_img.convert('RGB'))
        count = 0
        for i in range(1, len(self.tab_data)):
            if count % 2 != 0:
                self.table.insert('', END, values=(i,self.tab_data[i][0],self.tab_data[i][1]), tags=('oddrow',))
            else:
                if i == 1:
                    self.table.insert('', END, values=(i, self.tab_data[i][0], self.tab_data[i][1]), tags=('evenrow',),image=self.medal)
                else:
                    self.table.insert('', END, values=(i,self.tab_data[i][0],self.tab_data[i][1]), tags=('evenrow',))
            count += 1
        self.table.image = self.medal
        self.table.grid(row=0, column=0, sticky=W, padx=(100, 0),columnspan=4)


        self.scroll = Scrollbar(self, command=self.table.yview,orient=VERTICAL,width=20)
        self.table.configure(yscrollcommand=self.scroll.set)
        self.table.grid_rowconfigure(0, weight=1)
        self.table.grid_columnconfigure(0, weight=1)
        self.scroll.grid(row=0,column=3,sticky=NS,padx=(0,0),rowspan=4)