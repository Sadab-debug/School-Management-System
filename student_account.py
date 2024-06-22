from functions import showCopyrightClaim, uploadImage


class StudentAccount:
    '''
    StudentAccount class handles all the account related functions of student.

    
    Attributes:
        master(tk.Tk): The main window or parent widget.
        ctk(module): Module used to set up custom widgets.
        button_font(font): Font used for buttons.
        name(str): Student's name.
        id(str): Student's ID.
        roll(str): Student's roll number.
        bangla(int): Marks in Bangla.
        english(int): Marks in English.
        math(int): Marks in Math.
        science(int): Marks in Science.
        life_livelihood(int): Marks in Life and Livelihood.
        digital_tech(int): Marks in Digital Technology.
        history_social_science(int): Marks in History and Social Science.
        religion(int): Marks in Religion.
        wellbeing(int): Marks in Wellbeing.
        arts_culture(int): Marks in Arts and Culture.
        age(int): Student's age.
        guardian(str): Student's guardian's name.
        phone(str): Student's phone number.

    Methods:
        __init__(self, master, ctk, button_font): Initializes up the StudentAccount class and sets up gui elements.
        backToMain(self): Destroys the current frame and returns to main menu

    '''
    def __init__(self, master, ctk, button_font, name, id, roll, bangla, english, math, science, life_livelihood, digital_tech, history_social_science, religion, wellbeing, arts_culture, age, guardian, phone, class_name) -> None:
        '''
        Initalizes StudentAccount class. Sets up the main frame and account frame, 
        loads the profile image and displays student's info

        Args:
            master(tk.Tk): The main window or parent widget.
            ctk(module): Sets up custom widgets.
            buttont_font(font): Font used for buttons.
            name(str): Student's name.
            id(str): Student's ID.
            roll(str): Student's roll number.
            bangla(int): Marks in Bangla.
            english(int): Marks in English.
            math(int): Marks in Math.
            science(int): Marks in Science.
            life_livelihood(int): Marks in Life and Livelihood.
            digital_tech(int): Marks in Digital Technology.
            history_social_science(int): Marks in History and Social Science.
            religion(int): Marks in Religion.
            wellbeing(int): Marks in Wellbeing.
            arts_culture(int): Marks in Arts and Culture.
            age(int): Student's age.
            guardian(str): Student's guardian's name.
            phone(str): Student's phone number.
            main_frame(CTkScrollableFrame): Frame that holds all the widgets of student account.
        '''
        self.master = master
        self.ctk = ctk
        self.button_font = button_font

        self.name = name
        self.id = id
        self.roll = roll
        self.class_name = class_name

        self.bangla = bangla
        self.english = english
        self.math = math
        self.science = science
        self.life_livelihood = life_livelihood
        self.digital_tech = digital_tech
        self.history_social_science = history_social_science
        self.religion = religion
        self.wellbeing = wellbeing
        self.arts_culture = arts_culture

        self.age = age
        self.guardian = guardian
        self.phone = phone

        self.font = ('Arial', 20, 'bold')

        # main_frame
        self.main_frame = self.ctk.CTkFrame(
            self.master,
            width=1200,
            height=650,
            border_width=2,
            border_color="white"
        )
        self.main_frame.place(relx=0.5, rely=0.5, anchor='center')

        # copyright claim
        showCopyrightClaim(self.ctk, self.master)

        # Set profile picture frame
        self.profile_frame = self.ctk.CTkFrame(self.main_frame, width=150, height=150, border_width=2, border_color='white')
        self.profile_frame.place(relx=0.02, rely=0.02)

        # Placeholder for profile picture
        self.profile_picture_label = self.ctk.CTkLabel(self.profile_frame, text="No Image", font=('Arial', 20, 'bold'))
        self.profile_picture_label.place(relx=0.03, rely=0.02)

        # back button
        self.back_button = self.ctk.CTkButton(
            self.main_frame,
            text="Back",
            text_color="white",
            font=self.button_font,
            width=150,
            height=35,
            fg_color="red",  # Ensure visible color
            command=self.backToMain
        )
        self.back_button.place(relx=0.15, rely=0.08)

        # photo uploadbutton
        self.upload_button = self.ctk.CTkButton(self.main_frame, font=self.button_font, text="Upload Photo", width=150, height=35, text_color='white', command=lambda: uploadImage(self))
        self.upload_button.place(relx=0.15, rely=0.02)

        # labels
        self.label_name = self.ctk.CTkLabel(self.main_frame, font=self.font, text="Name      : ")
        self.label_name.place(relx=0.02, rely=0.3)

        self.label_roll = self.ctk.CTkLabel(self.main_frame, font=self.font, text='Roll         : ')
        self.label_roll.place(relx=0.02, rely=0.35)

        self.label_id = self.ctk.CTkLabel(self.main_frame, font=self.font, text="ID            : ")
        self.label_id.place(relx=0.02, rely=0.4)

        self.label_class = self.ctk.CTkLabel(self.main_frame, font=self.font, text="Class      : ")
        self.label_class.place(relx=0.02, rely=0.45)

        self.label_phone = self.ctk.CTkLabel(self.main_frame, font=self.font, text="Phone     :")
        self.label_phone.place(relx=0.02, rely=0.5)


        # label info
        self.display_name = self.ctk.CTkLabel(self.main_frame, font=self.font, text=f"{self.name}", text_color="white", fg_color="black", width=115, height=30, corner_radius=20)
        self.display_name.place(relx=0.1, rely=0.3)

        self.display_roll = self.ctk.CTkLabel(self.main_frame, font=self.font, text=f"{self.roll}", text_color="white", fg_color="black", width=115, height=30, corner_radius=20)
        self.display_roll.place(relx=0.1, rely=0.35)

        self.display_id = self.ctk.CTkLabel(self.main_frame, font=self.font, text=f"{self.id}", text_color="white", fg_color="black", width=115, height=30, corner_radius=20)
        self.display_id.place(relx=0.1, rely=0.4)

        self.display_class = self.ctk.CTkLabel(self.main_frame, font=self.font, text=f"{self.class_name}", text_color="white", fg_color="black", width=115, height=30, corner_radius=20)
        self.display_class.place(relx=0.1, rely=0.45)

        self.display_phone = self.ctk.CTkLabel(self.main_frame, font=self.font, text=f"{self.phone}", text_color="white", fg_color="black", width=115, height=30, corner_radius=20)
        self.display_phone.place(relx=0.1, rely=0.5)

        
        # marks frame
        self.marks_frame = self.ctk.CTkFrame(
        self.main_frame,
        width = 718,
        height = 646,
        fg_color = 'black',
        )
        self.marks_frame.place(relx=0.4, rely=0.001)

        # display marks
        self.math_mark = self.ctk.CTkLabel(self.marks_frame, text="Math", font=self.font, text_color="white")
        self.math_mark.place(relx=0.02, rely=0.02)

        self.bangla_mark = self.ctk.CTkLabel(self.marks_frame, text="Bangla", font=self.font, text_color="white")
        self.bangla_mark.place(relx=0.02, rely=0.1)

        self.english_mark = self.ctk.CTkLabel(self.marks_frame, text="English", font=self.font, text_color="white")
        self.english_mark.place(relx=0.02, rely=0.2)

        self.science_mark = self.ctk.CTkLabel(self.marks_frame, text="Science", font=self.font, text_color="white")
        self.science_mark.place(relx=0.02, rely=0.3)

        self.religion_mark = self.ctk.CTkLabel(self.marks_frame, text="Religion", font=self.font, text_color="white")
        self.religion_mark.place(relx=0.02, rely=0.4)

        self.wellbeing_mark = self.ctk.CTkLabel(self.marks_frame, text="Wellbeing", font=self.font, text_color="white")
        self.wellbeing_mark.place(relx=0.02, rely=0.5)

        self.ac_mark = self.ctk.CTkLabel(self.marks_frame, text="Arts and Culture", font=self.font, text_color="white")
        self.ac_mark.place(relx=0.02, rely=0.6)

        self.dt_mark = self.ctk.CTkLabel(self.marks_frame, text="Digital Technology", font=self.font, text_color="white")
        self.dt_mark.place(relx=0.02, rely=0.7)

        self.ll_mark = self.ctk.CTkLabel(self.marks_frame, text="Life and Livelihood", font=self.font, text_color="white")
        self.ll_mark.place(relx=0.02, rely=0.8)

        self.hss_mark = self.ctk.CTkLabel(self.marks_frame, text="History and Social Science", font=self.font, text_color="white")
        self.hss_mark.place(relx=0.02, rely=0.9)


        # Progress bar with labels
        self.progress_font = ("Arial", 15, "bold")

        self.math_progress = ctk.CTkProgressBar(self.marks_frame, orientation='horizontal', mode="determinate", border_width=2, border_color='white', width=300, height=25)
        self.math_progress.place(relx=0.75, rely=0.02, anchor='center')
        self.math_progress.set(self.math / 100.0)
        self.label_1 = self.ctk.CTkLabel(self.marks_frame, text=f"{self.math}%", font=self.font, text_color="white")
        self.label_1.place(relx=0.45, rely=0.01)

        self.bangla_progress = ctk.CTkProgressBar(self.marks_frame, orientation='horizontal', mode="determinate", border_width=2, border_color='white', width=300, height=25)
        self.bangla_progress.place(relx=0.75, rely=0.1, anchor='center')
        self.bangla_progress.set(self.bangla / 100.0)
        self.label_2 = self.ctk.CTkLabel(self.marks_frame, text=f"{self.bangla}%", font=self.font, text_color="white")
        self.label_2.place(relx=0.45, rely=0.1)

        self.english_progress = ctk.CTkProgressBar(self.marks_frame, orientation='horizontal', mode="determinate", border_width=2, border_color='white', width=300, height=25)
        self.english_progress.place(relx=0.75, rely=0.2, anchor='center')
        self.english_progress.set(self.english / 100.0)
        self.label_3 = self.ctk.CTkLabel(self.marks_frame, text=f"{self.english}%", font=self.font, text_color="white")
        self.label_3.place(relx=0.45, rely=0.2)

        self.science_progress = ctk.CTkProgressBar(self.marks_frame, orientation='horizontal', mode="determinate", border_width=2, border_color='white', width=300, height=25)
        self.science_progress.place(relx=0.75, rely=0.3, anchor='center')
        self.science_progress.set(self.science / 100.0)
        self.label_4 = self.ctk.CTkLabel(self.marks_frame, text=f"{self.science}%", font=self.font, text_color="white")
        self.label_4.place(relx=0.45, rely=0.3)


        self.religion_progress = ctk.CTkProgressBar(self.marks_frame, orientation='horizontal', mode="determinate", border_width=2, border_color='white', width=300, height=25)
        self.religion_progress.place(relx=0.75, rely=0.4, anchor='center')
        self.religion_progress.set(self.religion / 100.0)
        self.label_5 = self.ctk.CTkLabel(self.marks_frame, text=f"{self.religion}%", font=self.font, text_color="white")
        self.label_5.place(relx=0.45, rely=0.4)
        
        
        self.wellbeing_progress = ctk.CTkProgressBar(self.marks_frame, orientation='horizontal', mode="determinate", border_width=2, border_color='white', width=300, height=25)
        self.wellbeing_progress.place(relx=0.75, rely=0.5, anchor='center')
        self.wellbeing_progress.set(self.wellbeing / 100.0)
        self.label_6 = self.ctk.CTkLabel(self.marks_frame, text=f"{self.wellbeing}%", font=self.font, text_color="white")
        self.label_6.place(relx=0.45, rely=0.5)

        self.ac_progress = ctk.CTkProgressBar(self.marks_frame, orientation='horizontal', mode="determinate", border_width=2, border_color='white', width=300, height=25)
        self.ac_progress.place(relx=0.75, rely=0.6, anchor='center')
        self.ac_progress.set(self.arts_culture / 100.0)
        self.label_7 = self.ctk.CTkLabel(self.marks_frame, text=f"{self.arts_culture}%", font=self.font, text_color="white")
        self.label_7.place(relx=0.45, rely=0.6)

        self.dt_progress = ctk.CTkProgressBar(self.marks_frame, orientation='horizontal', mode="determinate", border_width=2, border_color='white', width=300, height=25)
        self.dt_progress.place(relx=0.75, rely=0.7, anchor='center')
        self.dt_progress.set(self.digital_tech / 100.0)
        self.label_8 = self.ctk.CTkLabel(self.marks_frame, text=f"{self.digital_tech}%", font=self.font, text_color="white")
        self.label_8.place(relx=0.45, rely=0.7)

        self.ll_progress = ctk.CTkProgressBar(self.marks_frame, orientation='horizontal', mode="determinate", border_width=2, border_color='white', width=300, height=25)
        self.ll_progress.place(relx=0.75, rely=0.8, anchor='center')
        self.ll_progress.set(self.life_livelihood / 100.0)
        self.label_9 = self.ctk.CTkLabel(self.marks_frame, text=f"{self.life_livelihood}%", font=self.font, text_color="white")
        self.label_9.place(relx=0.45, rely=0.8)
        
        self.hss_progress = ctk.CTkProgressBar(self.marks_frame, orientation='horizontal', mode="determinate", border_width=2, border_color='white', width=300, height=25)
        self.hss_progress.place(relx=0.75, rely=0.9, anchor='center')
        self.hss_progress.set(self.history_social_science / 100.0)
        self.label_10 = self.ctk.CTkLabel(self.marks_frame, text=f"{self.history_social_science}%", font=self.font, text_color="white")
        self.label_10.place(relx=0.45, rely=0.9)


    def backToMain(self):
        """
        Handles the back button action. Destroys the current main frame and navigates back to the main menu.
        """
        self.main_frame.destroy()
        self.master.create_main_frame()
        

        