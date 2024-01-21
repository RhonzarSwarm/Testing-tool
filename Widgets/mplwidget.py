# Gerelateerde derde partij imports
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure

class MplWidget(QWidget):

    def __init__(self, ouder=None, y_max=2000, y_min=-2000, x_as=5):
        QWidget.__init__(self, ouder)  # Initialiseer de QWidget basis klasse
        self.y_lim = [y_max,y_min]  # Stel de y-as limieten in
        self.x_as = x_as  # Stel de x-as limieten in
        self.x_ = [0]  # Initialiseer de x-waarden
        self.canvas = FigureCanvas(Figure(figsize=(5,5)))  # Maak een nieuw FigureCanvas aan

        verticale_layout = QVBoxLayout()  # Maak een nieuwe verticale layout aan
        verticale_layout.addWidget(self.canvas)  # Voeg de canvas toe aan de layout
        positie=[0.25, 0.25, 0.65, 0.65]  # Definieer de positie van de subplot
        self.canvas.axes = self.canvas.figure.add_subplot(111, position=positie)  # Voeg een subplot toe aan de figuur
        self.canvas.axes.set(xlabel="Tijd[s]", ylabel="Gemetenwaarde",  xlim=[self.x_[-1] - self.x_as,self.x_[-1]], ylim=self.y_lim)  # Stel de x-as en y-as limieten en labels in

        self.setLayout(verticale_layout)  # Stel de layout van de widget in

        self.canvas.draw()  # Teken de canvas
        self.plotcount = 1  # Initialiseer de plot teller

    
    def plot(self, x, y):
        self.x_ = x  # Update de x-waarden
        self.canvas.axes.clear()  # Maak de huidige plot leeg
        if self.y_lim == []:  # Controleer of de y_lim leeg is
            c = 0  # Initialiseer de teller
            for item in x:  # Doorloop de lijst x
                if item>= self.x_[-1] - self.x_as and item<= self.x_[-1]:  # Controleer of het item binnen de x-as limieten valt
                    c+= 1  # Verhoog de teller
            y = y[-c:]  # Pas de y lijst aan om alleen de laatste c items te bevatten
            x = x[-c:]  # Pas de x lijst aan om alleen de laatste c items te bevatten
            self.canvas.axes.set(xlabel="Tijd[s]", ylabel="Gemetenwaarde",  xlim=[self.x_[-1] - self.x_as,self.x_[-1]], ylim=[max(y)+0.1*(max(y)-min(y)), min(y)-0.1*(max(y)-min(y))])  # Stel de x-as en y-as limieten en labels in
        else:
            self.canvas.axes.set(xlabel="Tijd[s]", ylabel="Gemetenwaarde",  xlim=[self.x_[-1] - self.x_as,self.x_[-1]], ylim=self.y_lim)  # Stel de x-as en y-as limieten en labels in
        self.canvas.axes.plot(x, y, color='#0F0F0F')  # Plot de data op de canvas
        self.canvas.draw()  # Teken de canvas
        

    def setylim(self, y_lim):
        self.y_lim = y_lim  # Update de y-as limieten
        if self.y_lim == []:  # Controleer of de y_lim leeg is
            self.canvas.axes.set(ylim=None)  # Verwijder de y-as limieten
        else:
            self.canvas.axes.set(ylim=self.y_lim)  # Stel de y-as limieten in
        self.canvas.updateGeometry()  # Update de geometrie van de canvas
        self.canvas.draw()  # Teken de canvas

    def setxlim(self, x_as, x):
        self.x_ = x  # Update de x-waarden
        self.x_as = float(x_as)  # Zet de x-as om naar een float
        self.canvas.axes.set(xlim=[self.x_[-1] - self.x_as,self.x_[-1]])  # Stel de x-as limieten in
        self.canvas.updateGeometry()  # Update de geometrie van de canvas
        self.canvas.draw()  # Teken de canvas

        

        