from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout, QHBoxLayout

class AddNoteGUI(QWidget):
    def __init__(self, controller, stackedLayout):
        super().__init__()
        self.controller = controller
        self.stackedLayout = stackedLayout
    
    def add_note_screen(self):
        addNoteWidget = QWidget()
        addNoteLayout = QVBoxLayout()
        
        buttonOptionLayout = QHBoxLayout()

        addNoteText = QLabel("Please enter what you would like to write in the note.")
        addNoteText.setAlignment(Qt.AlignmentFlag.AlignCenter) # Center aligning the text
        
        noteInput = QLineEdit(self)

        goBackButton = QPushButton("Back")
        goBackButton.clicked.connect(lambda: self.go_back_button_click(noteInput))
        
        enterButton = QPushButton("Enter")
        enterButton.clicked.connect(lambda: self.enter_button_click(noteInput))
        
        addNoteLayout.addWidget(addNoteText)
        addNoteLayout.addWidget(noteInput)
        
        buttonOptionLayout.addWidget(goBackButton)
        buttonOptionLayout.addWidget(enterButton)
        
        addNoteLayout.addLayout(buttonOptionLayout)
        addNoteWidget.setLayout(addNoteLayout)
        
        return addNoteWidget
    
    def go_back_button_click(self, noteText):
        noteText.clear()
        self.stackedLayout.setCurrentIndex(10)
        
    def enter_button_click(self, noteInput):
        note = noteInput.text()
        patient = self.controller.get_current_patient()
        patient.record.create_note(note)
        self.stackedLayout.setCurrentIndex(10)
        QMessageBox.information(self, "Success", "Note has been created", QMessageBox.StandardButton.Ok)
        
        noteInput.clear()