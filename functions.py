import tkinter.messagebox as messagebox

#border effect on hover
def onEnter(event, var):
    var.configure(border_color="white")

#border effect out on removing cursor
def onLeave(event, var):
    var.configure(border_color="black")


def showCopyrightClaim(ctk, frame_name):
    copyright_claim = ctk.CTkLabel(
        frame_name,
        text="© 2024 All rights reserved. Software developed by Sadab.",
        text_color="white",
        font=("Arial", 12, "italic"),
        justify="right"
    )
    copyright_claim.place(relx=0.95, rely=0.95, anchor="se")

def showErrorMessage(message):
    messagebox.showerror("Error!", message)

def showInfo(message):
    messagebox.showinfo("Info", message)