# Standaard bibliotheek imports
import sys

# Gerelateerde derde partij imports
from PyQt5 import QtWidgets

class StartupDialog(QtWidgets.QDialog):
    def __init__(self, options, graphnum):
        super().__init__()  # Initialiseer de QDialog basis klasse
        self.graphnum = graphnum  # Stel het aantal grafieken in
        self.initUI(options)  # Roep de initUI methode aan met de gegeven opties

    def initUI(self, options):
        self.layout = QtWidgets.QFormLayout()  # Maak een nieuw QFormLayout aan

        self.project_label = QtWidgets.QLabel()  # Maak een nieuw QLabel aan
        self.project_label.setText("Project naam:")  # Stel de tekst van het label in

        self.layout.addRow(self.project_label)  # Voeg het label toe aan de layout

        self.project_lineEdit = QtWidgets.QLineEdit()  # Maak een nieuwe QLineEdit aan

        self.layout.addRow(self.project_lineEdit)  # Voeg de QLineEdit toe aan de layout

        graphnumbers = []
        for i in range(0, self.graphnum):
            graphnumbers.append(str(i+1))  # Voeg het huidige nummer toe aan de lijst van grafieknummers

        self.input_combobox = QtWidgets.QComboBox()  # Maak een nieuwe QComboBox aan
        self.input_combobox.addItems(graphnumbers)  # Voeg de grafieknummers toe aan de combobox

        self.inputs_label = QtWidgets.QLabel()  # Maak een nieuw QLabel aan
        self.inputs_label.setText("Aantal Grafieken: ")  # Stel de tekst van het label in

        self.layout.addRow(self.inputs_label, self.input_combobox)  # Voeg het label en de combobox toe aan de layout

        self.graphsettings = [[],[]]  # Initialiseer de lijst voor de grafiekinstellingen

        for i in range(0, self.graphnum):
            label = QtWidgets.QLabel()  # Maak een nieuw QLabel aan
            label.setText("Configuratie " + str(i+1) + ":")  # Stel de tekst van het label in

            Combobox = QtWidgets.QComboBox()  # Maak een nieuwe QComboBox aan
            Combobox.addItems(options)  # Voeg de gegeven opties toe aan de combobox

            self.graphsettings[0].append(label)  # Voeg het label toe aan de lijst van labels
            self.graphsettings[1].append(Combobox)  # Voeg de combobox toe aan de lijst van comboboxen
            self.layout.addRow(label, Combobox)  # Voeg het label en de combobox toe aan de layout
        
        for i in range(1, self.graphnum):
            self.graphsettings[0][i].hide()  # Verberg het label
            self.graphsettings[1][i].hide()  # Verberg de combobox

        self.Accepted_button = QtWidgets.QPushButton()  # Maak een nieuwe QPushButton aan
        self.Accepted_button.setText("Ok")  # Stel de tekst van de knop in

        self.Rejected_button = QtWidgets.QPushButton()  # Maak een nieuwe QPushButton aan
        self.Rejected_button.setText("Cancel")  # Stel de tekst van de knop in

        self.layout.addRow(self.Accepted_button, self.Rejected_button)  # Voeg de knoppen toe aan de layout

        # Voeg de hoofdlayout toe aan de dialoog
        self.setLayout(self.layout)
        self.setWindowTitle('Configuratie')  # Stel de titel van het venster in
        self.adjustSize()  # Pas de grootte van de dialoog aan

        self.Rejected_button.clicked.connect(sys.exit)  # Verbind de Cancel-knop met de sys.exit functie
        self.rejected.connect(sys.exit)  # Verbind het rejected signaal met de sys.exit functie
        self.input_combobox.currentTextChanged.connect(self.appearing_comboboxes)  # Verbind het currentTextChanged signaal van de combobox met de appearing_comboboxes functie

    def appearing_comboboxes(self):
        inputnum = int(self.input_combobox.currentText())  # Haal het huidige nummer uit de combobox
        for i in range(1,inputnum):
            self.graphsettings[0][i].show()  # Toon het label
            self.graphsettings[1][i].show()  # Toon de combobox
        for i in range(inputnum, self.graphnum):
            self.graphsettings[0][i].hide()  # Verberg het label
            self.graphsettings[1][i].hide()  # Verberg de combobox
        self.adjustSize()  # Pas de grootte van de dialoog aan