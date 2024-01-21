# Related third party imports
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *

# Local application/library specific imports
from Widgets.mplwidget import MplWidget


#Maak een class aan voor Grafiek widget met instellingen
class Graphtab(QWidget):
    def __init__(self, Y_lim_min=-2000, Y_lim_max=2000, Y_min_start=-500, Y_max_start=500, Y_eenheid="-", x_start=5, Y_sym=False, Y_auto=False, *args, **kwargs):
        super(Graphtab, self).__init__(*args, **kwargs) 
        self.setObjectName("tabx")

        #Sla Y_eenheid op als object variable
        self.Y_eenheid = Y_eenheid

        #Maak een Checkbox aan voor de Y symmetrie
        self.Y_sym = QtWidgets.QCheckBox(self)
        self.Y_sym.setGeometry(QtCore.QRect(240, 310, 111, 21))
        self.Y_sym.setChecked(Y_sym)
        self.Y_sym.setObjectName("Y_sym")

        #Maak een Checkbox aan voor het vrijgeven van de Y as
        self.Y_free = QtWidgets.QCheckBox(self)
        self.Y_free.setGeometry(QtCore.QRect(240, 330, 111, 21))
        self.Y_free.setChecked(Y_auto)
        self.Y_free.setObjectName("Y_free")        

        #Maak een label aan voor de X as
        self.X_label = QtWidgets.QLabel(self)
        self.X_label.setGeometry(QtCore.QRect(20, 310, 121, 16))
        self.X_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.X_label.setAlignment(QtCore.Qt.AlignCenter)
        self.X_label.setObjectName("X_label")

        #Maak een label aan voor de eenheid van de x as
        self.X_value_eenheid_label = QtWidgets.QLabel(self)
        self.X_value_eenheid_label.setGeometry(QtCore.QRect(200, 310, 16, 16))
        self.X_value_eenheid_label.setObjectName("X_value_eenheid_label")

        #Maak een slider aan voor de resolutie van de x as
        self.X_slider = QtWidgets.QSlider(self)
        self.X_slider.setGeometry(QtCore.QRect(20, 330, 191, 22))
        self.X_slider.setMinimum(1)
        self.X_slider.setMaximum(60)
        self.X_slider.setProperty("value", x_start)
        self.X_slider.setOrientation(QtCore.Qt.Horizontal)
        self.X_slider.setObjectName("X_slider")

        #Maak een label aan om de Resolutie van de x as weer te geven
        self.X_value = QtWidgets.QLabel(self)
        self.X_value.setGeometry(QtCore.QRect(140, 310, 55, 16))
        self.X_value.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.X_value.setNum(x_start)
        self.X_value.setObjectName("X_value")

        #Maak een label aan voor de minimale Y waarde
        self.Y_min_label = QtWidgets.QLabel(self)
        self.Y_min_label.setGeometry(QtCore.QRect(220, 260, 121, 16))
        self.Y_min_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Y_min_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Y_min_label.setObjectName("Y_min_label")

        #Maak een label aan voor de eenheid van de minimale Y waarde
        self.Y_min_value_eenheid_label = QtWidgets.QLabel()
        self.Y_min_value_eenheid_label.setGeometry(QtCore.QRect(400, 260, 16, 16))
        self.Y_min_value_eenheid_label.setObjectName("Y_min_value_eenheid_label")

        #Maak een slider aan voor de minimale resolutie van de Y as
        self.Y_min_slider = QtWidgets.QSlider(self)
        self.Y_min_slider.setGeometry(QtCore.QRect(220, 280, 191, 22))
        self.Y_min_slider.setMinimum(Y_lim_min)
        self.Y_min_slider.setMaximum(Y_lim_max)
        self.Y_min_slider.setProperty("value", Y_min_start)
        self.Y_min_slider.setSliderPosition(Y_min_start)
        self.Y_min_slider.setOrientation(QtCore.Qt.Horizontal)
        self.Y_min_slider.setObjectName("Y_min_slider")

        #Maak een spinbox aan voor de minimale resolutie van de Y as
        self.Y_min_value = QtWidgets.QSpinBox(self)
        self.Y_min_value.setGeometry(QtCore.QRect(340, 260, 75, 16))
        self.Y_min_value.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Y_min_value.setObjectName("Y_min_value")
        self.Y_min_value.setMaximum(Y_lim_max)
        self.Y_min_value.setMinimum(Y_lim_min)
        self.Y_min_value.setValue(Y_min_start)

        #Maak een label aan voor de maximale Y waarde
        self.Y_max_label = QtWidgets.QLabel(self)
        self.Y_max_label.setGeometry(QtCore.QRect(20, 260, 121, 16))
        self.Y_max_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Y_max_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Y_max_label.setObjectName("Y_max_label")

        #Maak een label aan voor de eenheid van de maximale Y waarde
        self.Y_max_value_eenheid_label = QtWidgets.QLabel()
        self.Y_max_value_eenheid_label.setGeometry(QtCore.QRect(200, 260, 16, 16))
        self.Y_max_value_eenheid_label.setObjectName("Y_max_value_eenheid_label")

         #Maak een slider aan voor de maximale resolutie van de Y as
        self.Y_max_slider = QtWidgets.QSlider(self)
        self.Y_max_slider.setGeometry(QtCore.QRect(19, 280, 191, 22))
        self.Y_max_slider.setMinimum(Y_lim_min)
        self.Y_max_slider.setMaximum(Y_lim_max)
        self.Y_max_slider.setProperty("value", Y_max_start)
        self.Y_max_slider.setOrientation(QtCore.Qt.Horizontal)
        self.Y_max_slider.setObjectName("Y_max_slider")

        #Maak een spinbox aan voor de maximale resolutie van de Y as
        self.Y_max_value = QtWidgets.QSpinBox(self)
        self.Y_max_value.setGeometry(QtCore.QRect(140, 260, 75, 16))
        self.Y_max_value.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Y_max_value.setObjectName("Y_max_value")
        self.Y_max_value.setMaximum(Y_lim_max)
        self.Y_max_value.setMinimum(Y_lim_min)
        self.Y_max_value.setValue(Y_max_start)

        #Maak een grafiek widget aan met het formaat van de start waardes
        self.Graph = MplWidget(self, y_max=Y_max_start, y_min=Y_min_start)
        self.Graph.setGeometry(QtCore.QRect(9, 9, 420, 230))
        self.Graph.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Graph.setAutoFillBackground(False)
        self.Graph.setObjectName("Graph1")

        #Maak start variabelen aan
        self.time_axes = [0]
        self.y_axes = [0]
        self.auto_adjust_y_axis = 0

        #UI functies
        self.retranslateUi()
        self.Signalconnect()

    #Maak een functie aan om alle zichtbare teksten van de Grafiek UI in te voeren
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.Y_sym.setText(_translate("MainWindow", "Y symmetrisch"))
        self.Y_free.setText(_translate("MainWindow", "Y automatisch"))
        self.Y_min_value_eenheid_label.setText(_translate("MainWindow", self.Y_eenheid))
        self.X_label.setText(_translate("MainWindow", "Tijds resolutie"))
        self.X_value_eenheid_label.setText(_translate("MainWindow", "s"))
        self.Y_max_value_eenheid_label.setText(_translate("MainWindow", self.Y_eenheid))
        self.Y_max_label.setText(_translate("MainWindow", "Y max"))
        self.Y_min_label.setText(_translate("MainWindow", "Y min"))
        
        
    #Maak een functie aan om de UI signalen met functies te verbinden
    def Signalconnect(self):
        #Controleer checkboxes en voer acties daarvoor uit
        self.toggleysym(first_try=1)
        self.toggleyauto()

        #Verbind UI veranderingen met waardes van andere UI delen
        self.X_slider.sliderMoved['int'].connect(self.X_value.setNum) # type: ignore
        self.Y_max_slider.sliderMoved['int'].connect(self.Y_max_value.setValue) # type: ignore
        self.Y_max_value.valueChanged['int'].connect(self.Y_max_slider.setValue)
        self.Y_min_slider.sliderMoved['int'].connect(self.Y_min_value.setValue) # type: ignore
        self.Y_min_value.valueChanged['int'].connect(self.Y_min_slider.setValue) # type: ignore

        #Verbind UI veranderingen met des betreffende Resize functie
        self.Y_min_slider.sliderMoved.connect(self.resize_y)
        self.Y_max_slider.sliderMoved.connect(self.resize_y)
        self.Y_min_value.valueChanged.connect(self.resize_y)
        self.Y_max_value.valueChanged.connect(self.resize_y)
        self.X_slider.sliderMoved.connect(self.resize_x)

        #Verbind checkboxes met checkbox functies
        self.Y_sym.toggled.connect(self.toggleysym)
        self.Y_free.toggled.connect(self.toggleyauto)

    #Maak een functie aan om de Y as symmetrisch te maken
    def toggleysym(self, first_try=None):
        #Als de symmetrie checkbox aangevinkt is stel de UI zo in dat de Y min en max automatisch gespiegeld worden
        if self.Y_sym.isChecked():
            self.Y_min_slider.setValue(self.Y_max_slider.value() * -1)
            self.Y_min_value.setValue(self.Y_max_slider.value() * -1)
            self.Y_min_slider.valueChanged['int'].connect(self.mirror_y_min)
            self.Y_max_slider.valueChanged['int'].connect(self.mirror_y_max)

            #Resize naar gespiegelde verzie
            self.resize_y()
        
        #Als het niet de eerste keer is en de checkbox is niet aangevinkt moeten het systeem stoppen met automatisch spiegelen
        elif not first_try:
            self.Y_min_slider.valueChanged['int'].disconnect(self.mirror_y_min)
            self.Y_max_slider.valueChanged['int'].disconnect(self.mirror_y_max)

    #Functie om vanaf Y min te spiegelen
    def mirror_y_min(self):
        self.Y_max_slider.setValue(self.Y_min_slider.value() * -1)
        self.Y_max_value.setValue(self.Y_min_slider.value() * -1)
        
    #Functie om vanaf Y max te spiegelen
    def mirror_y_max(self):
        self.Y_min_slider.setValue(self.Y_max_slider.value() * -1)
        self.Y_min_value.setValue(self.Y_max_slider.value() * -1)

    #Functie om de grafiek te formatten naar de nieuwe y waardes
    def resize_y(self):
        #Als Y automatisch aangepast moet worden wordt dit niet uitgevoerd
        if self.auto_adjust_y_axis != 1:
            self.Graph.setylim([self.Y_min_slider.value(), self.Y_max_slider.value()])

    #Functie om de grafiek te formatten naar de nieuwe x waardes
    def resize_x(self):
        self.Graph.setxlim(self.X_slider.value(), self.time_axes)

    #Functie om twee waardes tegenover elkaar te plotten in de Grafiek
    def plot(self, x, y):
        self.time_axes = x
        self.y_axes = y
        self.Graph.plot(x,y)

    #Functie om de Y as over te schakelen naar automatisch aanpassen
    def toggleyauto(self):
        #Als de checkbox aangevinkt is stel de UI zo in dat de Y min en max automatisch aangepast worden
        if self.Y_free.isChecked():
            self.auto_adjust_y_axis = 1
            self.Graph.setylim([])
        #Als de checkbox niet aangevinkt is stel de UI zo in dat de Y min en max niet automatisch aangepast wordens
        else:
            self.auto_adjust_y_axis = 0
            self.Graph.setylim([self.Y_min_slider.value(), self.Y_max_slider.value()])
        
