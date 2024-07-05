from functions import showCopyrightClaim, showErrorMessage
import json
from teacher_account import TeacherAccount

class TeacherLogin:

    '''
    The StudentLogin class handles the creation and management of the student login interface.
    It provides fucntinalities for teachers to log in by providing their teaher's id and navigate
    back to the menu using back button

    Attributes:
        master(tk.Tk): The main window or parent widget.
        ctk(module): Customtkinter module used for custom widgets.
        button_font(font): Font used for the buttons.
        login_frame(CTkFrame): The frame that holds all login related widgets.
        header_label(CTkLabel): Label for the header text.
        id_label(CTkLabel): Label for the id entry.
        id_entry(CTkEntry): Entry widget for teacher id.
        back_button(CTkButton): Button for navigating to the main menu.
        login_button(CTkButton): Button to login.


    Methods:
        __init__(self, master, ctk, buttonFont): Initializes the TeacherLogin class and sets up the gui elements.
        backToMain(self): Destroys the current window and returns to the main frame.

    '''

    def __init__(self, master, ctk, buttonFont):
        '''
        Initializes the TeacherLogin class. Sets up the login frame, header, id entry and buttons.

        Args:
            master(tk.Tk): The main window or parent widget.
            ctk(module): Module used for custom widgets.
            buttonFont(font): Font used for button.
        '''
        self.ctk = ctk
        self.master = master
        self.button_font = buttonFont

        # Create login frame
        self.login_frame = self.ctk.CTkFrame(self.master, width=800, height=500, border_width=2, border_color="white")
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center")

        # copyright claim 
        showCopyrightClaim(self.ctk, self.login_frame)

        # label header
        self.header_label = self.ctk.CTkLabel(
            self.login_frame,
            text = "Welcome to Our School\nLogin as a Teacher",
            font=('Arial', 50, 'bold'),
            text_color = "white",
        )
        self.header_label.place(relx=0.5, rely=0, anchor="n", y=10)

        # Label ID
        self.id_label = self.ctk.CTkLabel(
            self.login_frame,
            text="ID No.",
            text_color="white",
            font=self.button_font  # Use the font passed from main
        )
        self.id_label.place(relx=0.3, rely=0.4)

        # id Entry
        self.id_entry = self.ctk.CTkEntry(
            self.login_frame,
            width=250,
            font=self.button_font,
            placeholder_text = "Enter ID"
        )
        self.id_entry.place(relx=0.4, rely=0.4)

        # Back button
        self.back_button = self.ctk.CTkButton(
            self.login_frame,
            text="Back",
            text_color="white",
            font=self.button_font,
            width=150,
            height=35,
            fg_color="red",  # Ensure visible color
            command=self.backToMain
        )
        self.back_button.place(relx=0.3, rely=0.6)

        # login button
        self.login_button = self.ctk.CTkButton(
            self.login_frame,
            text="Login",
            text_color="white",
            font=self.button_font,
            width=150,
            height=35,
            # fg_color="red",  # Ensure visible color
            command=self.authenticateTeacherLogin
        )
        self.login_button.place(relx=0.6, rely=0.6)



    def backToMain(self):
        '''
        Destroys the current window and returns to the main menu
        '''
        self.login_frame.destroy()
        self.master.create_main_frame()

    def openTeacherAccount(self, teacher_name, teacher_salary, accessed_class, teacher_id):
        self.teacher_name = teacher_name
        self.teacher_salary = teacher_salary
        self.accessed_class = accessed_class
        self.teacher_id = teacher_id

        self.login_frame.destroy()
        TeacherAccount(self.master, self.ctk, self.button_font, self.teacher_name, self.teacher_salary, self.accessed_class, self.teacher_id)


    def authenticateTeacherLogin(self):
        teacher_id = self.id_entry.get()

        try:
            with open("teachers.json", 'r') as f:
                data = json.load(f)

            # find teacher id 
            teacher_data = next((teacher for teacher in data["teachers"] if teacher["id"] == teacher_id), None)
            if not teacher_data:
                showErrorMessage(f"ID {teacher_id} not found")
                return
            
            # extract teahcer data 
            teacher_name = teacher_data["Name"]
            teacher_salary = teacher_data["Salary"]
            accessed_class = teacher_data["accessed class"]

            self.openTeacherAccount(teacher_name, teacher_salary, accessed_class, teacher_id)

        except FileNotFoundError:
            showErrorMessage("File doesn't exist")
        except json.JSONDecodeError:
            showErrorMessage("Error reading the json file")


