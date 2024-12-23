from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout, QHBoxLayout 

class GetPHNGUI(QWidget):
    def __init__(self, controller, stackedLayout, mainWindow):
        super().__init__()
        self.controller = controller
        self.stackedLayout = stackedLayout
        self.mainWindow = mainWindow
        
    def get_PHN_screen(self):
        getPHNScreenWidget = QWidget()
        getPHNScreenLayout = QVBoxLayout()

        buttonOptionLayout = QHBoxLayout()
        
        patientLabel = QLabel("")
        patientLabel.hide()
        searchPatientLabel = QLabel("Please enter the PHN of the patient you want to start an appointment with.")
        searchPatientLabel.setAlignment(Qt.AlignmentFlag.AlignCenter) 
 
        PHNInput = QLineEdit(self)
        PHNInput.setPlaceholderText("PHN")

        backButton = QPushButton("Back")
        backButton.clicked.connect(lambda: self.back_button_click(PHNInput, patientLabel))

        enterButton = QPushButton("Enter")
        enterButton.clicked.connect(lambda: self.enter_button_click(PHNInput))

        buttonOptionLayout.addWidget(backButton)
        buttonOptionLayout.addWidget(enterButton)

        getPHNScreenLayout.addWidget(searchPatientLabel)
        getPHNScreenLayout.addWidget(PHNInput)
        getPHNScreenLayout.addLayout(buttonOptionLayout)
        getPHNScreenLayout.addWidget(patientLabel)

        getPHNScreenWidget.setLayout(getPHNScreenLayout)
        return getPHNScreenWidget
    #Goes back to the main menu
    def back_button_click(self, PHNInput, patientLabel):
        PHNInput.clear()
        patientLabel.setText("")
        patientLabel.hide()
        self.stackedLayout.setCurrentIndex(2)
    #checks the current PHN box input to see if the user exists
    def enter_button_click(self, PHNInput):
        PHN = PHNInput.text().strip()
        if not PHN or not PHN.isnumeric():
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid PHN.")
            PHNInput.clear()
            return

        patient = self.controller.search_patient(int(PHN))

        if patient is None:
            QMessageBox.warning(self, "Invalid PHN", "No patient with this PHN exists")
        else:
            patientString = f"\n\nPHN: {patient.phn}\nName: {patient.name}\nBirthday: {patient.birth_date}\nPhone Number: {patient.phone}\nEmail: {patient.email}\nAddress: {patient.address}"
            #Custom message box to handle checking if the specified PHN is to the intended patient
            found = QMessageBox()
            found.setText("Is this the patient you want to book an appointment with?" + patientString)
            found.setWindowTitle("Confirmation")
            found.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            x = found.exec()
            if x == QMessageBox.StandardButton.Yes:                
                # Set current_patient to the PHN
                self.controller.set_current_patient(int(PHN))
                self.mainWindow.setWindowTitle("MEDICAL CLINIC SYSTEM - APPOINTMENT MENU")
                self.stackedLayout.setCurrentIndex(10)
            else:
                found.close()

        PHNInput.clear()
