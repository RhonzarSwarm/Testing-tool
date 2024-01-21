
# Python testing tool

Dit python programma is bedoeld om numerieke waardes over een seriele verbinding: uit te lezen, weer te geven en opnemen. Momenteel is dit programma niet bestemd voor sample rates hoger dan 10 Hz dit kan leiden tot een hoop lag
en kan ook de functionaliteit beinvloeden.


## Auteurs

- Sander Schrader


## Installatie

Getest met python versies: 3.10 en 3.11

Installeer afhankelijkheden met pip

```bash
  pip install pyqt5
  pip install numpy
  pip install matplotlib
  pip install pyserial
```

Als het programma niet werkt zou het kunnen dat er een oude versie van de afhankelijkheden wordt gebruikt dus hieronder de versies waarmee het programma geschreven is.

```bash
  pip install pyqt5==5.15.9
  pip install numpy==1.26.0
  pip install matplotlib==3.8.0
  pip install pyserial==3.5
```

## Directory

Het directory waar Python_testing_tool.py zich bevindt moet de volgende bestanden bevatten:
```bash
  UI\\Serial.ui               Dit bevat de UI voor het instellen van de seriele communicatie. mogelijk aanpassen met QTdesigner

  Widgets\\__init__.py        Initialiseert de folder
  Widgets\\comdialog.py       Dit bestand bevat de class voor de dialog waar seriele communicatie wordt ingesteld
  Widgets\\graphtab.py        Dit bestand bevat de class voor alles wat zich binnen een tab bevindt en wat uniek is per grafiek
  Widgets\\mainwindow.py      Dit bestand bevat de class voor de mainwindow en is de root van het project
  Widgets\\mplwidget.py       Dit bestand bevat de class voor het inladen van een grafiek in pyqt5
  Widgets\\newgraphwidget.py  Dit bestand bevat de class voor het aanmaken van een nieuwe configuratie
  Widgets\\SerialThread.py    Dit bestand bevat de class voor het uitlezen van de seriele monitor in een losse thread
  Widgets\\startupdialog.py   Dit bestand bevat de class voor het opstart scherm

  plot_config.csv             Dit bestand bevat alle configuraties voor grafieken
```
## Features

De testing tool is gemaakt met de volgende features:
```bash
- COM-port detectie
- Meerdere baudrates mogelijk
- Realtime weergave
- Meerdere data inputs mogelijkx  
- Configureerbare grafieken
- Data opslaan
- Basis statistische analyse 
```

## Documentatie

