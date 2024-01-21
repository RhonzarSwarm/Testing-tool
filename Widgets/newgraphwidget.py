# Standaard bibliotheek imports
import sys

# Gerelateerde derde partij imports
from PyQt5 import QtWidgets

class NewGraphDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()  # Initialiseer de QDialog basis klasse
        self.initUI()  # Roep de initUI methode aan

    def initUI(self):
        self.layout = QtWidgets.QFormLayout()  # Maak een nieuw QFormLayout aan
        self.label_names_spin =  ["Y minimaal:", "Y maximaal:", "Y minimaal start:", "Y maximaal start:", "Tijd start:"]  # Definieer de labels voor de spinboxen
        self.label_names_line = ["Categorie naam:", "Y eenheid:"]  # Definieer de labels voor de line edits

        self.labels = []  # Initialiseer de labels lijst
        self.lineEdits = []  # Initialiseer de lineEdits lijst
        naam_label = QtWidgets.QLabel()  # Maak een nieuw QLabel aan
        naam_label.setText(self.label_names_line[0])  # Stel de tekst van het label in
        self.labels.append(naam_label)  # Voeg het label toe aan de labels lijst

        naam_lineEdit = QtWidgets.QLineEdit()  # Maak een nieuwe QLineEdit aan
        self.lineEdits.append(naam_lineEdit)  # Voeg de QLineEdit toe aan de lineEdits lijst

        self.layout.addRow(self.labels[-1],self.lineEdits[-1])  # Voeg de label en QLineEdit toe aan de layout

        # Herhaal voor elk item in label_names_spin
        for item in self.label_names_spin:
            label = QtWidgets.QLabel()  # Maak een nieuw QLabel aan
            label.setText(item)  # Stel de tekst van het label in
            self.labels.append(label)  # Voeg het label toe aan de labels lijst

            lineEdit = QtWidgets.QSpinBox()  # Maak een nieuwe QSpinBox aan
            lineEdit.setMinimum(-1000000000)  # Stel het minimum van de QSpinBox in
            lineEdit.setValue(1)  # Stel de waarde van de QSpinBox in
            lineEdit.setMaximum(1000000000)  # Stel het maximum van de QSpinBox in
           
            self.lineEdits.append(lineEdit)  # Voeg de QLineEdit toe aan de lineEdits lijst

            self.layout.addRow(self.labels[-1],self.lineEdits[-1])  # Voeg de label en QLineEdit toe aan de layout

        # Stel de maximum, minimum en startwaarden in voor specifieke lineEdits
        self.lineEdits[5].setMaximum(60)
        self.lineEdits[5].setMinimum(2)
        self.lineEdits[1].setValue(-1)
        self.lineEdits[3].setValue(-1)

        eenheid_label = QtWidgets.QLabel()  # Maak een nieuw QLabel aan
        eenheid_label.setText(self.label_names_line[1])  # Stel de tekst van het label in
        self.labels.append(eenheid_label)  # Voeg het label toe aan de labels lijst

        eenheid_lineEdit = QtWidgets.QLineEdit()  # Maak een nieuwe QLineEdit aan
        self.lineEdits.append(eenheid_lineEdit)  # Voeg de QLineEdit toe aan de lineEdits lijst

        self.layout.addRow(self.labels[-1],self.lineEdits[-1])  # Voeg de label en QLineEdit toe aan de layout

        self.auto_checkbox = QtWidgets.QCheckBox()  # Maak een nieuwe QCheckBox aan
        self.auto_checkbox.setText("Y automatisch")  # Stel de tekst van de checkbox in

        self.sym_checkbox = QtWidgets.QCheckBox()  # Maak een nieuwe QCheckBox aan
        self.sym_checkbox.setText("Y Symmetrisch")  # Stel de tekst van de checkbox in

        self.layout.addRow(self.auto_checkbox, self.sym_checkbox)  # Voeg de checkboxes toe aan de layout

        self.Accepted_button = QtWidgets.QPushButton()  # Maak een nieuwe QPushButton aan
        self.Accepted_button.setText("Ok")  # Stel de tekst van de knop in
        
        self.Rejected_button = QtWidgets.QPushButton()  # Maak een nieuwe QPushButton aan
        self.Rejected_button.setText("Cancel")  # Stel de tekst van de knop in

        self.layout.addRow(self.Accepted_button, self.Rejected_button)  # Voeg de knoppen toe aan de layout

        # Voeg de hoofdlayout toe aan de dialoog
        self.setLayout(self.layout)
        self.setWindowTitle('Configuratie')  # Stel de titel van het venster in

        # Verbind de knoppen met de bijbehorende functies
        self.Rejected_button.clicked.connect(sys.exit)
        self.rejected.connect(sys.exit)
        self.Accepted_button.clicked.connect(self.setconfig)
        self.sym_checkbox.stateChanged.connect(self.sym_toggle)

    def sym_toggle(self):
        # Als de sym_checkbox aangevinkt is, verberg bepaalde elementen
        if self.sym_checkbox.isChecked():
            self.lineEdits[1].hide()
            self.lineEdits[3].hide()
            self.labels[1].hide()
            self.labels[3].hide()
            self.adjustSize()
        else:
            # Als de sym_checkbox niet aangevinkt is, toon de elementen
            self.lineEdits[1].show()
            self.lineEdits[3].show()
            self.labels[1].show()
            self.labels[3].show()
            self.adjustSize()  # Pas de grootte van de dialoog aan
 
    
    def setconfig(self):
        self.config = []  # Initialiseer de config lijst
        for item in self.lineEdits:
            try:
                # Probeer de waarde van het item toe te voegen aan de config lijst
                self.config.append(item.Value())
            except:
                # Als dat niet lukt, voeg dan de tekst van het item toe aan de config lijst
                self.config.append(item.text())

        if self.sym_checkbox.isChecked():
            # Als de sym_checkbox aangevinkt is, stel de waarden van config[1] en config[3] in op het negatieve van config[2] en config[4]
            self.config[1] = int(self.config[2]) * -1
            self.config[3] = int(self.config[4]) * -1

        # Voeg de status van de checkboxes toe aan de config lijst
        self.config.append(self.auto_checkbox.isChecked())
        self.config.append(self.sym_checkbox.isChecked())
        
        csvfile = open("plot_config.csv", 'a')  # Open het configuratiebestand in append-modus

        csvline = "\n"  # Initialiseer de csv-lijn met een nieuwe regel

        for item in self.config:
            # Voeg elk item in de config lijst toe aan de csv-lijn, gevolgd door een puntkomma
            csvline = csvline + str(item) + ";"
        
        csvline = csvline[:-1]  # Verwijder de laatste puntkomma van de csv-lijn

        csvfile.write(csvline)  # Schrijf de csv-lijn naar het configuratiebestand

