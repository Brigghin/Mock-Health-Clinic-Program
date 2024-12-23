from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QTableView, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QStandardItem, QStandardItemModel

class RetrieveNotesGUI(QWidget):
    def __init__(self, controller, stackedLayout):
        super().__init__()
        self.controller = controller
        self.stackedLayout = stackedLayout
        self.noteTable = QTableView()
        self.noteModel = QStandardItemModel()
    
    def retrieve_notes_screen(self):
        retrieveNotesScreenWidget = QWidget()
        retrieveNotesScreenLayout = QVBoxLayout()
        
        buttonOptionsLayout = QHBoxLayout()

        labelText = QLabel("Retrieve notes by searching for their text.")
        labelText.setAlignment(Qt.AlignmentFlag.AlignCenter) # Center aligning the text
        
        noteInput = QLineEdit(self)
        
        goBackButton = QPushButton("Back")
        goBackButton.clicked.connect(lambda: self.go_back_button_click(noteInput))
        
        enterButton = QPushButton("Enter")
        enterButton.clicked.connect(lambda: self.enter_button_click(noteInput))
        
        buttonOptionsLayout.addWidget(goBackButton)
        buttonOptionsLayout.addWidget(enterButton)
        
        retrieveNotesScreenLayout.addWidget(labelText)
        retrieveNotesScreenLayout.addWidget(self.noteTable)
        retrieveNotesScreenLayout.addWidget(noteInput)
        retrieveNotesScreenLayout.addLayout(buttonOptionsLayout)
        retrieveNotesScreenWidget.setLayout(retrieveNotesScreenLayout)
        
        return retrieveNotesScreenWidget
    
    def go_back_button_click(self, noteInput):
        noteInput.clear()
        self.noteModel.clear()
        self.stackedLayout.setCurrentIndex(10)
        
    def enter_button_click(self, noteInput):
        note_substring = noteInput.text().strip()
        notes = self.controller.retrieve_notes(note_substring)
        if not notes:
            QMessageBox.warning(self, "Invalid text", "No notes with this text exist.", QMessageBox.StandardButton.Ok)
        else:
            # Clear the table before inserting new data
            self.noteModel.clear()
            self.noteTable.setModel(self.noteModel)
            
            self.noteModel.setHorizontalHeaderLabels(["Code #", "Text", "Timestamp"])
            noteInfoList = []
            for note in notes:
                noteInfo = [str(note.code), note.text, str(note.timestamp)]
                noteInfoList.append(noteInfo)
                
            for row in noteInfoList:
                items = [QStandardItem(field) for field in row]
                for item in items:
                    item.setEditable(False)
                self.noteModel.appendRow(items)
                
            self.noteTable.setModel(self.noteModel)
            self.noteTable.resizeColumnsToContents
        noteInput.clear()