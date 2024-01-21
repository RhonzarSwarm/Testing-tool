#Imports
from PyQt5 import QtWidgets, uic

#Sla UI op in variabele COMDIalog
COMDialog = uic.loadUiType("UI/Serial.ui")[0]

#Maak een class aan voor het communicatie instellingen scherm
class COMDialogclass(QtWidgets.QDialog, COMDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        #Laad UI in
        self.setupUi(self)