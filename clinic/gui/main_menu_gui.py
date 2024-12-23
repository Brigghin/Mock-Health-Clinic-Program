from PyQt6.QtWidgets import QWidget, QPushButton, QGridLayout, QVBoxLayout

class MainMenuGUI(QWidget):
    def __init__(self, controller, stackedLayout, listPatientsGUI):
        super().__init__()
        self.controller = controller
        self.stackedLayout = stackedLayout #Importing the stackedLayout to navigate through main menu screens
        self.listPatientsGUI = listPatientsGUI #Importing list patients to deal with the way the screen is updated

    def main_menu(self):
        mainMenuWidget = QWidget()
        mainMenuLayout = QVBoxLayout()

        subMainMenuLayout = QGridLayout()

        addNewButton = QPushButton("Add a new patient")
        addNewButton.setCheckable(True)
        addNewButton.clicked.connect(self.add_new_button_click)
       
        searchPatientButton = QPushButton("Search patient by PHN")
        searchPatientButton.clicked.connect(self.search_patient_button_click)

        retrievePatientsButton = QPushButton("Retrieve patients by name")
        retrievePatientsButton.clicked.connect(self.retrieve_patients_button_click)

        changePatientButton = QPushButton("Update patient data")
        changePatientButton.clicked.connect(self.update_patient_button_click)

        removePatientButton = QPushButton("Remove patient")
        removePatientButton.clicked.connect(self.remove_patient_button_click)

        listAllButton = QPushButton("List all patients")
        listAllButton.clicked.connect(self.list_patients_button_click)
        
        startAppointmentButton = QPushButton("Start appointment with patient")
        startAppointmentButton.clicked.connect(self.start_appointment_button_click)

        logOutButton = QPushButton("Logout")
        logOutButton.clicked.connect(self.log_out_button_click)
   
        mainMenuLayout.addWidget(startAppointmentButton)
  
        #Adding all of the option buttons to a grid in the main menu
        subMainMenuLayout.addWidget(addNewButton, 0, 1)
        subMainMenuLayout.addWidget(searchPatientButton, 0, 2)
        subMainMenuLayout.addWidget(retrievePatientsButton, 1, 1)
        subMainMenuLayout.addWidget(changePatientButton, 1, 2)
        subMainMenuLayout.addWidget(removePatientButton, 2, 1)
        subMainMenuLayout.addWidget(listAllButton, 2, 2)
  
        mainMenuLayout.addLayout(subMainMenuLayout)

        mainMenuLayout.addWidget(logOutButton)

        mainMenuWidget.setLayout(mainMenuLayout)
        return mainMenuWidget

    #All of these functions navigate to the respective screens for the button in the stackedLayout
    def log_out_button_click(self):
        self.controller.logout()
        self.stackedLayout.setCurrentIndex(0)
       
    def add_new_button_click(self):
        self.stackedLayout.setCurrentIndex(3)

    def search_patient_button_click(self):
        self.stackedLayout.setCurrentIndex(4)

    def remove_patient_button_click(self):
        self.stackedLayout.setCurrentIndex(5)
  
    def retrieve_patients_button_click(self):
        self.stackedLayout.setCurrentIndex(6)

    def list_patients_button_click(self):
        self.listPatientsGUI.update_patient_table() #Sets the list patient table to update upon entry
        self.stackedLayout.setCurrentIndex(7)

    def update_patient_button_click(self):
        self.stackedLayout.setCurrentIndex(8)

    def start_appointment_button_click(self):
        self.stackedLayout.setCurrentIndex(9)
