from functions import uploadImage, showCopyrightClaim
from PIL import Image, ImageTk
import json
from tkinter import messagebox, Toplevel


class AdminAccount:

    """
    The AdminAccount class handles the creation and management of the admin account interface.
    It provides functionalities to upload a profile picture, create classes, view existing classes,
    and manage students within these classes. The class interacts with JSON files to save and load
    data persistently.

    Attributes:
        master (tk.Tk): The main window or parent widget.
        ctk (module): CustomTkinter module used for custom widgets.
        button_font (font): Font used for the buttons.
        main_frame (CTkScrollableFrame): Main frame that holds all account-related widgets.
        account_frame (CTkFrame): Frame that holds account-specific widgets.
        profile_frame (CTkFrame): Frame for displaying the profile picture.
        profile_picture_label (CTkLabel): Label for the profile picture.
        upload_button (CTkButton): Button to upload a profile picture.
        create_class (CTkButton): Button to create a new class.
        back_button (CTkButton): Button to navigate back to the main menu.
        classes (CTkButton): Button to display each class.

    Methods:
        __init__(self, master, ctk, button_font): Initializes the AdminAccount class and sets up the GUI elements.
        backToMain(self): Destroys the current main frame and returns to the main menu.
        loadProfileImage(self): Loads the profile image from 'admin_id.json' if it exists.
        showExistingClasses(self): Displays existing classes from 'classes.json'.
        addClassButton(self, class_name): Adds a button for each class in the main frame.
        createClass(self): Opens a new window to create a class and saves it to 'classes.json'.
        saveClass(self): Saves the new class to 'classes.json' and updates the GUI.
        openClass(self, c, filename='classes.json'): Opens a window to display and manage students in the selected class.
        createStudent(self, class_name): Opens a window to create a new student for the selected class.
        saveStudent(self, class_name): Saves the new student to the respective class in 'classes.json'.
    """

    def __init__(self, master, ctk, button_font) -> None:

        
        """
        Initializes the AdminAccount class. Sets up the main frame and account frame, loads the profile
        image, and displays existing classes.

        Args:
            master (tk.Tk): The main window or parent widget.
            ctk (module): CustomTkinter module used for custom widgets.
            button_font (font): Font used for the buttons.
        """

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
        self.upload_button = self.ctk.CTkButton(self.account_frame, font=self.button_font, text="Upload Photo", width=150, height=35, text_color='white', command=lambda: uploadImage(self, filename='admin_id.json'))
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
            command=self.backToMain
        )
        self.back_button.place(relx=0.2, rely=0.45)

        # show existing classes
        self.showExistingClasses()



    def backToMain(self):
        """
        Handles the back button action. Destroys the current main frame and navigates back to the main menu.
        """
        self.main_frame.destroy()
        self.master.create_main_frame()


    
    def loadProfileImage(self):
        """
        Loads the profile image from 'admin_id.json' if it exists. Displays a placeholder if not found.
        """
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
        """
        Displays existing classes by reading from 'classes.json'.
        """
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
        """
        Adds a button for each class in the main frame.

        Args:
            class_name (str): The name of the class.
        """
        self.classes = self.ctk.CTkButton(
            self.main_frame,
            text=f"Class {class_name}",
            text_color="white",
            font=self.button_font,
            width=700,
            height=100,
            command=lambda c=class_name: self.openClass(c) #open class
        )
        self.classes.pack(padx=10, pady=10)



    def createClass(self):
        """
        Opens a new window to create a class and saves it to 'classes.json'.
        """
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
        """
        Saves the new class to 'classes.json' and updates the GUI.
        """
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
                self.window.destroy() #destroys create class window

            else:
                messagebox.showerror("Error", "Class already exists")
                

    def openClass(self, c, filename='classes.json'):
        """
        Opens a window to display and manage students in the selected class.

        Args:
            c (str): The name of the class.
            filename (str): The JSON file to read data from. Defaults to 'classes.json'.
        """
        self.width = 1200
        self.height = 750

        self.window = self.ctk.CTk()
        self.window.resizable(False, False)
        self.window.geometry(f"{self.width}x{self.height}")
        self.window.title(f"Class : {c}")

        # Display copyright claim
        showCopyrightClaim(self.ctk, self.window)

        self.main_frame = self.ctk.CTkScrollableFrame(
            self.window,
            width=1000,
            height=600,
            border_width=2,
            border_color="white",
            orientation='vertical'
        )
        self.main_frame.place(relx=0.5, rely=0.5, anchor='center')

        try:
            with open(filename, 'r') as f:
                data = json.load(f)

            class_data = None
            for cls in data['classes']:
                if cls['class'] == c:
                    class_data = cls
                    break
            
            if not class_data:
                raise ValueError("Class not found")

            for student in class_data["students"]:
                student_info = f"{student['Name']}      Roll: {student['Roll']}"
                show_student = self.ctk.CTkButton(
                    self.main_frame,
                    width=950,
                    height=50,
                    text=student_info,
                    font=self.button_font,
                    fg_color='black',
                    border_width=2,
                    border_color='white'
                )
                show_student.pack(padx=10, pady=10)
                                        
        except FileNotFoundError:
            messagebox.showerror("Error", "classes.json not found.")
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Error decoding JSON from classes.json.")
        except KeyError as e:
            messagebox.showerror("Error", f"Missing key in JSON data: {e}")

        # Add students button
        self.create_student = self.ctk.CTkButton(
            self.window,
            text="Create Student",
            font=self.button_font,
            width=50,
            height=25,
            command=lambda: self.createStudent(class_name=c)
        )
        self.create_student.pack(side='bottom', pady=10)

        self.window.mainloop()


    def createStudent(self, class_name):
        """
        Opens a window to create a new student for the selected class.

        Args:
            class_name (str): The name of the class to which the student will be added.
        """
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

        self.student_phone_number_label = self.ctk.CTkLabel(self.student_window, text="Phone Number", text_color='black')
        self.student_phone_number_label.grid(row=5, column=0)
        self.student_phone_number_entry = self.ctk.CTkEntry(self.student_window)
        self.student_phone_number_entry.grid(row=5, column=1)

        self.student_guardian_label = self.ctk.CTkLabel(self.student_window, text="Guardian", text_color='black')
        self.student_guardian_label.grid(row=6, column=0)
        self.student_guardian_entry = self.ctk.CTkEntry(self.student_window)
        self.student_guardian_entry.grid(row=6, column=1)

        subjects = [
            "Bangla",
            "English",
            "Math",
            "Science",
            "Life and Livelihood",
            "Digital Technology",
            "History and Social Science",
            "Religion",
            "Wellbeing",
            "Arts and Culture"
        ]
        self.marks_entries = {}
        for i, subject in enumerate(subjects, start=1):
            label = self.ctk.CTkLabel(self.student_window, text=f"{subject} Marks", text_color='black')
            label.grid(row=6+i, column=0)
            entry = self.ctk.CTkEntry(self.student_window)
            entry.grid(row=6+i, column=1)
            self.marks_entries[f"{subject}"] = entry

        self.save_student_button = self.ctk.CTkButton(
            self.student_window,
            text="Save Student",
            command=lambda: self.saveStudent(class_name)
        )
        self.save_student_button.grid(row=17, column=0, columnspan=2)


    def saveStudent(self, class_name):
        """
        Saves the new student to the respective class in 'classes.json'.

        Args:
            class_name (str): The name of the class to which the student will be added.
        """
        student_data = {
            "Name": self.student_name_entry.get(),
            "ID": self.student_id_entry.get(),
            "Roll": self.student_roll_entry.get(),
            "Marks": {subject: int(entry.get()) for subject, entry in self.marks_entries.items()},
            "OtherInfo": {
                "Age": int(self.student_age_entry.get()),
                "Address": self.student_address_entry.get(),
                "Phone Number": self.student_phone_number_entry.get(),
                "Guardian": self.student_guardian_entry.get(),
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
