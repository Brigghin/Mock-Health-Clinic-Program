from PyQt6.QtWidgets import QWidget, QTableView, QPushButton, QVBoxLayout
from PyQt6.QtGui import QStandardItem, QStandardItemModel

class ListNotesGUI(QWidget): 
    def __init__(self, controller, stackedLayout):
        super().__init__()
        self.controller = controller
        self.stackedLayout = stackedLayout
        self.noteTable = QTableView()
        self.noteModel = QStandardItemModel()
    
    def list_notes_screen(self):
        listNotesScreenWidget = QWidget()
        listNotesScreenLayout = QVBoxLayout()
        
        goBackButton = QPushButton("Back")
        goBackButton.clicked.connect(self.go_back_button_click)
        
        listNotesScreenLayout.addWidget(self.noteTable)
        listNotesScreenLayout.addWidget(goBackButton)
        
        listNotesScreenWidget.setLayout(listNotesScreenLayout)
        return listNotesScreenWidget
    
    def update_note_table(self):
        notes = self.controller.list_notes()
        noteInfoList = []
        
        for note in notes:
            noteInfo = [str(note.code), note.text, str(note.timestamp)]
            noteInfoList.append(noteInfo)
            
        self.noteModel.clear()
        self.noteModel.setHorizontalHeaderLabels(["Code #", "Text", "Timestamp"])
        
        for row in noteInfoList:
            items = [QStandardItem(field) for field in row]
            for item in items:
                item.setEditable(False)
            self.noteModel.appendRow(items)
        
        self.noteTable.setModel(self.noteModel)
        self.noteTable.resizeColumnsToContents()
        
    def go_back_button_click(self):
        self.stackedLayout.setCurrentIndex(10)