from functions import showCopyrightClaim, showErrorMessage, uploadImage, loadProfileImage
import json

class TeacherAccount:
    """
    The TeacherAccount class handles the creation and management of the teacher account interface.
    It provides functionalities to upload a profile picture, view teacher details, manage accessed classes,
    and evaluate students within these classes. The class interacts with JSON files to save and load data persistently.

    Attributes:
        master (tk.Tk): The main window or parent widget.
        ctk (module): CustomTkinter module used for custom widgets.
        button_font (font): Font used for the buttons.
        teacher_name (str): The name of the teacher.
        teacher_salary (str): The salary of the teacher.
        accessed_class (list): List of classes the teacher has access to.
        teacher_id (str): The unique ID of the teacher.
        font (tuple): Font used for labels.
        teacher_frame (CTkScrollableFrame): Main frame that holds all teacher account-related widgets.
        teacher_acc_frame (CTkFrame): Frame that holds teacher-specific widgets.
        profile_frame (CTkFrame): Frame for displaying the profile picture.
        profile_picture_label (CTkLabel): Label for the profile picture.
        upload_button (CTkButton): Button to upload a profile picture.
        back_button (CTkButton): Button to navigate back to the main menu.
        label_name (CTkLabel): Label to display the teacher's name.
        label_id (CTkLabel): Label to display the teacher's ID.
        label_salary (CTkLabel): Label to display the teacher's salary.
        label_accessed_class (CTkLabel): Label to display the classes the teacher has access to.

    Methods:
        __init__(self, master, ctk, button_font, teacher_name, teacher_salary, accessed_class, teacher_id): 
            Initializes the TeacherAccount class and sets up the GUI elements.
        backToMain(self): Destroys the current main frame and returns to the main menu.
        showAccessedClass(self): Displays accessed classes from 'classes.json'.
        addClassButton(self, class_name): Adds a button for each class in the main frame.
        openClass(self, c, filename='classes.json'): Opens a window to display and manage students in the selected class.
        onClosing(self): Closes the student display window.
        evaluateStudent(self, c): Opens a window to evaluate a student in the selected class.
        updateMark(self, c, roll, subject, mark): Updates the student's mark in the selected class.
    """

    def __init__(self, master, ctk, button_font, teacher_name, teacher_salary, accessed_class, teacher_id) -> None:

        """
        Initialize the TeacherAccount class.
        
        Args:
            master (tk.Tk): The main window or parent widget.
            ctk (module): CustomTkinter module used for custom widgets.
            button_font (font): Font used for the buttons.
            teacher_name (str): The name of the teacher.
            teacher_salary (str): The salary of the teacher.
            accessed_class (list): List of classes the teacher has access to.
            teacher_id (str): The unique ID of the teacher.
        """

        self.master = master
        self.ctk = ctk
        self.button_font = button_font
        self.teacher_name = teacher_name
        self.teacher_salary = teacher_salary
        self.accessed_class = accessed_class
        self.teacher_id = teacher_id

        self.font = ('Arial', 20, 'bold')

        # main frame 
        self.teacher_frame = self.ctk.CTkScrollableFrame(
            self.master,
            width=1200,
            height=600,
            orientation="vertical",
            border_width=2,
            border_color="white",
            corner_radius=4
        )
        self.teacher_frame.place(relx=0.5, rely=0.5, anchor='center')

        # copyright 
        showCopyrightClaim(self.ctk, self.master)

        # Create account frame
        self.teacher_acc_frame = self.ctk.CTkFrame(
            self.teacher_frame,
            width=350,
            height=700,
            fg_color='black',
        )
        self.teacher_acc_frame.pack(side='left', fill='y')

        # Add profile picture frame
        self.profile_frame = self.ctk.CTkFrame(self.teacher_acc_frame, width=150, height=150)
        self.profile_frame.place(relx=0.2, rely=0.01)

        # Placeholder for profile picture
        self.profile_picture_label = self.ctk.CTkLabel(self.profile_frame, text="No Image", font=('Arial', 20, 'bold'))
        self.profile_picture_label.place(relx=0.05, rely=0.01)

        # Load profile image if exists
        # self.load_teacher_profile_image(self.teacher_id) 
 
    # def load_teacher_profile_image(self, teacher_id):
    #     try:
    #         with open("teachers.json", 'r') as file:
    #             data = json.load(file)
    #             teacher = next((t for t in data["teachers"] if t["id"] == teacher_id), None)
    #             if teacher:
    #                 profile_pic_path = teacher.get("profile_pic")
    #                 if profile_pic_path:
    #                     loadProfileImage(profile_pic_path, self.profile_picture_label)
    #     except (FileNotFoundError, json.JSONDecodeError) as e:
    #         print(f"Error loading profile image: {e}")

        # Add button to upload photo
        self.upload_button = self.ctk.CTkButton(self.teacher_acc_frame, font=self.button_font, text="Upload Photo", width=150, height=35, text_color='white', command=lambda: uploadImage(self, filename='admin_id.json'))
        self.upload_button.place(relx=0.2, rely=0.25)

        # back button 
        self.back_button = self.ctk.CTkButton(
            self.teacher_acc_frame,
            text="Back",
            text_color="white",
            font=self.button_font,
            width=150,
            height=35,
            fg_color="red",  # Ensure visible color
            command=self.backToMain
        )
        self.back_button.place(relx=0.2, rely=0.35)


        ##############################
        # show teacher info
        ##############################
        self.label_name = self.ctk.CTkLabel(self.teacher_acc_frame, text=f"Name: {self.teacher_name}", font=self.font, text_color="white", fg_color="#2B2B2B", width=115, height=30, corner_radius=20)
        self.label_name.place(relx=0.2, rely=0.45)

        self.label_id = self.ctk.CTkLabel(self.teacher_acc_frame, text=f"ID: {self.teacher_id}", font=self.font, text_color="white", fg_color="#2B2B2B", width=115, height=30, corner_radius=20)
        self.label_id.place(relx=0.2, rely=0.5)

        self.label_salary = self.ctk.CTkLabel(self.teacher_acc_frame, text=f"Salary: {self.teacher_salary}", font=self.font, text_color="white", fg_color="#2B2B2B", width=115, height=30, corner_radius=20)
        self.label_salary.place(relx=0.2, rely=0.55)

        self.label_accessed_class = self.ctk.CTkLabel(self.teacher_acc_frame, text=f"Access: {','.join(map(str, self.accessed_class))}", font=self.font, text_color="white", fg_color="#2B2B2B", width=115, height=30, corner_radius=20)
        self.label_accessed_class.place(relx=0.2, rely=0.6)

        # show accessed class 
        self.showAccessedClass()

    def backToMain(self):
        '''
        Destroys the current window and returns to the main menu
        '''
        for widget in self.teacher_frame.winfo_children():
            widget.destroy()

        self.master.create_main_frame()

    def showAccessedClass(self):
        """
        Reads the classes.json file and displays buttons for the classes
        the teacher has access to.
        """
        try:
            with open("classes.json", 'r') as f:
                _data = json.load(f)
                class_list = _data.get("classes",[])

                for class_data in class_list:
                    if class_data["class"] in self.accessed_class:
                        self.addClassButton(class_data["class"])
        except FileNotFoundError:
            showErrorMessage(message="Fatal Error!\nFile not found\nPerhaps it was deleted or restart the app")
        except json.JSONDecodeError:
            showErrorMessage(message="Error decoding classes\nRestart the app or pc")

    def addClassButton(self, class_name):
        """
        Adds a button for each class in the main frame.

        Args:
            class_name (str): The name of the class.
        """
        self.classes = self.ctk.CTkButton(
            self.teacher_frame,
            text=f"Class {class_name}",
            text_color="white",
            font=self.button_font,
            width=700,
            height=100,
            command=lambda c=class_name: self.openClass(c) #open class
        )
        self.classes.pack(padx=10, pady=10)

    
    def openClass(self, c, filename='classes.json'):
        """
        Opens a window to display and see students in the selected class.

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

        self.display_frame = self.ctk.CTkScrollableFrame(
            self.window,
            width=1000,
            height=600,
            border_width=2,
            border_color="white",
            orientation='vertical'
        )
        self.display_frame.place(relx=0.5, rely=0.5, anchor='center')

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
                student_info = f"{student['Name']}      Roll: {student['Roll']}     ID:{student["ID"]}"
                show_student = self.ctk.CTkButton(
                    self.display_frame,
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
            showErrorMessage(message="classes.json not found.")
        except json.JSONDecodeError:
            showErrorMessage(message="Error decoding JSON from classes.json.")
        except KeyError as e:
            showErrorMessage(message=f"Missing key in JSON data: {e}")

        
         # give marks to student
        self.mark_button = self.ctk.CTkButton(self.window, font=self.button_font, text="Evaluate", width=150, height=35, text_color='white', command = lambda: self.evaluateStudent(c))
        self.mark_button.pack(side='bottom', pady=10)

        # Bind the closing event to the on_closing function
        self.window.protocol("WM_DELETE_WINDOW", self.onClosing)
        self.window.mainloop()

    def onClosing(self):
        self.display_frame.destroy()
        self.window.destroy()


    def evaluateStudent(self, c):
        """
        Opens a window to evaluate a student in the selected class.

        Args:
            c (str): The name of the class.
        """
        _width = 450
        _height = 300

        self.screen = self.ctk.CTk()
        self.screen.geometry(f"{_width}x{_height}")
        self.screen.title(f"Evaluate for class{c}")

        _roll_label = self.ctk.CTkLabel(self.screen, text="Roll:  ", font=self.font, text_color="white")
        _roll_label.place(relx=0.1, rely=0.1)
        _subject_label = self.ctk.CTkLabel(self.screen, text="Subject: ", font=self.font, text_color="white") 
        _subject_label.place(relx=0.1, rely=0.3)
        _mark_label = self.ctk.CTkLabel(self.screen, text="Mark: ", font=self.font, text_color="white")
        _mark_label.place(relx=0.1, rely=0.5)

        _roll_entry = self.ctk.CTkEntry(self.screen, width=250, font=self.button_font, placeholder_text = "Enter student's roll")
        _roll_entry.place(relx=0.3, rely=0.1)
        _subject_entry = self.ctk.CTkEntry(self.screen, width=250, font=self.button_font, placeholder_text = "Enter Subject Name")
        _subject_entry.place(relx=0.3, rely=0.3)
        _mark_entry = self.ctk.CTkEntry(self.screen, width=250, font=self.button_font, placeholder_text = "Give appropriate marks")
        _mark_entry.place(relx=0.3, rely=0.5)

        _confirm_button = self.ctk.CTkButton(self.screen, font=self.button_font, text="Confirm", width=150, height=35, text_color='white', command=lambda: self.updateMark(c=c, roll=_roll_entry.get(), subject=_subject_entry.get(), mark=_mark_entry.get()))
        _confirm_button.place(relx=0.5, rely=0.7, anchor='center')

        self.screen.mainloop()

    def updateMark(self, c, roll, subject, mark):
        """
        Updates the student's mark in the selected class.

        Args:
            c (str): The name of the class.
            roll (str): The roll number of the student.
            subject (str): The subject for which the mark is being updated.
            mark (str): The mark to be updated.
        """
        _filename = "classes.json"
        try:
            with open(_filename , 'r') as f:
                data = json.load(f)

            _class = next((cls for cls in data['classes'] if cls['class'] == c), None)
            if not _class:
                showErrorMessage(message=f"Class {c} not found")
                raise ValueError(f"Class {c} not found")

            _student = next((student for student in _class['students'] if student['Roll'] == roll), None)
            if not _student:
                showErrorMessage(message=f"Roll: {roll} not found")
                raise ValueError(f"Roll: {roll} not found")

            if subject not in _student['Marks']:
                showErrorMessage(message=f"{subject} not found\nWrite subject name in Pascal case")
                raise ValueError(f"{subject} not found")
                
            # increment marks of specific subject
            _student['Marks'][subject] += int(mark)

            # save the updated data back to the file 
            with open(_filename, 'w') as f:
                json.dump(data, f, indent=4)
            self.screen.destroy()

        except Exception as e:
            showErrorMessage(message=f"something went wrong\n{e}")
            self.screen.destroy()


        

