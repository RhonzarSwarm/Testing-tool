# -*- coding: utf-8 -*-

# Python testing tool voor seriele verbindingen
#
# Created by: S. Schrader
#
# WAARSCHUWING: aanpassen van de code kan ervoor zorgen dat deze niet meer werkt zoals gewenst
# en in sommige gevallen dat het programma niet afgesloten kan worden zonder de computer ook af te sluiten.
# Als je aanpassingen maakt zorg ervoor dat je weet wat je aan het doen bent.




# Related third party imports
from PyQt5 import QtWidgets
import csv

# Local application/library specific imports
from Widgets.startupdialog import StartupDialog
from Widgets.mainwindow import Ui_MainWindow
from Widgets.newgraphwidget import NewGraphDialog

#Geef het maximale aantal grafieken
maxgraphs = 10

# start up sequence als een class geschreven
class startup():
    def __init__(self, maxgraphs):
        #Benodigde variabelen voor het inladen van de configuraties
        Config_file = "plot_config.csv"
        options = ["new"]
        self.configs = []
        
        #Configuraties van het csv bestand naar een 2 dimensionele lijst
        with open(Config_file, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:
                if row:
                    self.configs.append(row)

        #Lijst van configuratie namen
        for item in self.configs[1:]:
            options.append(item[0])

        #Start startup dialog op
        self.startup_dialog = StartupDialog(options, maxgraphs)
        self.startup_dialog.Accepted_button.clicked.connect(self.Mainwindowstart)
        self.startup_dialog.exec()

    def Mainwindowstart(self):
        #verberg startup dialog
        self.startup_dialog.hide()

        #Locale lijst aan maken van de gekozen configuraties
        configs_local = []

        #Per Grafiek de gekozen configuratie inladen
        for i in range(int(self.startup_dialog.input_combobox.currentText())):

            #Het gekozen item in de combobox oplsaan in een variabele
            chosen = self.startup_dialog.graphsettings[1][i].currentText()
            

            
            if chosen == "new":
                #Dialog openen om een nieuwe configuratie aan te maken
                self.newconfig = NewGraphDialog()
                self.newconfig.setWindowTitle("configuratie: " + str(i))
                self.newconfig.Accepted_button.clicked.connect(self.newconfig.hide)
                self.newconfig.exec()

                #Nieuwe configuratie opslaan
                config = self.newconfig.config[1:]
                configs_local.append(config)

            
            else:
                #Contoleren welke configuratie bij de gekozen configuratie naam past
                for item in self.configs[1:]:
                    if chosen == item[0]:
                        #De configuratie - de configuratie naam toevoegen aan de configuratie lijst
                        config = item[1:]
                        configs_local.append(config)
                        break
            
        #aanmaken van een mainwindow
        self.MainWindow = QtWidgets.QMainWindow()

        #Mainwindow aanmaken en de instellingen van de startup dialog doorvoeren
        self.ui = Ui_MainWindow()
        self.ui.config = config
        self.ui.configurations = configs_local
        self.ui.plotnum = int(self.startup_dialog.input_combobox.currentText())
        self.ui.project_name = self.startup_dialog.project_lineEdit.text()

        #UI van de Mainwindow inladen en Mainwindow opstarten
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()


#Run het programma
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    start = startup(maxgraphs)
    sys.exit(app.exec_())


