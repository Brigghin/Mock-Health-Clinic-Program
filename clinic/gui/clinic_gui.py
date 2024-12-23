import sys
from PyQt6.QtCore import Qt
from clinic.exception.invalid_login_exception import InvalidLoginException
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QStackedLayout
from clinic.gui.main_menu_gui import MainMenuGUI
from clinic.gui.main_menu_elements.add_new_patient_gui import AddNewPatientGUI
from clinic.gui.main_menu_elements.search_patient_gui import SearchPatientGUI
from clinic.gui.main_menu_elements.delete_patient_gui import DeletePatientGUI
from clinic.gui.main_menu_elements.retrieve_patients_gui import RetrievePatientsGUI
from clinic.gui.main_menu_elements.list_patients_gui import ListPatientsGUI
from clinic.gui.main_menu_elements.update_patient_gui import UpdatePatientGUI
from clinic.gui.main_menu_elements.get_phn_gui import GetPHNGUI
from clinic.gui.appointment_gui import AppointmentGUI
from clinic.gui.appointment_menu_elements.add_note_gui import AddNoteGUI
from clinic.gui.appointment_menu_elements.change_note_gui import ChangeNoteGUI
from clinic.gui.appointment_menu_elements.list_notes_gui import ListNotesGUI
from clinic.gui.appointment_menu_elements.remove_note_gui import RemoveNoteGUI
from clinic.gui.appointment_menu_elements.retrieve_notes_gui import RetrieveNotesGUI
from clinic.controller import Controller 

class ClinicGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.controller = Controller(autosave=True)
        self.setWindowTitle("MEDICAL CLINIC SYSTEM")
        self.stackedLayout = QStackedLayout()
        
        # Initializing all of the screens
        self.list_patients_gui = ListPatientsGUI(self.controller, self.stackedLayout)
        self.main_menu_gui = MainMenuGUI(self.controller, self.stackedLayout, self.list_patients_gui)
        self.add_new_patient_gui = AddNewPatientGUI(self.controller, self.stackedLayout)
        self.search_patient_gui = SearchPatientGUI(self.controller, self.stackedLayout)
        self.delete_patient_gui = DeletePatientGUI(self.controller, self.stackedLayout)
        self.retrieve_patients_gui = RetrievePatientsGUI(self.controller, self.stackedLayout)
        self.update_patient_gui = UpdatePatientGUI(self.controller, self.stackedLayout)
        self.list_notes_gui = ListNotesGUI(self.controller, self.stackedLayout)
        self.appointment_menu_gui = AppointmentGUI(self.controller, self.stackedLayout, self)
        self.get_phn_gui = GetPHNGUI(self.controller, self.stackedLayout, self)
        self.add_note_gui = AddNoteGUI(self.controller, self.stackedLayout)
        self.change_note_gui = ChangeNoteGUI(self.controller, self.stackedLayout)
        self.remove_note_gui = RemoveNoteGUI(self.controller, self.stackedLayout)
        self.retrieve_note_gui = RetrieveNotesGUI(self.controller, self.stackedLayout)
        
        # Add the screens to the main layout
        self.stackedLayout.addWidget(self.home_screen()) # 0
        self.stackedLayout.addWidget(self.login_screen()) # 1
        
        self.stackedLayout.addWidget(self.main_menu_gui.main_menu()) # 2
        self.stackedLayout.addWidget(self.add_new_patient_gui.add_new_screen()) # 3
        self.stackedLayout.addWidget(self.search_patient_gui.search_patient_screen()) # 4
        self.stackedLayout.addWidget(self.delete_patient_gui.delete_patient_screen()) # 5
        self.stackedLayout.addWidget(self.retrieve_patients_gui.retrieve_patients_screen()) # 6
        self.stackedLayout.addWidget(self.list_patients_gui.list_Patients_screen()) # 7
        self.stackedLayout.addWidget(self.update_patient_gui.update_patient_screen()) # 8
        
        self.stackedLayout.addWidget(self.get_phn_gui.get_PHN_screen()) # 9
        self.stackedLayout.addWidget(self.appointment_menu_gui.appointment_menu_screen()) # 10
        self.stackedLayout.addWidget(self.add_note_gui.add_note_screen()) # 11
        self.stackedLayout.addWidget(self.change_note_gui.change_note_screen()) # 12
        self.stackedLayout.addWidget(self.list_notes_gui.list_notes_screen()) # 13
        self.stackedLayout.addWidget(self.remove_note_gui.remove_note_screen()) # 14
        self.stackedLayout.addWidget(self.retrieve_note_gui.retrieve_notes_screen()) # 15
 
        # Setting up the main widget for the screen and setting the main layout to it
        widget = QWidget()
        widget.setLayout(self.stackedLayout)
        self.setCentralWidget(widget)
    
    # Opening Screen for logging in or quitting
    def home_screen(self):
        homeScreenWidget = QWidget()
        homeScreenOptions = QVBoxLayout()

        welcomeText = QLabel("Welcome to the Medical Clinic System.")
        welcomeText.setAlignment(Qt.AlignmentFlag.AlignCenter) # Center aligning the text
 
        loginButton = QPushButton("Login")
        loginButton.clicked.connect(self.login_button_click)

        quitButton = QPushButton("Quit")
        quitButton.clicked.connect(self.quit_button_click)

        homeScreenOptions.addWidget(welcomeText)
        homeScreenOptions.addWidget(loginButton)
        homeScreenOptions.addWidget(quitButton)

        homeScreenWidget.setLayout(homeScreenOptions)
        return homeScreenWidget

    # Function to move to the signin screen
    def login_button_click(self):
        self.stackedLayout.setCurrentIndex(1)
    
    #Close the app
    def quit_button_click(self):
        sys.exit()

    # Screen for inputing username and pass
    def login_screen(self):

        loginScreenWidget = QWidget()
        loginScreenLayout = QVBoxLayout()

        welcomeText = QLabel("Please enter your details to continue.")  
        welcomeText.setAlignment(Qt.AlignmentFlag.AlignCenter)

        userInput = QLineEdit(self)
        userInput.setPlaceholderText(" Username")
        
        passInput = QLineEdit(self)
        passInput.setPlaceholderText(" Password")
        passInput.setEchoMode(QLineEdit.EchoMode.Password)

        buttonOptionLayout = QHBoxLayout()

        backButton = QPushButton("Back")
        backButton.clicked.connect(lambda: self.back_button_click(userInput, passInput)) #Lambda function so function
                                                                                       #is not called when connecting
        enterButton = QPushButton("Enter")
        enterButton.clicked.connect(lambda: self.enter_button_click(userInput, passInput))

        buttonOptionLayout.addWidget(backButton)
        buttonOptionLayout.addWidget(enterButton)

        loginScreenLayout.addWidget(welcomeText)
        loginScreenLayout.addWidget(userInput)
        loginScreenLayout.addWidget(passInput)
        loginScreenLayout.addLayout(buttonOptionLayout)

        loginScreenWidget.setLayout(loginScreenLayout)
        return loginScreenWidget
    #Go back to the home screen
    def back_button_click(self, userInput, passInput):
        self.stackedLayout.setCurrentIndex(0)
        userInput.clear() #Resetting text for next time user enters login screen
        passInput.clear()
    #enter the current user and pass fields
    def enter_button_click(self, userInput, passInput):
        try:
           username = userInput.text()
           password = passInput.text()
           self.controller.login(username, password)
           userInput.clear()
           passInput.clear()
           self.stackedLayout.setCurrentIndex(2)
        except InvalidLoginException:
           QMessageBox.warning(self, "Invalid Login", "Please try again.")
           userInput.clear()
           passInput.clear()


#Setting up the main window
def main():
    app = QApplication(sys.argv)
    window = ClinicGUI()
    window.setMinimumSize(600, 500)
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
