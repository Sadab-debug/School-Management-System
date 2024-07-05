from functions import showCopyrightClaim, showErrorMessage, uploadImage, loadProfileImage
import json

class TeacherAccount:
    def __init__(self, master, ctk, button_font, teacher_name, teacher_salary, accessed_class, teacher_id) -> None:
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
            width = 1200,
            height = 600,
            orientation = "vertical",
            border_width = 2,
            border_color = "white",
            corner_radius = 4
        )
        self.teacher_frame.place(relx = 0.5, rely = 0.5, anchor = 'center')

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
        # self.window.destroy()
        self.teacher_acc_frame.destroy()
        self.teacher_frame.destroy()
        self.master.create_main_frame()




    def showAccessedClass(self):
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
                student_info = f"{student['Name']}      Roll: {student['Roll']}"
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
        self.mark_button = self.ctk.CTkButton(self.window, font=self.button_font, text="Evaluate", width=150, height=35, text_color='white')
        self.mark_button.pack(side='bottom', pady=10)

        # Bind the closing event to the on_closing function
        self.window.protocol("WM_DELETE_WINDOW", self.onClosing)
        self.window.mainloop()

    def onClosing(self):
        self.display_frame.destroy()
        self.window.destroy()


