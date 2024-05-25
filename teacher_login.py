class TeacherLogin:
    def __init__(self, master, ctk, buttonFont):
        self.ctk = ctk
        self.master = master
        self.button_font = buttonFont

        # Create login frame
        self.login_frame = self.ctk.CTkFrame(self.master, width=800, height=500, border_width=2, border_color="white")
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center")

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
            # fg_color="red",  # Ensure visible color
            command=self.back_to_main
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
            # command=self.back_to_main
        )
        self.login_button.place(relx=0.6, rely=0.6)

    def back_to_main(self):
        self.login_frame.destroy()
        self.master.create_main_frame()
