from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout, QHBoxLayout

class RemoveNoteGUI(QWidget):
    def __init__(self, controller, stackedLayout):
        super().__init__()
        self.controller = controller
        self.stackedLayout = stackedLayout
    
    def remove_note_screen(self):
        removeNoteWidget = QWidget()
        removeNoteLayout = QVBoxLayout()

        buttonOptionsLayout = QHBoxLayout()
        
        labelText = QLabel("Please enter the code # of the note you want to delete.")
        labelText.setAlignment(Qt.AlignmentFlag.AlignCenter) # Center aligning the text
        
        noteInput = QLineEdit(self)
        
        goBackButton = QPushButton("Back")
        goBackButton.clicked.connect(lambda: self.go_back_button_click(noteInput))
        
        enterButton = QPushButton("Enter")
        enterButton.clicked.connect(lambda: self.enter_button_click(noteInput))
        
        removeNoteLayout.addWidget(labelText)
        removeNoteLayout.addWidget(noteInput)
        
        buttonOptionsLayout.addWidget(goBackButton)
        buttonOptionsLayout.addWidget(enterButton)
        
        removeNoteLayout.addLayout(buttonOptionsLayout)
        removeNoteWidget.setLayout(removeNoteLayout)
        
        return removeNoteWidget
    
    def go_back_button_click(self, noteInput):
        noteInput.clear()
        self.stackedLayout.setCurrentIndex(10)
        
    def enter_button_click(self, noteInput):
        code = noteInput.text()
        if not code or not code.isnumeric():
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid code #.")
            noteInput.clear()
            return
        
        note = self.controller.search_note(int(code))
        
        if note is None:
            QMessageBox.warning(self, "Invalid Code #", "There is no note that exists with this code #.")
        else:
            noteString = f"\n\nCode #: {note.code}\nText: {note.text}\nTimestamp: {note.timestamp}"
            confirmationBox = QMessageBox.question(self, "Confirm?", "Are you sure you want to delete this note?" + noteString)
            
            if confirmationBox == QMessageBox.StandardButton.Yes:
                self.controller.delete_note(int(code))
                self.stackedLayout.setCurrentIndex(10)
                QMessageBox.information(self, "Success", "Note has been deleted.")
                
        noteInput.clear()