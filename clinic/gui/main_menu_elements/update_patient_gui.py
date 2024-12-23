from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout, QHBoxLayout

class UpdatePatientGUI(QWidget):

    def __init__(self, controller, stackedLayout):
        super().__init__()
        self.controller = controller
        self.stackedLayout = stackedLayout

    def update_patient_screen(self):
        updateWidget = QWidget()
        updateLayout = QVBoxLayout()

        buttonOptionLayout = QHBoxLayout()

        updateLable = QLabel("Please enter a patient's PHN to update their info.")
        updateLable.setAlignment(Qt.AlignmentFlag.AlignCenter)
        currentPHNInput = QLineEdit(self)
        currentPHNInput.setPlaceholderText("Current PHN")
        newPHNInput = QLineEdit(self)
        newPHNInput.setPlaceholderText("PHN")
        nameInput = QLineEdit(self)
        nameInput.setPlaceholderText("Patient Name")
        birthDateInput = QLineEdit(self)
        birthDateInput.setPlaceholderText("Patient Birthday")
        phoneInput = QLineEdit(self)
        phoneInput.setPlaceholderText("Patient Phone Number")
        emailInput = QLineEdit(self)
        emailInput.setPlaceholderText("Patient Email")
        addressInput = QLineEdit(self)
        addressInput.setPlaceholderText("Patient Address")

        newPHNInput.hide()
        nameInput.hide()
        birthDateInput.hide()
        phoneInput.hide()
        emailInput.hide()
        addressInput.hide()

        backButton = QPushButton("Back")
        backButton.clicked.connect(lambda: self.back_button_click(saveButton, searchButton, clearButton, currentPHNInput, newPHNInput, nameInput, birthDateInput, phoneInput, emailInput, addressInput))

        clearButton = QPushButton("Clear")
        clearButton.hide()
        clearButton.clicked.connect(lambda: self.clear_button_click(saveButton, searchButton, clearButton, currentPHNInput, newPHNInput, nameInput, birthDateInput, phoneInput, emailInput, addressInput))

        saveButton = QPushButton("Save")
        saveButton.hide()
        saveButton.clicked.connect(lambda: self.save_button_click(saveButton, searchButton, clearButton, currentPHNInput, newPHNInput, nameInput, birthDateInput, phoneInput, emailInput, addressInput))
 
        searchButton = QPushButton("Enter")
        searchButton.clicked.connect(lambda: self.search_button_click(saveButton, searchButton, clearButton, currentPHNInput, newPHNInput, nameInput, birthDateInput, phoneInput, emailInput, addressInput))

        buttonOptionLayout.addWidget(backButton)
        buttonOptionLayout.addWidget(clearButton)
        buttonOptionLayout.addWidget(saveButton)
        buttonOptionLayout.addWidget(searchButton)

        updateLayout.addWidget(updateLable)
        updateLayout.addWidget(currentPHNInput)
        updateLayout.addWidget(newPHNInput)
        updateLayout.addWidget(nameInput)
        updateLayout.addWidget(birthDateInput)
        updateLayout.addWidget(phoneInput)
        updateLayout.addWidget(emailInput)
        updateLayout.addWidget(addressInput)

        updateLayout.addLayout(buttonOptionLayout)
        updateWidget.setLayout(updateLayout)

        return updateWidget
    #Checks to see if the inputted PHN is a valid user and if so loads their info
    def search_button_click(self, saveButton, searchButton, clearButton, currentPHNInput, newPHNInput, nameInput, birthDateInput, phoneInput, emailInput, addressInput):
        PHN = currentPHNInput.text().strip()
        if not PHN or not PHN.isnumeric():
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid PHN.")
            currentPHNInput.clear()
            return

        patient = self.controller.search_patient(int(PHN))

        if patient is None:
            QMessageBox.warning(self, "Invalid PHN", "No patient with this PHN exists.")
            currentPHNInput.setText("")
        else:
            #Updating the buttons so save and clear only show when a patient is found, and search when
            #A patient has not yet been found
            saveButton.show()
            clearButton.show()
            searchButton.hide()
            
            currentPHNInput.setEnabled(False)
            newPHNInput.show()
            nameInput.show()
            birthDateInput.show()
            phoneInput.show()
            emailInput.show()
            addressInput.show()
            #Loading a patients current data into the text boxes to be edited by the user
            newPHNInput.setText(str(patient.phn))
            nameInput.setText(patient.name)
            birthDateInput.setText(patient.birth_date)
            phoneInput.setText(patient.phone)
            emailInput.setText(patient.email)
            addressInput.setText(patient.address)
    #Saves the users new info and overwrites what was there before
    def save_button_click(self, saveButton, searchButton, clearButton, currentPHNInput, newPHNInput, nameInput, birthDateInput, phoneInput, emailInput, addressInput):
        #updates the patients info in the controller and clears and hides all the update boxes
        PHN = newPHNInput.text().strip()
        if not PHN:
            QMessageBox.warning(self, "Invalid Input", "Please enter a PHN.")
            return

        self.controller.update_patient(int(currentPHNInput.text()), int(newPHNInput.text()), nameInput.text(), birthDateInput.text(), phoneInput.text(), emailInput.text(), addressInput.text())
        currentPHNInput.setText("")
        newPHNInput.setText("")
        nameInput.setText("")
        birthDateInput.setText("")
        phoneInput.setText("")
        emailInput.setText("")
        addressInput.setText("")
        
        currentPHNInput.setEnabled(True)
        newPHNInput.hide()
        nameInput.hide()
        birthDateInput.hide()
        phoneInput.hide()
        emailInput.hide()
        addressInput.hide()

        saveButton.hide()
        clearButton.hide()
        searchButton.show()
        
        self.stackedLayout.setCurrentIndex(2)
        QMessageBox.information(self, "Success", "Patient information updated.")

    #Clears the currenlty loaded user's info
    def clear_button_click(self, saveButton, searchButton, clearButton, currentPHNInput, newPHNInput, nameInput, birthDateInput, phoneInput, emailInput, addressInput):
        currentPHNInput.setText("")
        newPHNInput.setText("")
        nameInput.setText("")
        birthDateInput.setText("")
        phoneInput.setText("")
        emailInput.setText("")
        addressInput.setText("")

        currentPHNInput.setEnabled(True)
        newPHNInput.hide()
        nameInput.hide()
        birthDateInput.hide()
        phoneInput.hide()
        emailInput.hide()
        addressInput.hide()

        saveButton.hide()
        clearButton.hide()
        searchButton.show()
    #Goes back to the main menu
    def back_button_click(self, saveButton, searchButton, clearButton, currentPHNInput, newPHNInput, nameInput, birthDateInput, phoneInput, emailInput, addressInput):
        currentPHNInput.setText("")
        newPHNInput.setText("")
        nameInput.setText("")
        birthDateInput.setText("")
        phoneInput.setText("")
        emailInput.setText("")
        addressInput.setText("")

        currentPHNInput.setEnabled(True)
        newPHNInput.hide()
        nameInput.hide()
        birthDateInput.hide()
        phoneInput.hide()
        emailInput.hide()
        addressInput.hide()

        saveButton.hide()
        clearButton.hide()
        searchButton.show()

        self.stackedLayout.setCurrentIndex(2)
