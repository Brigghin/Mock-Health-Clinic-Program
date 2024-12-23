from PyQt6.QtCore import Qt
from clinic.exception.illegal_operation_exception import IllegalOperationException
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout, QHBoxLayout

class AddNewPatientGUI(QWidget):

    def __init__(self, controller, stackedLayout):
        super().__init__()
        self.controller = controller
        self.stackedLayout = stackedLayout
    
    def add_new_screen(self):
        addNewWidget = QWidget()
        addNewLayout = QVBoxLayout()

        buttonOptionLayout = QHBoxLayout()
      
        #Inputs for all of a patients information
        addNewLable = QLabel("Please enter the new patient's information.")
        addNewLable.setAlignment(Qt.AlignmentFlag.AlignCenter)
        PHNInput = QLineEdit(self)
        PHNInput.setPlaceholderText("PHN")
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

        backButton = QPushButton("Back")
        backButton.clicked.connect(lambda: self.back_button_click(PHNInput, nameInput, birthDateInput, phoneInput, emailInput, addressInput))

        enterButton = QPushButton("Enter")
        enterButton.clicked.connect(lambda: self.enter_button_click(PHNInput, nameInput, birthDateInput, phoneInput, emailInput, addressInput))

        buttonOptionLayout.addWidget(backButton)
        buttonOptionLayout.addWidget(enterButton)

        addNewLayout.addWidget(addNewLable)
        addNewLayout.addWidget(PHNInput)
        addNewLayout.addWidget(nameInput)
        addNewLayout.addWidget(birthDateInput)
        addNewLayout.addWidget(phoneInput)
        addNewLayout.addWidget(emailInput)
        addNewLayout.addWidget(addressInput)

        addNewLayout.addLayout(buttonOptionLayout)

        addNewWidget.setLayout(addNewLayout)
        return addNewWidget
    #Goes back to the main menu
    def back_button_click(self, PHNInput, nameInput, birthDateInput, phoneInput, emailInput, addressInput):
        #Resetting the test boxes
        PHNInput.clear()
        nameInput.clear()
        birthDateInput.clear()
        phoneInput.clear()
        emailInput.clear()
        addressInput.clear()
        self.stackedLayout.setCurrentIndex(2)       
    #Enters the currently inputed fields for a new user
    def enter_button_click(self, PHNInput, nameInput, birthDateInput, phoneInput, emailInput, addressInput):
        PHN = PHNInput.text().strip()
        if not PHN or not PHN.isnumeric():
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid PHN.")
            PHNInput.clear()
            return
        #Getting user input and storing
        PHN = int(PHNInput.text())
        name = nameInput.text()
        birthDate = birthDateInput.text()
        phone = phoneInput.text()
        if phone and not phone.isnumeric():
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid phone number.")
            phoneInput.clear()
            return
        email = emailInput.text()
        address = addressInput.text()
         
        try:
            #Creating a new patient with inputed info
            self.controller.create_patient(PHN, name, birthDate, phone, email, address)
            self.stackedLayout.setCurrentIndex(2)
            QMessageBox.information(self, "Success", "Patient has been created.")

        except IllegalOperationException:
            QMessageBox.warning(self, "Duplicate PHN", "A patient with that PHN already exists.")

        PHNInput.clear()
        nameInput.clear()
        birthDateInput.clear()
        phoneInput.clear()
        emailInput.clear()
        addressInput.clear()

