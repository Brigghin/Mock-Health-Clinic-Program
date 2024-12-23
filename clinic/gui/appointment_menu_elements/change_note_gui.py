from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout, QHBoxLayout

class ChangeNoteGUI(QWidget):
    def __init__(self, controller, stackedLayout):
        super().__init__()
        self.controller = controller
        self.stackedLayout = stackedLayout
    
    def change_note_screen(self):
        changeNoteWidget = QWidget()
        changeNoteLayout = QVBoxLayout()
        
        buttonOptionsLayout = QHBoxLayout()

        self.labelText = QLabel("Please enter the code # of the note you would like to change.")
        self.labelText.setAlignment(Qt.AlignmentFlag.AlignCenter) # Center aligning the text
        
        noteInput = QLineEdit(self) # Re-use for updating text
        
        goBackButton = QPushButton("Back")
        goBackButton.clicked.connect(lambda: self.go_back_button_click(noteInput, updateButton, enterButton))
        
        enterButton = QPushButton("Enter")
        enterButton.clicked.connect(lambda: self.enter_button_click(noteInput, updateButton, enterButton))
        
        updateButton = QPushButton("Update")
        updateButton.clicked.connect(lambda: self.update_button_click(noteInput, updateButton, enterButton))
        updateButton.hide()
        
        changeNoteLayout.addWidget(self.labelText)
        changeNoteLayout.addWidget(noteInput)
        
        buttonOptionsLayout.addWidget(goBackButton)
        buttonOptionsLayout.addWidget(enterButton)
        buttonOptionsLayout.addWidget(updateButton)
        
        changeNoteLayout.addLayout(buttonOptionsLayout)
        changeNoteWidget.setLayout(changeNoteLayout)
        
        return changeNoteWidget
    
    def go_back_button_click(self, noteInput, updateButton, enterButton):
        noteInput.clear()
        updateButton.hide()
        enterButton.show()
        self.labelText.setText("Please enter the code # of the note you would like to change.")
        self.stackedLayout.setCurrentIndex(10)
        
    def enter_button_click(self, noteInput, updateButton, enterButton):
        code = noteInput.text().strip()
        if not code or not code.isnumeric():
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid code #")
            noteInput.clear()
            return
        
        self.note_code = int(code)
        note = self.controller.search_note(self.note_code)
        
        if note is None:
            QMessageBox.warning(self, "Invalid Code #", "There is no note that exists with this code #.")
            noteInput.clear()
        else:
            self.labelText.setText("Update the note's text to your liking.")
            enterButton.hide()
            updateButton.show()
            
            noteInput.setText(note.text)
            
        
    def update_button_click(self, noteInput, updateButton, enterButton):
        # If clicked, we know that code is valid and exists
        self.controller.update_note(self.note_code, noteInput.text())
        noteInput.clear()
        updateButton.hide()
        enterButton.show()
        self.labelText.setText("Please enter the code # of the note you would like to change.")
        self.stackedLayout.setCurrentIndex(10)
        QMessageBox.information(self, "Success", "Note has been updated.")