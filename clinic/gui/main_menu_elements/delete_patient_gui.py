
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout, QHBoxLayout

class DeletePatientGUI(QWidget):

    def __init__(self, controller, stackedLayout):
        super().__init__()
        self.controller = controller
        self.stackedLayout = stackedLayout

    def delete_patient_screen(self):
        deletePatientScreenWidget = QWidget()
        deletePatientScreenLayout = QVBoxLayout()
        
        buttonOptionLayout = QHBoxLayout()

        deletePatientLabel = QLabel("Please enter the PHN of the patient you want to delete.") 
        deletePatientLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        PHNInput = QLineEdit(self)
        PHNInput.setPlaceholderText("PHN")

        backButton = QPushButton("Back")
        backButton.clicked.connect(lambda: self.back_button_click(PHNInput))

        enterButton = QPushButton("Enter")
        enterButton.clicked.connect(lambda: self.enter_button_click(PHNInput))

        buttonOptionLayout.addWidget(backButton)
        buttonOptionLayout.addWidget(enterButton)

        deletePatientScreenLayout.addWidget(deletePatientLabel)
        deletePatientScreenLayout.addWidget(PHNInput)
        deletePatientScreenLayout.addLayout(buttonOptionLayout)

        deletePatientScreenWidget.setLayout(deletePatientScreenLayout)
        return deletePatientScreenWidget
    #Goes back to the main menu
    def back_button_click(self, PHNInput):
        PHNInput.clear()
        self.stackedLayout.setCurrentIndex(2)

    #Checks if the currenly inputed PHN is a valid user, and if so if the user wants to delete them
    def enter_button_click(self, PHNInput):
        PHN = PHNInput.text().strip()
        if not PHN or not PHN.isnumeric():
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid PHN.")
            PHNInput.clear()
            return

        patient = self.controller.search_patient(int(PHN))

        if patient is None:
            QMessageBox.warning(self, "Invalid PHN", "No patient exists with this PHN.")
        else:
            #custom message box to double check that specific PHN matches the intended patient
            patientString = f"\n\nPHN: {patient.phn}\nName: {patient.name}\nBirthday: {patient.birth_date}\nPhone Number: {patient.phone}\nEmail: {patient.email}\nAddress: {patient.address}"
            confirmationBox = QMessageBox.question(self, "Confirm", "Are you sure you want to delete this patient?" + patientString)

            if confirmationBox == QMessageBox.StandardButton.Yes:
                patient.record.clear_notes()
                self.controller.delete_patient(int(PHN))
                self.stackedLayout.setCurrentIndex(2)
                QMessageBox.information(self, "Success", "Patient deleted.")
        PHNInput.clear()

