# Standard library imports
from calendar import c
import os
import time
from datetime import datetime

# Related third party imports
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QThread
import serial.tools.list_ports

# Local application/library specific imports
from Widgets.graphtab import Graphtab
from Widgets.SerialThread import SerialThread
from Widgets.comdialog import COMDialogclass

# Maindindow class
class Ui_MainWindow(object):
    # vaste variabelen aanmaken
    project_name = ""
    config = []
    configurations = []
    plotnum = 1

    # UI setup
    def setupUi(self, MainWindow):
        
        #Maak een hoofdscherm aan
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(665, 501)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #Maak een tab widget aan
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 420, 400))
        self.tabWidget.setObjectName("tabWidget")

        #Maak een lijst met graphiek objecten aan voor alle configuraties      
        self.Graphs = []
        graphcount = 1
        for config in self.configurations:
            #omzetten van strings naar booleans
            
            for i in range(len(config)):
                if config[i] == "True":
                    config[i] = True
                elif config[i] == "False":
                    config[i] = False
            
            print(config)

            #Aanmaken van een nieuwe grafiek met de ingestelde configuratie
            Graph = Graphtab( Y_lim_min=int(config[0]),
                                Y_lim_max=int(config[1]),
                                Y_max_start=int(config[3]),
                                Y_min_start=int(config[2]),
                                Y_auto=config[-2],
                                Y_sym=config[-1],
                                Y_eenheid=str(config[4]))

            #Grafiek toevoegen als een nieuw tab
            tabname = f"Grafiek {graphcount}"
            test = self.tabWidget.addTab(Graph, tabname)
            print(test)
            #Grafiek toevoegen aan de lijst met grafieken
            graphcount += 1
            self.Graphs.append(Graph)
        
        #Maak een progressbar aan voor het bijhouden van de meting
        self.Record_progressbar = QtWidgets.QProgressBar(self.centralwidget)
        self.Record_progressbar.setGeometry(QtCore.QRect(30, 420, 391, 23))
        self.Record_progressbar.setProperty("value", 0)
        self.Record_progressbar.setObjectName("Record_progressbar")

        #Maak een label aan voor de test naam
        self.Testnaam_label = QtWidgets.QLabel(self.centralwidget)
        self.Testnaam_label.setGeometry(QtCore.QRect(470, 80, 121, 16))
        self.Testnaam_label.setObjectName("Testnaam_label")

        #Maak een line edit box aan voor het opgeven van de test naam
        self.Testnaam_box = QtWidgets.QLineEdit(self.centralwidget)
        self.Testnaam_box.setGeometry(QtCore.QRect(470, 110, 161, 22))
        self.Testnaam_box.setObjectName("Testnaam_box")

        #Maak een label aan voor de meetlengte
        self.Meetlengte_label = QtWidgets.QLabel(self.centralwidget)
        self.Meetlengte_label.setGeometry(QtCore.QRect(470, 220, 80, 16))
        self.Meetlengte_label.setObjectName("Meetlengte_label")

        #Maak een slider aan voor de meetlengte
        self.Meetlengte_slider = QtWidgets.QSlider(self.centralwidget)
        self.Meetlengte_slider.setGeometry(QtCore.QRect(470, 240, 160, 22))
        self.Meetlengte_slider.setMinimum(10)
        self.Meetlengte_slider.setMaximum(10000)
        self.Meetlengte_slider.setOrientation(QtCore.Qt.Horizontal)
        self.Meetlengte_slider.setObjectName("Meetlengte_slider")

        #Maak een label aan voor de waarde van de meetlengte
        self.Meetlengte_value = QtWidgets.QLabel(self.centralwidget)
        self.Meetlengte_value.setGeometry(QtCore.QRect(570, 220, 55, 16))
        self.Meetlengte_value.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Meetlengte_value.setObjectName("Meetlengte_value")

        #Maak een spinbox aan voor de meetlengte
        self.meetlengte_spinbox = QtWidgets.QSpinBox(self.centralwidget)
        self.meetlengte_spinbox.setGeometry(QtCore.QRect(470, 270, 81, 22))
        self.meetlengte_spinbox.setMinimum(10)
        self.meetlengte_spinbox.setMaximum(10000)
        self.meetlengte_spinbox.setObjectName("meetlengte_spinbox")

        #Maak een label aan voor het test nummer
        self.Testnummer_label = QtWidgets.QLabel(self.centralwidget)
        self.Testnummer_label.setGeometry(QtCore.QRect(470, 140, 111, 16))
        self.Testnummer_label.setObjectName("Testnummer_label")

        #Maak een spinbox aan voor het test nummer
        self.Testnummer_box = QtWidgets.QSpinBox(self.centralwidget)
        self.Testnummer_box.setGeometry(QtCore.QRect(470, 170, 161, 22))
        self.Testnummer_box.setObjectName("Testnummer_box")
        self.Testnummer_box.setMinimum(1)
        self.Testnummer_box.setValue(1)
        self.Testnummer_box.setMaximum(100)

        #Maak een Checkbox aan voor het maken van een grafiek met gemete data
        self.Grafiek_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.Grafiek_checkbox.setGeometry(QtCore.QRect(480, 330, 141, 20))
        self.Grafiek_checkbox.setChecked(True)
        self.Grafiek_checkbox.setObjectName("Grafiek_checkbox")
        
        #Maak een Checkbox aan voor het maken van een histogram met gemete data
        self.Hist_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.Hist_checkbox.setGeometry(QtCore.QRect(480, 310, 141, 20))
        self.Hist_checkbox.setChecked(True)
        self.Hist_checkbox.setObjectName("Grafiek_checkbox")

        #Maak een knop aan om de metingen op te nemen
        self.Record_button = QtWidgets.QPushButton(self.centralwidget)
        self.Record_button.setGeometry(QtCore.QRect(480, 370, 141, 41))
        self.Record_button.setObjectName("Record_button")
        self.Record_button.setEnabled(False)

        #Maak een knop aan om het seriele verbindingen scherm te openen
        self.Serial_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Serial_Button.setGeometry(QtCore.QRect(460, 40, 180, 28))
        self.Serial_Button.setObjectName("Serial_Button")

        #Window centreren en toevoegen status bar
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #Maak een PYQT5 thread aan
        self.thread = QThread()

        #Maak Object aan voor de Communicatie thread
        self.SerialThread = SerialThread()

        #Voeg het communicatie thread object aan de thread toe
        self.SerialThread.moveToThread(self.thread)
        
        #Stel de front end namen van labels in
        self.retranslateUi(MainWindow)

        #Begin op grafiek 1
        self.tabWidget.setCurrentIndex(0)

        #Verbind de meetlengte slider en spinbox met de waarde zodat deze met elkaar veranderen
        self.Meetlengte_slider.sliderMoved['int'].connect(self.Meetlengte_value.setNum) # type: ignore
        self.meetlengte_spinbox.valueChanged['int'].connect(self.Meetlengte_slider.setValue) # type: ignore
        self.Meetlengte_slider.valueChanged['int'].connect(self.Meetlengte_value.setNum) # type: ignore
        self.Meetlengte_slider.sliderMoved['int'].connect(self.meetlengte_spinbox.setValue) # type: ignore

        #Verbind het opstarten van de thread met het opstarten van het thread object
        self.thread.started.connect(self.SerialThread.start)

        #Verbind alle emit functies van het thread object met de desbetreffende functies
        self.SerialThread.finished.connect(self.record_finished)
        self.SerialThread.plot.connect(self.plotfunc)
        self.SerialThread.progress.connect(self.recordprogress)

        #Verbind de knoppen met hun des betreffende functies
        self.Record_button.clicked.connect(self.record_button_func)
        self.Serial_Button.clicked.connect(self.comopenfunc)
      
        #Stel de headers voor de csv bestanden in
        self.headline = "Tijd[s]"
        for item in self.configurations:
            self.headline = self.headline + ";Meting[{}]".format(item[-3])

        #Verbind overige functies
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    #Progress doorvoeren naar de progressbar
    def recordprogress(self):
        self.Record_progressbar.setValue(self.SerialThread.count)
    
    #Functie voor het opnemen van de gemete waardes
    def record_button_func(self):
        #Sla de gekozen meetlengte op en geef dit door aan de betreffende objecten
        meetlengte = self.Meetlengte_slider.value()
        self.Record_progressbar.setMaximum(meetlengte)
        self.SerialThread.meetlengte = meetlengte

        #Geef de huidige tijd door aan de communicatie functie
        self.SerialThread.metingstarttime = time.perf_counter()

        #Projectnaam naar Temp veranderen als er geen projectnaam is opgegeven
        if self.project_name == "":
            self.project_name = "Temp"

        #Test naam bepalen en vastleggen
        if self.Testnaam_box.text() == "":
            self.testnaam = "Temp"
        else:
            self.testnaam = self.Testnaam_box.text()
        
        #Test nummer vastleggen
        self.testnummer = str(self.Testnummer_box.value())

        #Pathing opstellen voor opgenomen data
        self.project_path = f"projects/{self.project_name}"
        path = f"{self.project_path}/{self.testnaam}"
        filename = f"{path}/{self.testnaam}_{self.testnummer}"

        #Maak een folder genaamd projects aan als deze nog niet bestaat
        if not os.path.exists("projects"):
            os.mkdir("projects")
        
        #Maak een folder aan voor dit specifieke project als deze nog niet bestaat
        if not os.path.exists(self.project_path):
            os.mkdir(self.project_path)

        #Maak een folder aan voor deze test als deze nog niet bestaat
        if not os.path.exists(path):
                os.mkdir(path)
        
        #Datum en tijd van test vaststellen
        now = datetime.now()
        dt_string = now.strftime("dt_%m-%d_t_%H_%M_%S")

        #Bestands naam voor het csv bestand vastleggen
        filename = f"{filename}_{dt_string}.csv"

        #Maak het bestand aan en voeg de gewenste headers toe
        with open(filename, 'w') as csvfile:
            csvfile.write(self.headline)

        #Grafiek checkbox controleren en vastleggen
        if self.Grafiek_checkbox.isChecked():
            self.SerialThread.makegraph = 1
        else:
            self.SerialThread.makegraph = 0

        #Histogram checkbox controleren en vastleggen
        if self.Hist_checkbox.isChecked():
            self.SerialThread.makehistandbox = 1
        else:
            self.SerialThread.makehistandbox = 0

        #Bestandsnaam doorgeven aan de communicatie thread   
        self.SerialThread.filename = filename

        #Doorgeven aan de communicatie thread dat deze moet beginnen met opnemen
        self.SerialThread.record = 1

    #Maak een functie aan voor als het programma klaar is met opnemen
    def record_finished(self):
        #reset progressbar
        self.Record_progressbar.setValue(0)
        #Test nummer 1 omhoog
        self.Testnummer_box.setValue(self.Testnummer_box.value()+1)
        
    #Maak een functie aan voor het plotten van de uitgelezen data
    def plotfunc(self):
        #plot de tijd en y assen van de huidig zichtbare grafiek
        i = self.tabWidget.currentIndex()
        self.Graphs[i].plot(self.SerialThread.time_axes, self.SerialThread.new_Y_axes[i])

    #Maak een functie voor het openen van het seriele instellingen scherm
    def comopenfunc(self):
        #Maak een dialog aan op basis van de COMDialog class en verbind de accept button aan de accept functie
        self.dialog = COMDialogclass()
        self.dialog.buttonBox.accepted.connect(self.comacceptfunc)
        
        #Maak een lijst met beschikbare COMpoorten en geef deze door
        options = [comport.device for comport in serial.tools.list_ports.comports()]
        self.dialog.comboBox.addItems(options)

        #Open het seriele instellingen scherm
        self.dialog.exec()

    #Maak een functie aan voor het accepteren van de communicatie instellingen
    def comacceptfunc(self):
        #Geef de COMpoort, de gekozen Baudrate en het aantal gemete waardes door aan de Communicatie thread
        self.SerialThread.COMPORT = self.dialog.comboBox.currentText()
        self.SerialThread.Baudrate = int(self.dialog.Serial_combobox.currentText())
        self.SerialThread.plotnum = self.plotnum

        #Maak de opneem knop klik baar
        self.Record_button.setEnabled(True)

        #Start de Communicatie thread
        self.thread.start()

    #Maak een functie aan om alle zichtbare teksten van de mainwindow UI in te voeren
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Python Testing Tool V5"))

        self.Testnaam_label.setText(_translate("MainWindow", "Test naam:"))
        self.Meetlengte_label.setText(_translate("MainWindow", "Meetlengte"))
        self.Testnummer_label.setText(_translate("MainWindow", "Test nummer:"))
        self.Grafiek_checkbox.setText(_translate("MainWindow", "Sla &Grafiek op"))
        self.Record_button.setText(_translate("MainWindow", "&Meting opnemen"))
        self.Meetlengte_value.setText(_translate("MainWindow", "10"))
        self.Serial_Button.setText(_translate("MainWindow", "&Serial"))
        self.Hist_checkbox.setText(_translate("MainWindow", "Maak een &Histogram"))