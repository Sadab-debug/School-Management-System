import customtkinter as ctk
from functions import onEnter, onLeave, showCopyrightClaim
from student_login import StudentLogin
from teacher_login import TeacherLogin
from admin_login import AdminLogin
from credentials import Credentials


ctk.set_appearance_mode("dark") #options: "light", "dark", "system"
ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"

class App(ctk.CTk):

    '''
    The main application class for the School Management System.

    Attributes:
        main_frame (CTkFrame): The main frame that holds all the main menu widgets.
        button_font (tuple): Font style used for the buttons.

    Methods:
        create_main_frame(): Creates the main menu frame with buttons for login and privacy policy.
        openStudentLogin(): Opens the student login interface.
        openTeacherLogin(): Opens the teacher login interface.
        openAdminLogin(): Opens the admin login interface.
        openCredentials(): Opens the privacy and policy information.
    '''

    def __init__(self):
        '''
        Initializes the the main screen and widgets inside the screen.
        '''
        super().__init__()

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # self.FG_COLOR = "#C0C0C0"
        self.button_font = ("Arial", 20)


        # set window, title and size
        self.title("School Management System")
        self.geometry(f"{screen_width}x{screen_height}")
        self.minsize(400, 300)


        # Create the main frame
        self.main_frame = None
        self.create_main_frame()


    def create_main_frame(self):
        '''
        Creates the main menu frame with buttons for logging in as a student, teacher, or admin,
        and for viewing privacy and policy information.
        '''
        if self.main_frame is not None:
            self.main_frame.destroy()

        self.main_frame = ctk.CTkFrame(self, width=800, height=500, border_width = 2, border_color = "white")
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center")

        # copyright claim 
        showCopyrightClaim(ctk, self.main_frame)


        # teacher login
        self.teacher_login = ctk.CTkButton(
            self.main_frame,
            text="Login as Teacher",
            text_color="white",
            font=self.button_font,
            width=250,  # Adjust width to fit the text
            height=100,  # Adjust height to fit the text
            # fg_color="black",
            command=self.openTeacherLogin,
            border_width=2,
            border_color="black",
        )
        self.teacher_login.place(relx=0.03, rely=0.1)
        #  Bind hover events 
        self.teacher_login.bind("<Enter>", lambda event: onEnter(event, self.teacher_login))
        self.teacher_login.bind("<Leave>", lambda event: onLeave(event, self.teacher_login))

        
        # admin login
        self.admin_login = ctk.CTkButton(
            self.main_frame,
            text="Login as Admin",
            text_color="white",
            font=self.button_font,
            width=250,  # Adjust width to fit the text
            height=100,  # Adjust height to fit the text
            # fg_color="black",
            command= self.openAdminLogin,
            border_width=2,
            border_color="black",
        )
        self.admin_login.place(relx=0.03, rely=0.5)
        #  Bind hover events 
        self.admin_login.bind("<Enter>", lambda event: onEnter(event, self.admin_login))
        self.admin_login.bind("<Leave>", lambda event: onLeave(event, self.admin_login))


        # student login
        self.student_login = ctk.CTkButton(
            self.main_frame,
            text="Login as Student",
            text_color="white",
            font=self.button_font,
            width=250,  # Adjust width to fit the text
            height=100,  # Adjust height to fit the text
            # fg_color="black",
            command=self.openStudentLogin,
            border_width=2,
            border_color="black",
        )
        self.student_login.place(relx=0.65, rely=0.1)
        #  Bind hover events 
        self.student_login.bind("<Enter>", lambda event: onEnter(event, self.student_login))
        self.student_login.bind("<Leave>", lambda event: onLeave(event, self.student_login))


        # credentials
        self.credentials = ctk.CTkButton(
            self.main_frame,
            text="Privacy & Policy",
            text_color="white",
            font=self.button_font,
            width=250,  # Adjust width to fit the text
            height=100,  # Adjust height to fit the text
            # fg_color="black",
            command= self.openCredentials,
            border_width=2,
            border_color="black",
        )
        self.credentials.place(relx=0.65, rely=0.5)
        #  Bind hover events 
        self.credentials.bind("<Enter>", lambda event: onEnter(event, self.credentials))
        self.credentials.bind("<Leave>", lambda event: onLeave(event, self.credentials))


    def openStudentLogin(self):
        """
        Destroys the main frame and opens the student login interface.
        """
        self.main_frame.destroy()
        StudentLogin(self, ctk, buttonFont=self.button_font)

    def openTeacherLogin(self):
        """
        Destroys the main frame and opens the teacher login interface.
        """
        self.main_frame.destroy()
        TeacherLogin(self, ctk, buttonFont=self.button_font)

    def openAdminLogin(self):
        """
        Destroys the main frame and opens the admin login interface.
        """
        self.main_frame.destroy()
        AdminLogin(self, ctk, buttonFont=self.button_font)

    def openCredentials(self):
        """
        Destroys the main frame and opens the privacy and policy information interface.
        """
        self.main_frame.destroy()
        Credentials(self, ctk, buttonFont=self.button_font)


# create and run the app
if __name__ == "__main__":
    app = App()
    app.mainloop()
 

