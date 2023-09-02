import customtkinter
from tkinter import *
from tkinter import messagebox

app = customtkinter.CTk()
app.title("Login")
app.geometry("350x200")
app.config(bg="#242320")

#font1=('Arial',15,'bold')

# Funciones

username = '1'
password = '2'
trials = 0

def login():
    global username
    global username
    global trials
    written_username = username_entry.get()
    written_password = password_entry.get()
    
 
    if written_username == '' or written_password == '': # Si alguno de los campos está vacío
        messagebox.showwarning(title="Error", message="Enter your username and password.")
    elif written_username == username and written_password == password: # Si lo ingresado es igual al que definimos
        newWindow=Toplevel(app)
        newWindow.geometry("350x200")
        newWindow.config(bg="#242320")
        welcome_label = customtkinter.CTkLabel(newWindow, text="Welcome...", text_color = "#FFFFFF" ) #
        welcome_label.place(x= 100, y= 100) 
    elif written_username != username or written_password != password and trials < 3:
        messagebox.showerror(title="Error", message="Username or Password is not correct.")
        trials += 1
        if trials != 3: # Hasta que no alcance el máximo de intentos
            trials_laber = customtkinter.CTkLabel(app, text=f"You have {3-trials} trials", text_color = "#FFFFFF" )
            trials_laber.place(x= 100, y= 100)
        if trials == 3: # Cuando alcance el máximo de intentos
            login_button.destroy()
            locked_laber = customtkinter.CTkLabel(app, text="Your account is locked.", text_color = "#FFFFFF" )
            messagebox.showerror(title="Error", message="Your account is locked.")
            locked_laber.place(x= 100, y= 160)
 

# Configuraciones de pantalla y botones
username_label = customtkinter.CTkLabel(app, text="Username")#, text_font=font1, text_color="#FFFFFF")
username_label.place(x=2, y=25)

password_label = customtkinter.CTkLabel(app, text="Password")#, text_font=font1, text_color="#FFFFFF")
password_label.place(x=2, y=75)

username_entry = customtkinter.CTkEntry(app, fg_color="#FFFFFF", text_color="#000000", border_color="#FFFFFF", width=200, height=1)
username_entry.place(x=130, y=25)

password_entry = customtkinter.CTkEntry(app,show= '*' ,fg_color="#FFFFFF", text_color="#000000", border_color="#FFFFFF", width=200, height=1)
password_entry.place(x=130, y=75)

login_button = customtkinter.CTkButton(app,command= login ,text="Login",text_color = "#FFFFFF", fg_color = "#07b527", hover_color = "#07b527", width=50)
login_button.place(x= 140, y= 120)

app.mainloop()