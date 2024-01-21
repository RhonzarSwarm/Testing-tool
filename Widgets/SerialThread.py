# Standaard bibliotheek imports
import time

# Gerelateerde derde partij imports
import serial
import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtCore import QObject, QThread, pyqtSignal


class SerialThread(QObject):
    finished = pyqtSignal()  # Signaal voor het einde van de thread
    progress = pyqtSignal()  # Signaal voor de voortgang van de thread
    plot = pyqtSignal()  # Signaal voor het plotten van data
    time_axes = []  # Lijst voor de tijd-as van de plot
    Y_axes = []  # Lijst voor de Y-as van de plot
    new_Y_axes = []  # Lijst voor de nieuwe Y-as van de plot
    record = 0  # Variabele voor het opnemen van data
    COMPORT = None  # Variabele voor de COM-poort
    Baudrate = 9600  # Variabele voor de baudrate
    count = 0  # Teller voor het aantal metingen
    meetlengte = 0  # Variabele voor de lengte van de meting
    metingstarttime = 0  # Variabele voor de starttijd van de meting
    filename = ""  # Variabele voor de bestandsnaam
    makegraph = 0  # Variabele voor het maken van een grafiek
    makehistandbox = 0  # Variabele voor het maken van een histogram en boxplot
    plotnum = 1  # Variabele voor het aantal plots

    def start(self):
        self.ser = serial.Serial(self.COMPORT, baudrate=self.Baudrate)  # Start de seriële verbinding
        self.loop()  # Start de loop

    def loop(self):

        starttime = time.perf_counter()  # Sla de starttijd op
        print(self.plotnum)
        for i in range(self.plotnum):
            self.new_Y_axes.append([])  # Voeg een nieuwe lijst toe aan new_Y_axes
            
        while(True):
            data = self.ser.readline()  # Lees een regel van de seriële verbinding

            if data:
                
                data = data.decode()  # Decodeer de data
                data = data.split(";")  # Splits de data op de puntkomma's
                count = 0

                for item in data:
                    item = float(item)  # Zet het item om naar een float
                    self.new_Y_axes[count].append(item)  # Voeg het item toe aan new_Y_axes
                    count += 1  # Verhoog de teller

                Time = time.perf_counter() - starttime  # Bereken de verstreken tijd
                self.time_axes.append(Time)  # Voeg de verstreken tijd toe aan time_axes
                
                if self.time_axes[-1] - 60 >= self.time_axes[0]:
                    self.time_axes.pop(0)  # Verwijder het eerste element van de tijd-as
                    for item in self.new_Y_axes:
                        item.pop(0)  # Verwijder het eerste element van de nieuwe Y-as

                self.plot.emit()  # Zend het plot signaal uit
                if self.record == 1:
                    # waardes opnemen in csv
                    MetingTime = time.perf_counter() - self.metingstarttime  # Bereken de tijd van de meting
                    newline = [str(MetingTime)]  # Maak een nieuwe regel met de tijd van de meting
                    for item in data:
                        if item.endswith("\n"):
                            item = item[:-2]  # Verwijder de newline karakters
                        newline.append(str(item))  # Voeg het item toe aan de nieuwe regel
                    with open(self.filename, 'a') as csvfile:
                        label = ''
                        csvline = '\n'
                        for item in newline:
                            csvline = csvline + item + ';'  # Voeg het item toe aan de csv regel
                            if item != newline[0]:
                                label = label + ', '
                            label = label + item
                        csvfile.write(csvline)  # Schrijf de csv regel naar het bestand
                    self.count += 1  # Verhoog de teller
                    self.progress.emit()  # Zend het progress signaal uit

                    if self.meetlengte == self.count:

                        with open(self.filename, 'r') as csvfile:
                            x = []
                            y = []
                            file = csvfile.readlines()  # Lees alle regels van het bestand
                            file[0] = file[0].split(";")  # Splits de eerste regel op de puntkomma's
                            print(file[0])
                            file[0] = file[0][1:]  # Verwijder het eerste element van de eerste regel
                            for item in file[0]:
                                y.append([])  # Voeg een lege lijst toe aan y
                            categories = len(file[0])  # Bepaal het aantal categorieën
                            file = file[1:]  # Verwijder de eerste regel van het bestand

                            for i in range(len(file)):

                                file[i] = file[i].split(";")  # Splits de i-de regel op de puntkomma's
                                if len(file[i]) > categories:
                                    file[i] = file[i][:-1]  # Verwijder het laatste element van de i-de regel
                                x.append(float(file[i][0]))  # Voeg het eerste element van de i-de regel toe aan x
                                for j in range(categories):
                                    y[j].append(float(file[i][j+1]))  # Voeg het j+1-de element van de i-de regel toe aan y[j]


                            if self.makehistandbox == 1:
                                for i in range(len(y)):
                                    y_local = y[i]  # Sla de i-de y op in y_local
                                    data = np.array(y_local, dtype='float')  # Zet y_local om naar een numpy array van floats

                                    roundoff = 2  # Stel de afronding in op 2 decimalen

                                    # Bereken verschillende statistieken en rond ze af
                                    MIN = round(np.min(data),roundoff)
                                    MAX = round(np.max(data),roundoff)
                                    MEDIAAN = round(np.median(data),roundoff)
                                    eerste_Kwartiel = round(np.quantile(data, 0.25),roundoff)
                                    derde_Kwartiel = round(np.quantile(data, 0.75),roundoff)
                                    Spreidingsbreedte = round(np.max(data) - np.min(data),roundoff)
                                    Kwartielafstand = round(np.quantile(data, 0.75) - np.quantile(data, 0.25),roundoff)
                                    Gemiddelde = round(np.average(data),roundoff)   

                                    # Maak een figuur met een boxplot en een histogram
                                    fig, ax = plt.subplots(
                                        2, figsize=(7, 6), sharex=False,
                                        gridspec_kw={"height_ratios": (.3, .7)}  # de boxplot krijgt 30% van de verticale ruimte
                                    )

                                    # de boxplot
                                    ax[0].boxplot(data, vert=False, manage_ticks=True)
                                    # verwijder de randen
                                    ax[0].spines['top'].set_visible(False)
                                    ax[0].spines['right'].set_visible(False)
                                    ax[0].spines['left'].set_visible(False)
                                    ax[0].set_xticks([MIN,eerste_Kwartiel,MEDIAAN,derde_Kwartiel,MAX])
                                    ax[0].set_yticks([],[])

                                    # het histogram
                                    n, bins, patcher = ax[1].hist(data, bins=20)

                                    ax[1].set_xticks(bins)
                                    ax[1].set_xticklabels(bins, rotation=45)
                                    stdev = round(np.std(data),roundoff)

                                    ax[1].text(min(y_local), max(n), 'stdev: %s\nmean: %s\naverage: %s' % (stdev, MEDIAAN, Gemiddelde), fontsize=10, verticalalignment='top')

                                    # sla de figuur op
                                    fig.savefig(fname=self.filename[:-4] + "_plot_histogram_" + str(i))
                                    fig.clear()

                            if self.makegraph == 1:
                                plt.xlim(round(float(x[1])), round(float(x[-1])))  # Stel de limieten van de x-as in
                                xticks = []  # Maak een lege lijst voor de x-ticks
                                for i in range(11):
                                    xticks.append(round(round(float(x[-1])) / 10 * i, 1))  # Voeg de i-de x-tick toe aan de lijst
                                plt.xticks(xticks,xticks)  # Stel de x-ticks in
                                for i in range(len(y)):
                                    plt.plot(x,y[i])  # Plot de i-de y tegen x
                                    plt.savefig(fname=self.filename[:-4] + "_plot_" + str(i))  # Sla de figuur op
                                    plt.clf()  # Maak de figuur leeg
                                    
                        self.finished.emit()  # Zend het finished signaal uit

                        self.count = 0  # Zet de teller op 0
                        self.record = 0  # Zet de opname uit

    def setname(self):
        pass  # Deze functie doet niets
