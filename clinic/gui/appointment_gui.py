from PyQt6.QtWidgets import QWidget, QPushButton, QMessageBox, QGridLayout, QVBoxLayout

class AppointmentGUI(QWidget):
    def __init__(self, controller, stackedLayout, mainWindow):
        super().__init__()
        self.controller = controller
        self.stackedLayout = stackedLayout
        self.mainWindow = mainWindow
    
    def appointment_menu_screen(self):
        appointmentMenuWidget = QWidget()
        appointmentMenuLayout = QVBoxLayout()
        
        subAppointmentMenuLayout = QGridLayout()
        
        addNoteButton = QPushButton("Add note to patient record")
        addNoteButton.clicked.connect(self.add_note_button_click)
        
        retrieveNotesButton = QPushButton("Retrieve notes from patient record")
        retrieveNotesButton.clicked.connect(self.retrieve_notes_button_click)
        
        changeNoteButton = QPushButton("Change note from patient record")
        changeNoteButton.clicked.connect(self.change_note_button_click)
        
        removeNoteButton = QPushButton("Remove note from patient record")
        removeNoteButton.clicked.connect(self.remove_note_button_click)
        
        listNotesButton = QPushButton("List full patient record")
        listNotesButton.clicked.connect(self.list_notes_button_click)
        
        finishAppointmentButton = QPushButton("Finish appointment")
        finishAppointmentButton.clicked.connect(self.finish_appointment_button_click)
        
        subAppointmentMenuLayout.addWidget(addNoteButton, 0, 1)
        subAppointmentMenuLayout.addWidget(retrieveNotesButton, 0, 2)
        subAppointmentMenuLayout.addWidget(changeNoteButton, 1, 1)
        subAppointmentMenuLayout.addWidget(removeNoteButton, 1, 2)
        
        appointmentMenuLayout.addLayout(subAppointmentMenuLayout)
        
        appointmentMenuLayout.addWidget(listNotesButton)
        appointmentMenuLayout.addWidget(finishAppointmentButton)
        
        appointmentMenuWidget.setLayout(appointmentMenuLayout)
        
        return appointmentMenuWidget
    
    def finish_appointment_button_click(self):
        QMessageBox.information(self, " ", "Appointment finished.", QMessageBox.StandardButton.Ok)
        # Go back to main menu
        self.controller.unset_current_patient()
        self.mainWindow.setWindowTitle("MEDICAL CLINIC SYSTEM")
        self.stackedLayout.setCurrentIndex(2)
        
    def add_note_button_click(self):
        self.stackedLayout.setCurrentIndex(11)
        
    def retrieve_notes_button_click(self):
        self.stackedLayout.setCurrentIndex(15)
    
    def change_note_button_click(self):
        self.stackedLayout.setCurrentIndex(12)
        
    def remove_note_button_click(self):
        self.stackedLayout.setCurrentIndex(14)
        
    def list_notes_button_click(self):
        self.mainWindow.list_notes_gui.update_note_table()
        self.stackedLayout.setCurrentIndex(13)
        
    

