from functions import uploadImage, showCopyrightClaim
from PIL import Image, ImageTk
import json
from tkinter import messagebox


class AdminAccount:
    def __init__(self, master, ctk, button_font) -> None:
        self.master = master
        self.ctk = ctk
        self.button_font = button_font

        # Create main frame
        self.main_frame = self.ctk.CTkScrollableFrame(
            self.master,
            width=1200,
            height=700,
            border_width=2,
            border_color="white",
            orientation='vertical'
        )
        self.main_frame.place(relx=0.5, rely=0.5, anchor='center')

        # copyright
        showCopyrightClaim(self.ctk, self.master)

        # Create account frame
        self.account_frame = self.ctk.CTkFrame(
            self.main_frame,
            width=300,
            height=700,
            fg_color='black',
        )
        self.account_frame.pack(side='left', fill='y')

        # Add profile picture frame
        self.profile_frame = self.ctk.CTkFrame(self.account_frame, width=150, height=150)
        self.profile_frame.place(relx=0.2, rely=0.01)

        # Placeholder for profile picture
        self.profile_picture_label = self.ctk.CTkLabel(self.profile_frame, text="No Image", font=('Arial', 20, 'bold'))
        self.profile_picture_label.place(relx=0.05, rely=0.01)

        # Load profile image if exists
        self.loadProfileImage()

        # Add button to upload photo
        self.upload_button = self.ctk.CTkButton(self.account_frame, font=self.button_font, text="Upload Photo", width=150, height=35, text_color='white', command=lambda: uploadImage(self))
        self.upload_button.place(relx=0.2, rely=0.25)

        # create student account
        self.create_class = self.ctk.CTkButton(self.account_frame, font=self.button_font, text="Create Class", width=150, height=35, text_color='white', command=self.createClass)
        self.create_class.place(relx=0.2, rely=0.35)

        # back button
        self.back_button = self.ctk.CTkButton(
            self.account_frame,
            text="Back",
            text_color="white",
            font=self.button_font,
            width=150,
            height=35,
            fg_color="red",  # Ensure visible color
            command=self.back_to_main
        )
        self.back_button.place(relx=0.2, rely=0.45)

        # show existing classes
        self.showExistingClasses()


    def back_to_main(self):
        self.main_frame.destroy()
        self.master.create_main_frame()


    def loadProfileImage(self):
        try:
            with open('admin_id.json', 'r') as f:
                data = json.load(f)
                file_path = data.get('profile_pic')
                if file_path:
                    image = Image.open(file_path)
                    image = image.resize((200, 200), Image.Resampling.LANCZOS)
                    self.profile_image = ImageTk.PhotoImage(image)
                    self.profile_picture_label.configure(image=self.profile_image, text="")
        except (FileNotFoundError, json.JSONDecodeError):
            print("admin_id.json not found or corrupted")


    def showExistingClasses(self):
        try:
            with open('classes.json', 'r') as f:
                data = json.load(f)
                # Ensure we are dealing with a list of classes
                class_list = data.get("class", [])
                for class_name in class_list:
                    self.addClassButton(class_name)
        except FileNotFoundError:
            print("classes.json not found.")
        except json.JSONDecodeError:
            print("Error decoding JSON from classes.json.")


    def addClassButton(self, class_name):
        self.classes = self.ctk.CTkButton(
            self.main_frame,
            text=class_name,
            text_color="white",
            font=self.button_font,
            width=700,
            height=100,
        )
        self.classes.pack(padx=10, pady=10)


    def createClass(self):
        self.width = 200
        self.height = 250

        self.window = self.ctk.CTk()
        self.window.resizable(False, False)
        self.window.geometry(f"{self.width}x{self.height}")
        self.window.title("Info")

        # labels
        self.class_name_label = self.ctk.CTkLabel(
            self.window,
            text="Class Name",
            text_color='white',
            font=('Arial', 10, 'bold'),
        )
        self.class_name_label.place(relx=0.5, rely=0.3, anchor='center')

        # entry
        self.class_entry = self.ctk.CTkEntry(
            self.window,
            width=100,
            corner_radius=2,
            placeholder_text='Enter Class (i.e. 7 or 8)',
        )
        self.class_entry.place(relx=0.5, rely=0.5, anchor='center')

        # buttons
        self.create_btn = self.ctk.CTkButton(
            self.window,
            text='Create',
            text_color='white',
            width=50,
            height=35,
            font=self.button_font,
            command=self.saveClass
        )
        self.create_btn.place(relx=0.5, rely=0.7, anchor='center')

        self.window.mainloop()


    def saveClass(self):
        class_name = self.class_entry.get()
        if class_name:
            # Read the existing data from the JSON file
            try:
                with open('classes.json', 'r') as f:
                    data = json.load(f)
            except FileNotFoundError:
                data = {"class": []}
            
            if class_name not in data["class"]:
                # Append the new class name to the list
                data["class"].append(class_name)
                
                # Write the updated data back to the JSON file
                with open('classes.json', 'w') as f:
                    json.dump(data, f, indent=4)

                # Update the UI
                self.add_class_button(class_name)


                # Close the class creation window
                self.window.destroy()

            else:
                messagebox.showerror("Error", "Class already exists")

    