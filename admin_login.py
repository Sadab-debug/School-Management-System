from functions import showCopyrightClaim, showErrorMessage, showInfo
from json import load
from admin_account import AdminAccount

class AdminLogin:
    '''
    The AdminLogin class handles the creation and management of the admin login interface.
    It provides functionalities for admins to log in by entering their ID and has a button
    to navigate back to the main menu.

    Attributes:
        master (tk.Tk): The main window or parent widget.
        ctk (module): CustomTkinter module used for custom widgets.
        button_font (font): Font used for the buttons.
        login_frame (CTkFrame): Frame that holds all login-related widgets.
        header_label (CTkLabel): Label for the header text.
        id_label (CTkLabel): Label for the ID entry.
        id_entry (CTkEntry): Entry widget for the admin ID.
        back_button (CTkButton): Button to navigate back to the main menu.
        login_button (CTkButton): Button to log in as an admin.

    Methods:
        __init__(self, master, ctk, buttonFont): Initializes the AdminLogin class and sets up the GUI elements.
        backToMain(self): Destroys the current login frame and returns to the main menu.
        openAdminAccount(self): Destroys the current login frame and opens the admin account interface.
        authenticateAdminLogin(self): Authenticates the admin login by checking the ID against stored data.
    '''
    def __init__(self, master, ctk, buttonFont):
        '''
        Initializes the AdminLogin class. Sets up the login frame, header, ID entry, and buttons.

        Args:
            master (tk.Tk): The main window or parent widget.
            ctk (module): CustomTkinter module used for custom widgets.
            buttonFont (font): Font used for the buttons.
        '''
        self.ctk = ctk
        self.master = master
        self.button_font = buttonFont

        # create login frame
        self.login_frame = self.ctk.CTkFrame(self.master, width=800, height=500, border_width=2, border_color="white")
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center")

        # copyright claim 
        showCopyrightClaim(self.ctk, self.login_frame)


        # label header
        self.header_label = self.ctk.CTkLabel(
            self.login_frame,
            text = "Welcome to Our School\nLogin as a Admin",
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
            placeholder_text = "Enter ID No.",
            width=250,
            font=self.button_font
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
            command = self.authenticateAdminLogin,
            width=150,
            height=35,
            # fg_color="red",  # Ensure visible color
            # command=self.back_to_main
        )
        self.login_button.place(relx=0.6, rely=0.6)


    def backToMain(self):
        '''
        Handles the back button action. Destroys the current login frame and navigates back to the main menu.
        '''
        self.login_frame.destroy()
        self.master.create_main_frame()

    def openAdminAccount(self):
        '''
        Opens the admin account interface by destroying the current login frame and initializing the AdminAccount class.
        '''
        self.login_frame.destroy()
        AdminAccount(self.master, self.ctk, self.button_font)

    def authenticateAdminLogin(self):
        '''
        Authenticates the admin login by checking the entered ID against the stored admin ID in a JSON file.

        If the ID matches, a success message is shown and the admin account interface is opened.
        If the ID does not match or the file does not exist, an error message is shown.
        '''
        data_file = 'admin_id.json'
        id_no = self.id_entry.get()

        try:
            with open(data_file) as f:
                data = load(f)
                if id_no != data.get("admin_id"):
                    showErrorMessage(message="Login status: failed!.\nFatal error: unknown!\nId number incorrect!")
                else:
                    showInfo("Logged in successfully!")
                    self.openAdminAccount()
        except FileNotFoundError:
            showErrorMessage(message="File doesn't exist")

