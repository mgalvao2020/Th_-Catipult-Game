import arcade
import csv
from tkinter import *
import sqlite3


root = Tk()
root.title("BYUI - CSE 310 team 4")
width = 400
height = 280
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

#==============================VARIABLES======================================
USERNAME = StringVar()
PASSWORD = StringVar()
 
#==============================FRAMES=========================================
Top = Frame(root, bd=2,  relief=RIDGE)
Top.pack(side=TOP, fill=X)
Form = Frame(root, height=200)
Form.pack(side=TOP, pady=20)
 
#==============================LABELS=========================================
lbl_title = Label(Top, text = "CATIPULT GAME", font=('arial', 35))
lbl_title.pack(fill=X)
lbl_username = Label(Form, text = "Username:", font=('arial', 14), bd=15)
lbl_username.grid(row=0, sticky="e")
lbl_password = Label(Form, text = "Password:", font=('arial', 14), bd=15)
lbl_password.grid(row=1, sticky="e")
lbl_text = Label(Form)
lbl_text.grid(row=2, columnspan=2)
 
#==============================ENTRY WIDGETS==================================
username = Entry(Form, textvariable=USERNAME, font=(14))
username.grid(row=0, column=1)
password = Entry(Form, textvariable=PASSWORD, show="*", font=(14))
password.grid(row=1, column=1)
 
#==============================BUTTON WIDGETS=================================
Login = 1
btn_login = Button(Form, text="Login", width=45, command=Login)
btn_login.grid(pady=25, row=3, columnspan=2)
btn_login.bind('<Return>', Login)

#==============================METHODS========================================
def Database():
    global conn, cursor
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("")       
    cursor.execute("")
    if cursor.fetchone() is None:
        cursor.execute("")
        conn.commit()

def Login(event=None):
    Database()
    if USERNAME.get() == "" or PASSWORD.get() == "":
        lbl_text.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            HomeWindow()
            USERNAME.set("")
            PASSWORD.set("")
            lbl_text.config(text="")
        else:
            lbl_text.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")   
    cursor.close()
    conn.close()
 
def HomeWindow():
    global Home
    root.withdraw()
    Home = Toplevel()
    Home.title("WELCOME TO CATIPULT GAME 2.0")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.resizable(0, 0)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    lbl_home = Label(Home, text="Successfully Login!", font=('times new roman', 20)).pack()
    btn_back = Button(Home, text='Back', command=Back).pack(pady=20, fill=X)
 
def Back():
    Home.destroy()
    root.deiconify()



GAME_STATE = "Testing"


class Game(arcade.Window):

    def __init__(self):
        self.catapult = Catapult_body()

        super().__init__(game_settings.get("SCREEN_WIDTH"),game_settings.get("SCREEN_HEIGHT"),game_settings.get("SCREEN_TITLE"))

        arcade.set_background_color()

        self.physics_list = None
        self.static_list = None

    def setup(self):
        pass

    def on_draw(self):
        pass

    def update(self, delta_time):
        pass

class Catapult_body(arcade.Sprite):

    def __init__(self):
        self.catapult_sprite = arcade.Sprite("Assets\Sprites\Trebuchette\pieces\chassis.png")

    def setup(self):
        pass
    
    def update(self):
        pass

    def draw(self):
        pass


            # Rooms needed
            # - level 1+ - Devan
            # - Victory screen - Devan
            # - opening screen - Manoel
            # - save/load menu - Richard

    global game_settings
    reader = csv.reader(open('game_settings.csv','r'))
    game_settings = {}
    for row in reader:
        k, v = row
        try:
            v = int(v)
        except:
            pass
        game_settings[k] = v

    window = Game()
    window.setup()
    arcade.run()


#==============================INITIALIATION==================================
if __name__ == '__main__':
    root.mainloop()

