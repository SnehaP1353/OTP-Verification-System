import twilio.rest
import random
from tkinter import Tk, Text, Canvas, Label, Button, messagebox

# Creating Window
root = Tk()
root.title("OTP Verification")
root.geometry("600x550")

# Twilio account details
account_sid = " "
auth_token = " "

# Resend the OTP
def resendOTP():
    global n
    try:
        n = random.randint(1000, 9999)
        client = twilio.rest.Client(account_sid, auth_token)
        client.messages.create(to=[" "], from_=" ", body=str(n))
        messagebox.showinfo("Info", "OTP Resent Successfully")
    except Exception as e:
        messagebox.showerror("Error", f"Error resending OTP: {str(e)}")

# Checking the OTP
def checkOTP():
    global n
    try:
        user_input = int(user.get(1.0, "end-1c"))
        if user_input == n:
            messagebox.showinfo("Info", "Login Success")
            n = "done"
        elif n == "done":
            messagebox.showinfo("Info", "Already entered")
        else:
            messagebox.showinfo("Info", "Wrong OTP")
    except ValueError:
        messagebox.showinfo("Info", "Invalid OTP")

# Drawing the canvas
c = Canvas(root, bg="white", width=400, height=300)
c.place(x=100, y=60)

# Label widget
login = Label(root, text="OTP Verification", font="bold,20", bg="white")
login.place(x=210, y=90)

# Entry widget
user = Text(root, borderwidth=2, wrap="word", width=29, height=2)
user.place(x=190, y=160)

# Sending the OTP
try:
    n = random.randint(1000, 9999)
    client = twilio.rest.Client(account_sid, auth_token)
    client.messages.create(to=[" "], from_=" ", body=str(n))
except Exception as e:
    print(f"Error creating Twilio message: {str(e)}")

# Submit button
submit_button = Button(root, text="Submit", command=checkOTP, font=('bold', 15),bg="green",fg="white")
submit_button.place(x=258, y=250)

# Resend Button
resend_button = Button(root, text="Resend OTP", command=resendOTP, font=("bold", 15),bg="blue",fg="white")
resend_button.place(x=240, y=400)

# Event Loop
root.mainloop()