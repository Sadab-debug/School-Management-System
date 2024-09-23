from functions import showCopyrightClaim, showErrorMessage
from student_account import StudentAccount
import json


class StudentLogin:

    """
    The StudentLogin class handles the creation and management of the student login interface.
    It provides functionalities for students to log in by entering their ID and has a button
    to navigate back to the main menu.

    Attributes:
        master (tk.Tk): The main window or parent widget.
        ctk (module): CustomTkinter module used for custom widgets.
        button_font (font): Font used for the buttons.
        login_frame (CTkFrame): Frame that holds all login-related widgets.
        header_label (CTkLabel): Label for the header text.
        id_label (CTkLabel): Label for the ID entry.
        id_entry (CTkEntry): Entry widget for the student ID.
        back_button (CTkButton): Button to navigate back to the main menu.
        login_button (CTkButton): Button to log in as a student.
        class_label (CTkLabel): Label for the class.
        class_entry (CTkEntry): Entry for class name.
        class_name (str): Retrieves name of class from class_entry.
        id_name (str): Retrieves ID number from id_entry.

    Methods:
        __init__(self, master, ctk, buttonFont): Initializes the StudentLogin class and sets up the GUI elements.
        back_to_main(self): Destroys the current login frame and returns to the main menu.
        openStudentAccount(self, student_name, student_id, student_roll, bangla_marks, english_marks, math_marks, 
                           science_marks, life_and_livelihood_marks, digital_technology_marks, 
                           history_and_social_science_marks, religion_marks, wellbeing_marks, arts_and_culture_marks, 
                           guardian, age, phone, class_name): Destroys the current login frame and opens StudentAccount.
        authenticateStudentLogin(self): Authenticates student login by checking the ID against stored data.
    """


    def __init__(self, master, ctk, buttonFont):
        """
        Initializes the StudentLogin class. Sets up the login frame, header, ID entry, and buttons.

        Args:
            master (tk.Tk): The main window or parent widget.
            ctk (module): CustomTkinter module used for custom widgets.
            buttonFont (font): Font used for the buttons.
        """
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
            text = "Welcome to Our School\nLogin as a Student",
            font=('Arial', 50, 'bold'),
            text_color = "white",
        )
        self.header_label.place(relx=0.5, rely=0, anchor="n", y=10)

        # label class
        self.class_label = self.ctk.CTkLabel(
            self.login_frame,
            text = "Class:",
            text_color = 'white',
            font=self.button_font
        )
        self.class_label.place(relx=0.3, rely=0.3)

        # class entry 
        self.class_entry = self.ctk.CTkEntry(
            self.login_frame,
            width = 250,
            font = self.button_font,
            placeholder_text = "Enter class name"
        )
        self.class_entry.place(relx=0.4, rely=0.3)


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
            placeholder_text = "Enter ID no."
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
            command=self.authenticateStudentLogin
        )
        self.login_button.place(relx=0.6, rely=0.6)


    def back_to_main(self):
        '''
        Handles the back button function. Destroys the current window and get back to the main menu
        '''
        self.login_frame.destroy()
        self.master.create_main_frame()

    def openstudentAccount(self, student_name, student_id, student_roll, bangla_marks, english_marks, math_marks, science_marks, life_and_livelihood_marks, digital_technology_marks, history_and_social_science_marks, religion_marks, wellbeing_marks, arts_and_culture_marks, guardian, age, phone, class_name):

        """
        Opens the student account interface by destroying the current login frame and initializing the StudentAccount class.

        Args:
            student_name (str): The name of the student.
            student_id (str): The ID of the student.
            student_roll (str): The roll number of the student.
            bangla_marks (str): Marks in Bangla.
            english_marks (str): Marks in English.
            math_marks (str): Marks in Math.
            science_marks (str): Marks in Science.
            life_and_livelihood_marks (str): Marks in Life and Livelihood.
            digital_technology_marks (str): Marks in Digital Technology.
            history_and_social_science_marks (str): Marks in History and Social Science.
            religion_marks (str): Marks in Religion.
            wellbeing_marks (str): Marks in Wellbeing.
            arts_and_culture_marks (str): Marks in Arts and Culture.
            guardian (str): Guardian's name.
            age (str): Age of the student.
            phone (str): Phone number.
            class_name (str): Name of the class.
        """

        self.student_name = student_name
        self.student_id = student_id
        self.student_roll = student_roll
        self.class_name = class_name

        self.bangla_marks = bangla_marks
        self.english_marks = english_marks
        self.math_marks = math_marks
        self.science_marks = science_marks
        self.LL_marks = life_and_livelihood_marks
        self.DT_marks = digital_technology_marks
        self.HSS_marks = history_and_social_science_marks
        self.religion_marks = religion_marks
        self.WB_marks = wellbeing_marks
        self.AC_marks = arts_and_culture_marks

        self.age = age
        self.guardian = guardian
        self.phone = phone

        self.login_frame.destroy()
        StudentAccount(self.master, self.ctk, self.button_font, student_name, student_id, student_roll, bangla_marks, english_marks, math_marks, science_marks, life_and_livelihood_marks, digital_technology_marks, history_and_social_science_marks, religion_marks,wellbeing_marks, arts_and_culture_marks, age, guardian, phone, class_name)


    def authenticateStudentLogin(self):
        """
        Authenticates the student login by checking the entered ID and class against stored data.
        """
        class_name = self.class_entry.get()
        id_num = self.id_entry.get()

        try:
            with open('classes.json', 'r') as f:
                data = json.load(f)

                # Find the class
                class_data = next((cls for cls in data['classes'] if cls['class'] == class_name), None)
                if not class_data:
                    showErrorMessage(f"Class {class_name} doesn't exist")
                    return 

                # Find the student
                student_data = next((student for student in class_data['students'] if student['ID'] == id_num), None)
                if not student_data:
                    showErrorMessage(f"ID {id_num} not found")
                    return 

                # Extract student data into variables
                student_name = student_data['Name']
                student_id = student_data['ID']
                student_roll = student_data['Roll']
                student_marks = student_data['Marks']
                student_other_info = student_data['OtherInfo']

                # Extract individual marks from the marks dictionary
                bangla_marks = student_marks.get('Bangla', 'N/A')
                english_marks = student_marks.get('English', 'N/A')
                math_marks = student_marks.get('Math', 'N/A')
                science_marks = student_marks.get('Science', 'N/A')
                life_and_livelihood_marks = student_marks.get('Life and Livelihood', 'N/A')
                digital_technology_marks = student_marks.get('Digital Technology', 'N/A')
                history_and_social_science_marks = student_marks.get('History and Social Science', 'N/A')
                religion_marks = student_marks.get('Religion', 'N/A')
                wellbeing_marks = student_marks.get('Wellbeing', 'N/A')
                arts_and_culture_marks = student_marks.get('Arts and Culture', 'N/A')

                # Extract individual marks from the marks dictionary
                guardian = student_other_info.get('Guardian')
                phone = student_other_info.get('Phone Number')
                age = student_other_info.get('Age')

                # Call the function with extracted variables
                self.openstudentAccount(
                    student_name, student_id, student_roll, bangla_marks, english_marks, math_marks, science_marks,
                    life_and_livelihood_marks, digital_technology_marks, history_and_social_science_marks, religion_marks,
                    wellbeing_marks, arts_and_culture_marks, guardian, age, phone, class_name
                )

        except FileNotFoundError:
            showErrorMessage("File doesn't exist")
        except json.JSONDecodeError:
            showErrorMessage("Error reading the JSON file")



            
            

        