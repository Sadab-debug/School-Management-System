from functions import uploadImage, showCopyrightClaim
from PIL import Image, ImageTk
import json
from tkinter import messagebox, Toplevel


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
                class_list = data.get("classes", [])
                for class_data in class_list:
                    self.addClassButton(class_data["class"])
        except FileNotFoundError:
            print("classes.json not found.")
        except json.JSONDecodeError:
            print("Error decoding JSON from classes.json.")



    def addClassButton(self, class_name):
        self.classes = self.ctk.CTkButton(
            self.main_frame,
            text=f"Class {class_name}",
            text_color="white",
            font=self.button_font,
            width=700,
            height=100,
            command=lambda c=class_name: self.openClass(c)
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
            try:
                with open('classes.json', 'r') as f:
                    data = json.load(f)
            except FileNotFoundError:
                data = {"classes": []}
            
            class_exists = any(cls["class"] == class_name for cls in data["classes"])

            if not class_exists:
                new_class = {
                    "class": class_name,
                    "students": []
                }
                data["classes"].append(new_class)
                
                with open('classes.json', 'w') as f:
                    json.dump(data, f, indent=4)

                self.addClassButton(class_name)
                self.window.destroy()

            else:
                messagebox.showerror("Error", "Class already exists")


    def openClass(self, c):
        self.width = 1200
        self.height = 720

        self.window = self.ctk.CTk()
        self.window.resizable(False, False)
        self.window.geometry(f"{self.width}x{self.height}")
        self.window.title(f"Class : {c}")

        self.main_frame = self.ctk.CTkScrollableFrame(
            self.window,
            width=1000,
            height=600,
            border_width=2,
            border_color="white",
            orientation='vertical'

        )
        self.main_frame.place(relx=0.5, rely=0.5, anchor='center')

        self.window.mainloop()

    def createStudent(self, class_name):
        self.student_window = Toplevel(self.master)
        self.student_window.title(f"Class {class_name}")

        self.student_name_label = self.ctk.CTkLabel(self.student_window, text="Student Name", text_color='black')
        self.student_name_label.grid(row=0, column=0)
        self.student_name_entry = self.ctk.CTkEntry(self.student_window)
        self.student_name_entry.grid(row=0, column=1)

        self.student_id_label = self.ctk.CTkLabel(self.student_window, text="Student ID", text_color='black')
        self.student_id_label.grid(row=1, column=0)
        self.student_id_entry = self.ctk.CTkEntry(self.student_window)
        self.student_id_entry.grid(row=1, column=1)

        self.student_roll_label = self.ctk.CTkLabel(self.student_window, text="Roll Number", text_color='black')
        self.student_roll_label.grid(row=2, column=0)
        self.student_roll_entry = self.ctk.CTkEntry(self.student_window)
        self.student_roll_entry.grid(row=2, column=1)

        self.student_age_label = self.ctk.CTkLabel(self.student_window, text="Age", text_color='black')
        self.student_age_label.grid(row=3, column=0)
        self.student_age_entry = self.ctk.CTkEntry(self.student_window)
        self.student_age_entry.grid(row=3, column=1)

        self.student_address_label = self.ctk.CTkLabel(self.student_window, text="Address", text_color='black')
        self.student_address_label.grid(row=4, column=0)
        self.student_address_entry = self.ctk.CTkEntry(self.student_window)
        self.student_address_entry.grid(row=4, column=1)

        self.marks_entries = {}
        for i in range(1, 11):
            label = self.ctk.CTkLabel(self.student_window, text=f"Subject{i} Marks", text_color='black')
            label.grid(row=4+i, column=0)
            entry = self.ctk.CTkEntry(self.student_window)
            entry.grid(row=4+i, column=1)
            self.marks_entries[f"Subject{i}"] = entry

        self.save_student_button = self.ctk.CTkButton(
            self.student_window,
            text="Save Student",
            command=lambda: self.saveStudent(class_name)
        )
        self.save_student_button.grid(row=15, column=0, columnspan=2)

    def saveStudent(self, class_name):
        student_data = {
            "Name": self.student_name_entry.get(),
            "ID": self.student_id_entry.get(),
            "Roll": self.student_roll_entry.get(),
            "Marks": {subject: int(entry.get()) for subject, entry in self.marks_entries.items()},
            "OtherInfo": {
                "Age": int(self.student_age_entry.get()),
                "Address": self.student_address_entry.get()
            }
        }

        try:
            with open('classes.json', 'r') as f:
                data = json.load(f)

            for cls in data["classes"]:
                if cls["class"] == class_name:
                    cls["students"].append(student_data)
                    break

            with open('classes.json', 'w') as f:
                json.dump(data, f, indent=4)

            self.student_window.destroy()

        except FileNotFoundError:
            messagebox.showerror("Error", "classes.json not found.")
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Error decoding JSON from classes.json.")



