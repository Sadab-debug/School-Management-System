from tkinter import filedialog
import tkinter.messagebox as messagebox
from PIL import Image, ImageTk
import json



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


def uploadImage(self, filename):
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        try:
            with open(filename, 'r') as f:
                data = json.load(f)

            data['profile_pic'] = file_path  # Update the profile_pic path

            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)

            image = Image.open(file_path)
            image = image.resize((200, 200), Image.Resampling.LANCZOS)
            self.profile_image = ImageTk.PhotoImage(image)

            # Update the label to show the profile picture
            self.profile_picture_label.configure(image=self.profile_image, text="")

        except FileNotFoundError:
            showErrorMessage("The admin_id.json file does not exist.")

        except json.JSONDecodeError:
            showErrorMessage("Error reading the admin_id.json file.")


def loadProfileImage(filename, label):
    """
    Loads the profile image from a JSON file if it exists and sets it to a label.
    
    Args:
        filename (str): The JSON file containing the profile image path.
        label (tk.Label): The Tkinter label where the image will be displayed.
    """
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            file_path = data.get('profile_pic')
            if file_path:
                image = Image.open(file_path)
                image = image.resize((200, 200), Image.Resampling.LANCZOS)
                profile_image = ImageTk.PhotoImage(image)
                label.configure(image=profile_image, text="")
                label.image = profile_image  # Keep a reference to avoid garbage collection
    except (FileNotFoundError, json.JSONDecodeError):
        print(f"{filename} not found or corrupted")


