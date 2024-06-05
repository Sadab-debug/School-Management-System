from functions import uploadImage
from PIL import Image, ImageTk
import json

class AdminAccount:
    def __init__(self, master, ctk) -> None:
        self.master = master
        self.ctk = ctk

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
        self.upload_button = self.ctk.CTkButton(self.account_frame, text="Upload Photo", width=150, height=35, text_color='white', command=lambda: uploadImage(self))
        self.upload_button.place(relx=0.2, rely=0.25)

    def loadProfileImage(self):
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


        