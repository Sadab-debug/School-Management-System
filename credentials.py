from functions import showCopyrightClaim


class Credentials:

    '''
    The Credentials class handles the creation and display of the credentials frame.
    It shows the privacy policy and provides a button to navigate back to the main menu.

    Attributes:
        master (tk.Tk): The main window or parent widget.
        ctk (module): CustomTkinter module used for custom widgets.
        button_font (font): Font used for the buttons and text.
        credential_frame (CTkFrame): Frame that holds all credentials-related widgets.
        privacy_policy_text (CTkLabel): Label to display the privacy policy text.
        back_button (CTkButton): Button to navigate back to the main menu.

    Methods:
        __init__(self, master, ctk, buttonFont): Initializes the Credentials class and sets up the GUI elements.
        back_to_main(self): Destroys the current credentials frame and returns to the main menu.
    '''

    def __init__(self, master, ctk, buttonFont):
        '''
        Initializes the Credentials class. Sets up the credential frame, privacy policy text, and back button.

        Args:
            master (tk.Tk): The main window or parent widget.
            ctk (module): CustomTkinter module used for custom widgets.
            buttonFont (font): Font used for the buttons and text.
        '''
        self.ctk = ctk
        self.master = master
        self.button_font = buttonFont

        # create credential frame
        self.credential_frame = self.ctk.CTkFrame(self.master, width=1000, height=600, border_width=2, border_color="white")
        self.credential_frame.place(relx=0.5, rely=0.5, anchor="center")


        # copyright claim 
        showCopyrightClaim(self.ctk, self.credential_frame)
        

         # Create a text widget for privacy and policy
        privacy_policy = (
            "Privacy Policy:\n\n"
            "1. Data Security: Your data is secure with us. We use advanced security measures to protect your information.\n\n"
            "2. Data Sharing: We do not share your information with third parties unless required by law.\n\n"
            "3. Data Collection: We collect only the necessary data required for the functionality of the application.\n\n"
            "4. Data Usage: Your data is used solely for the purpose of enhancing your experience with the application.\n\n"
            "5. User Consent: By using this application, you consent to the collection and use of your information as outlined in this policy.\n\n"
            "6. Data Retention: We retain your data only as long as necessary to fulfill the purposes for which it was collected.\n\n"
        )

        self.privacy_policy_text = self.ctk.CTkLabel(
            self.credential_frame,
            text=privacy_policy,
            text_color="white",
            font=self.button_font,
            justify="left",
            wraplength=700  # Adjust wrap length for better readability
        )
        self.privacy_policy_text.place(relx=0.5, rely=0.5, anchor="center")


        # Back button
        self.back_button = self.ctk.CTkButton(
            self.credential_frame,
            text="Back",
            text_color="white",
            font=self.button_font,
            width=150,
            height=35,
            fg_color="red",  # Ensure visible color
            command=self.back_to_main
        )
        self.back_button.place(relx=0.5, rely=0.9, anchor="center")


    def back_to_main(self):
        '''
        Handles the back button action. Destroys the current credentials frame and navigates back to the main menu.
        '''
        self.credential_frame.destroy()
        self.master.create_main_frame()

