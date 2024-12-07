from tkinter import *
from tkinter import messagebox
import base64

def decrypt():
    password = code.get()
    
    if password == "1234":
        screen2 = Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#2c3e50")  # Dark background
        
        # Get the encrypted message
        message = text1.get(1.0, END).strip()
        
        try:
            # Decode the message
            base64_bytes = message.encode("ascii")
            decoded_bytes = base64.b64decode(base64_bytes)
            decrypted_message = decoded_bytes.decode("ascii")
        except Exception as e:
            messagebox.showerror("Decryption Error", "Invalid encrypted message.")
            return
        
        Label(screen2, text="Decrypted Message", fg="white", bg="#2c3e50", font=("Arial", 14)).place(x=10, y=10)
        
        # Text Area for decrypted message
        text2 = Text(screen2, font="Roboto 12", bg="#ecf0f1", fg="black", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        
        text2.insert(END, decrypted_message)
        
    elif password == "":
        messagebox.showerror("Decryption", "Input password")
    else:
        messagebox.showerror("Decryption", "Invalid password")

def encrypt():
    password = code.get()
    
    if password == "1234":
        screen1 = Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#2c3e50")  # Dark background
        
        message = text1.get(1.0, END).strip()
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypted_message = base64_bytes.decode("ascii")
        
        Label(screen1, text="Encrypted Message", fg="white", bg="#2c3e50", font=("Arial", 14)).place(x=10, y=10)
    
        # Text Area for encrypted message
        text2 = Text(screen1, font="Roboto 12", bg="#ecf0f1", fg="black", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        
        text2.insert(END, encrypted_message)
        
    elif password == "":
        messagebox.showerror("Encryption", "Input password")
    else:
        messagebox.showerror("Encryption", "Invalid password")

def main_screen():
    global screen
    global code
    global text1
    
    screen = Tk()
    screen.geometry("375x398")
    
    # Set the background color of the window
    screen.configure(bg="#34495e")  # Darker background
    
    # Icon 
    image_icon = PhotoImage(file="1.png")  # Ensure this file exists
    screen.iconphoto(False, image_icon)
    screen.title("EDApp")
    
    def reset():
        code.set("")
        text1.delete(1.0, END)
    
    # Title Label
    Label(text="Enter secret key for encryption and decryption", fg="white", bg="#34495e", font=("Arial", 14)).place(x=10, y=10)
    
    # Text Area
    text1 = Text(font="Roboto 12", bg="#ecf0f1", fg="black", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)
    
    # Secret Key Label
    Label(text="Enter secret key:", fg="white", bg="#34495e", font=("Arial", 14)).place(x=10, y=170)
    
    # Entry for Secret Key
    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("Arial", 25), show="*").place(x=10, y=200)
    
    # Buttons with different styles
    Button(text="Encrypt", height="2", width=23, bg="#e74c3c", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    Button(text="Decrypt", height="2", width=23, bg="#27ae60", fg="white", bd=0, command=decrypt).place(x=10, y=300)
    Button(text="RESET", height="2", width=50, bg="#2980b9", fg="white", bd=0, command=reset).place(x=10, y=350)
    
    screen.mainloop()

main_screen()