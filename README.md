# Simple TUI – Terminal UI

![License](https://img.shields.io/badge/license-MIT-blue.svg)  ![Python](https://img.shields.io/badge/python-3.x-blue.svg) 

---

## Übersicht

**Simple TUI** ist ein minimalistisches Python-Terminal-UI-Projekt mit farbiger Ausgabe zur Anzeige von Menüs und zur Ausführung kleiner Beispiel Aufgabe wie dem Sortieren von Zahlen aus einer Textdatei.  
Es dient als Einstieg in die Welt der CLI-Tools mit `colorama` für Farbanpassung und einer einfachen Menüführung.

---

## Demo

```bash
$ python main.py
```

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
 0 > Exit
 1 > TASK 1
 2 > TASK 2
 v1.1 > TASK v1.1
└─────────────────────────────────────────────────────────────────────────────────────┘
```

TASK 1 erstellt eine Datei mit zufälligen Zahlen, sortiert sie und berechnet Durchschnitt & Maximum:

```
 3 | 17 | 26 | 44 | 59 | 62 | 75 | 78 | 87 | 91  
 Durchschnitt: 54.2 | Maximum: 91
```

---

## Features

- Farbige TUI mit ASCII-Banner
- Sortierung zufällig generierter Zahlen
- Speicherung der Ergebnisse in einer Datei
- Benutzerfreundliche Menüführung
- Einfach erweiterbar für neue Aufgaben

---

## Installation

### Voraussetzungen

- Python 3.8+
- `colorama`

```bash
pip install colorama
```

### Projekt klonen

```bash
git clone https://github.com/xqi1337/Simple-Static-TUI.git
cd Simple-Static-TUI
python main.py
```

---

## Projektstruktur

```bash
projekt/
├── main.py              # Hauptprogramm mit UI-Logik und Aufgaben
├── output.txt           # Generierte Zufallszahlen 
└─ processed_output.txt  # Ergebnisdatei
```

---

##  Erweiterungsideen

- Datei-Ein-/Auswahl per Eingabe
- Visualisierung der Zahlen als Balkendiagramm im Terminal
- Farbthema umschaltbar (Dark / Light / Rainbow)
- Weitere Tools wie Zufallswortgenerator, Dateivergleich etc.


---


<p align="center">
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/footers/gray0_ctp_on_line.svg?sanitize=true" />
</p>

