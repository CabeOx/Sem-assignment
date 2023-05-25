from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.title("theDatingApp")
def change_title():
    root.title("Find your soulmate Today")

root.after(2000, change_title)
root.geometry("950x560")
root.resizable(False, False)

def Login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "Rahul" and password == "Password":
        messagebox.showinfo(title="Login Success", message="You successfully logged in!")
    else:
        messagebox.showerror(title="Error", message="Invalid Login")

# Creating First frame
image_frame = Frame(bg="#B7B7B7")
image_frame.config(height=950, width=600) # Set the height and width of the frame

my_image = ImageTk.PhotoImage(Image.open("majs.jpg"))
my_image_label = Label(image=my_image)
my_image_label.place(x=20, y=20)

# Place the frame in the grid
image_frame.grid(row=0, column=0)

# Creating Second frame
login_frame = Frame(bg="#B7B7B7")
login_frame.config(height=950, width=400) # Set the height and width of the frame

# Creating Widgets
signUp_button = Button(login_frame, text="Sign Up", fg="#116D6E", bg="lightblue", font=("Ariel", 10, "bold"),
    borderwidth=0, cursor="heart")
signUp_button.place(x=290,y=0)

app_name = Label(login_frame, text="theDatingApp", fg="#116D6E", bg="#B7B7B7",font=("Ariel", 21, "bold"))
# app_name.config(font=("Ariel", 21, "bold"))
app_name.place(x=82, y=100)

app_welcome = Label(login_frame, text="The dating app that's more than just a swipe")
app_welcome.config(font=("Ariel", 13), fg="#116D6E", bg="#B7B7B7")
app_welcome.place(x=10, y= 160)

username_label = Label(login_frame, text="User name", font=("Ariel", 10, "bold"), fg="#116D6E", bg="#B7B7B7")
username_label.place(x=70, y=250)
username_entry = Entry(login_frame, fg="#116D6E", borderwidth=0, width=20, font="Ariel, 14", bg="white", cursor="heart")
username_entry.place(x=70, y=280)

password_label = Label(login_frame, text="Password", font=("Ariel", 10, "bold"), fg="#116D6E", bg="#B7B7B7")
password_label.place(x=70, y=310)
password_entry = Entry(login_frame, fg="#116D6E", borderwidth=0, width=20, show="*", font="Ariel, 14",bg="white", cursor="heart")
password_entry.place(x=70, y=340)

# Creating a Login Button
login_button = Button(login_frame, text="Login", fg="#116D6E", bg="lightblue", font=("Ariel", 19, "bold"),
    borderwidth=0, cursor="heart", command=Login)
login_button.place(x=90,y=430, width=170)

# Place the frame in the grid
login_frame.grid(row=0, column=1)


root.mainloop()
