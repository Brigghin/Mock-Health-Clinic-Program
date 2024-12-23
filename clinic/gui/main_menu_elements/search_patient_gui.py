from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QTableView, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QStandardItem, QStandardItemModel

class SearchPatientGUI(QWidget):

    def __init__(self, controller, stackedLayout):
        super().__init__()
        self.controller = controller
        self.stackedLayout = stackedLayout

    def search_patient_screen(self):
        searchPatientScreenWidget = QWidget()
        searchPatientScreenLayout = QVBoxLayout()

        buttonOptionWidget = QWidget()
        buttonOptionLayout = QHBoxLayout()
        
        patientTable = QTableView()
        patientModel = QStandardItemModel()
        patientTable.hide()
        searchPatientLabel = QLabel("Please enter the PHN of the patient you want to search for.")
        searchPatientLabel.setAlignment(Qt.AlignmentFlag.AlignCenter) 
 
        PHNInput = QLineEdit(self)
        PHNInput.setPlaceholderText("PHN")

        backButton = QPushButton("Back")
        backButton.clicked.connect(lambda: self.back_button_click(PHNInput, patientTable, patientModel))

        enterButton = QPushButton("Enter")
        enterButton.clicked.connect(lambda: self.enter_button_click(PHNInput, patientTable, patientModel))

        buttonOptionLayout.addWidget(backButton)
        buttonOptionLayout.addWidget(enterButton)

        searchPatientScreenLayout.addWidget(searchPatientLabel)
        searchPatientScreenLayout.addWidget(patientTable)
        searchPatientScreenLayout.addWidget(PHNInput)
        searchPatientScreenLayout.addLayout(buttonOptionLayout)

        searchPatientScreenWidget.setLayout(searchPatientScreenLayout)
        return searchPatientScreenWidget
    #Goes back to the main menu
    def back_button_click(self, PHNInput, patientTable, patientModel):
        PHNInput.clear()
        patientModel.clear()
        patientTable.hide()
        self.stackedLayout.setCurrentIndex(2)
    #Checks to see if the inputed PHN exists and loads the patient if so
    def enter_button_click(self, PHNInput, patientTable, patientModel):
        PHN = PHNInput.text().strip()
        if not PHN or not PHN.isnumeric():
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid PHN.")
            PHNInput.clear()
            return

        patient = self.controller.search_patient(int(PHN))

        if patient is None:
            QMessageBox.warning(self, "Invalid PHN", "No patient with this PHN exists")
        else:
            #If a patient is found shows the table and loads the patients info into it
            patientTable.show()
            patientInfo = [str(patient.phn), patient.name, patient.birth_date, patient.phone, patient.email, patient.address]
            patientModel.clear()
            patientModel.setHorizontalHeaderLabels(["PHN", "Name", "Birthday", "Phone", "Email", "Address"])
            items = [QStandardItem(field) for field in patientInfo]
            # Make info uneditable to user
            for item in items:
                item.setEditable(False)
            patientModel.appendRow(items)
            patientTable.setModel(patientModel)
            patientTable.resizeColumnsToContents()
        PHNInput.clear()
