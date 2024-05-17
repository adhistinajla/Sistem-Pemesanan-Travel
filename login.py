import tkinter
import customtkinter
import pywinstyles
import csv
from PIL import ImageTk, Image
from CTkMessagebox import CTkMessagebox

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

app=customtkinter.CTk()
app.geometry('1280x720')
app.state('withdrawn')
app.title('Login Page')


def menu_register():
    app.destroy()

    w=customtkinter.CTk()
    w.geometry('1280x720')
    w.state('withdrawn')
    w.title('Register Page')


    img1=ImageTk.PhotoImage(Image.open("bg_pattern.png"))
    l1=customtkinter.CTkLabel(master=w, image=img1)
    l1.pack()

    frame=customtkinter.CTkFrame(master=w, fg_color="#ffffff", width=550, height=600, corner_radius=30, bg_color="#000001")
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    l2=customtkinter.CTkLabel(master=frame, text="Halo!", font=("Poppins", 40, "bold"), text_color="#078be3")
    l2.place(x=65, y=53)

    l3=customtkinter.CTkLabel(master=frame, text="Yuk Daftar Dulu", font=("Poppins", 40, "bold"), text_color="#078be3")
    l3.place(x=65, y=99)

    entry1=customtkinter.CTkEntry(master=frame, width=425, height=50, corner_radius=30, fg_color="#deecfa", border_color="#deecfa", placeholder_text="Masukkan Username", font=("Poppins", 18))
    entry1.place(x=65, y=200)

    entry2=customtkinter.CTkEntry(master=frame, width=425, height=50, corner_radius=30, fg_color="#deecfa", border_color="#deecfa", placeholder_text="Masukkan Nomor Telepon", font=("Poppins", 18))
    entry2.place(x=65, y=270)

    entry3=customtkinter.CTkEntry(master=frame, width=425, height=50, corner_radius=30, fg_color="#deecfa", border_color="#deecfa", placeholder_text="Masukkan Kata Sandi", font=("Poppins", 18))
    entry3.place(x=65, y=340)

    def register_user():
        username = entry1.get()
        phone_number = entry2.get()
        password = entry3.get()

        with open('user_data.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, phone_number, password])

        CTkMessagebox(title="Register Info", message="Pendaftaran Akun Berhasil!", fg_color="#ffffff", bg_color="#ffffff", font=("Poppins", 15), button_color="#078be3", fade_in_duration=1)
    
    button2=customtkinter.CTkButton(master=frame, width=420, height=50, text="Register", corner_radius=30, font=("Poppins", 18), fg_color="#078be3", command=register_user)
    button2.place(x=65, y=410)

    l4=customtkinter.CTkLabel(master=frame, text="Sudah Punya Akun?", font=("Poppins", 15), text_color="#a6b0ba")
    l4.place(x=148, y=496)

    button3=customtkinter.CTkButton(master=frame, width=10, height=15, text="Login Aja", font=("Poppins SemiBold", 15), text_color="#a6b0ba", fg_color="#ffffff", hover=True, hover_color="#ebf5ff", corner_radius=200, command=login)
    button3.place(x=298, y=493)

    pywinstyles.set_opacity(frame, color="#000001")
    
    w.mainloop()

def login():
    img1=ImageTk.PhotoImage(Image.open("bg_pattern.png"))
    l1=customtkinter.CTkLabel(master=app, image=img1)
    l1.pack()

    frame=customtkinter.CTkFrame(master=l1, fg_color="#ffffff", width=550, height=600, corner_radius=30, bg_color="#000001")
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    l2=customtkinter.CTkLabel(master=frame, text="Halo!", font=("Poppins", 40, "bold"), text_color="#078be3")
    l2.place(x=65, y=53)

    l3=customtkinter.CTkLabel(master=frame, text="Silahkan Login", font=("Poppins", 40, "bold"), text_color="#078be3")
    l3.place(x=65, y=99)

    entry1=customtkinter.CTkEntry(master=frame, width=425, height=50, corner_radius=30, fg_color="#deecfa", border_color="#deecfa", placeholder_text="Masukkan Nomor Telepon", font=("Poppins", 18))
    entry1.place(x=65, y=200)

    entry2=customtkinter.CTkEntry(master=frame, width=425, height=50, corner_radius=30, fg_color="#deecfa", border_color="#deecfa", placeholder_text="Masukkan Kata Sandi", font=("Poppins", 18))
    entry2.place(x=65, y=270)

    button1=customtkinter.CTkButton(master=frame, text="Lupa Password?", font=("Poppins", 16), text_color="#a6b0ba", fg_color="#ffffff", hover=True, hover_color="#ebf5ff", corner_radius=30)
    button1.place(x=335, y=335)

    button2=customtkinter.CTkButton(master=frame, width=420, height=50, text="Login", corner_radius=30, font=("Poppins", 18), fg_color="#078be3")
    button2.place(x=65, y=380)

    l4=customtkinter.CTkLabel(master=frame, text="Belum Punya Akun?", font=("Poppins", 15), text_color="#a6b0ba")
    l4.place(x=146, y=455)

    button3=customtkinter.CTkButton(master=frame, width=10, height=15, text="Yuk Daftar", font=("Poppins SemiBold", 15), text_color="#a6b0ba", fg_color="#ffffff", hover=True, hover_color="#ebf5ff", corner_radius=200, command=menu_register)
    button3.place(x=295, y=453)

    pywinstyles.set_opacity(frame, color="#000001")

    app.mainloop()

login()