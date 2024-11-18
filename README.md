# Command & Conquer Tiberium Alliances Browser API Script
___

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Google Chrome](https://img.shields.io/badge/Google%20Chrome-4285F4?style=for-the-badge&logo=GoogleChrome&logoColor=white) ![EA](https://img.shields.io/badge/ea-%23000000.svg?style=for-the-badge&logo=ea&logoColor=white) ![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black) ![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white) ![macOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0)

Dieses Python-Skript dient dazu, mit der Browser-API von Google Chrome zu interagieren, um den Quelltext einer Webseite zu speichern und bestimmte Netzwerkereignisse zu analysieren. Es wurde speziell für die Verwaltung und Analyse von `Command & Conquer Tiberium Alliances` entwickelt.

___

## Features

- **Automatisches Starten von Google Chrome** im Debugging-Modus.
- **Speichern des Quelltexts einer Webseite** in einer Logdatei (`output3.log`).
- **Flexible Anpassung** an verschiedene Betriebssysteme (Windows, Linux, macOS).
- **Netzwerkereignis-Listener** (optional) für zukünftige Erweiterungen.

___

## Voraussetzungen

Bevor du das Skript ausführen kannst, stelle sicher, dass folgende Anforderungen erfüllt sind:

1. **Python 3.7+**
2. **Installierte Python-Bibliotheken:**
   - [pychrome](https://github.com/fate0/pychrome)
3. **Google Chrome**:
   - Chrome muss installiert und erreichbar sein.

___

## Installation

1. Klone dieses Repository:
   ```bash
   git clone <URL>
   cd <repository-name>

2. Installiere die benötigten Python-Bibliotheken:
    ```bash
    pip install -r requirements.txt

3. Stelle sicher, dass der Pfad zu Google Chrome in der Datei 'main.py' korrekt ist. Bearbeite die folgenden Zeilen entsprechend deines Betriebssystems:
    ```python
    if sys.platform.startswith('win'):  # Windows
        chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    elif sys.platform.startswith('linux'):  # Linux
        chrome_path = '/usr/bin/google-chrome'
    elif sys.platform.startswith('darwin'):  # macOS
        chrome_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

___

## Nutzung

1. Starte das Skript:

    ```bash
    python main.py

2. Nach dem Start des Skripts:
   * Google Chrome wird im Debugging-Modus gestartet.
   * Der Quelltext der Zielseite wird nach einer kurzen Wartezeit in die Datei output3.log geschrieben.

3. Logdatei prüfen: 
   Der gespeicherte Quelltext kann in der Datei output3.log eingesehen werden.

___

## Projektstruktur

    📂 project-directory/
    ├── 📂 modules/
    │   ├── browser_utils.py        # Browser-bezogene Funktionen (z. B. Chrome starten)
    │   ├── network_utils.py        # Netzwerklistener und Seitenquelltext-Funktionen
    ├── main.py                     # Hauptskript
    ├── requirements.txt            # Python-Abhängigkeiten
    ├── output3.log                 # Generierte Logdatei (Quelltext der Webseite)
    └── README.md                   # Projektbeschreibung

___

## Anpassungen

* Ziel-URL ändern: Um die Zielseite zu ändern, passe die URL in der Datei 'main.py' an:
    ```python
    tab.call_method("Page.navigate", url="https://www.ea.com/de-de/games/command-and-conquer/command-and-conquer-tiberium-alliances")

* Speicherintervall: Um den Quelltext in regelmäßigen Intervallen zu speichern, kann ein Timer hinzugefügt werden.

___

# Lizenz

Dieses Projekt steht unter der `MIT-Lizenz`. Du kannst es frei nutzen, verändern und weiterverteilen.

___

### Hinweis: 
- Dieses Skript wurde für Bildungs- und Analysezwecke entwickelt. Bitte achte darauf, die Nutzungsbedingungen der Zielseite zu respektieren.
- Der Author übernimmt keinerlei Haftung für eventuelle Schäden oder Dateiverluste. Die Nutzung dieses Scriptes erfolgt auf eigene Verantwortung.
