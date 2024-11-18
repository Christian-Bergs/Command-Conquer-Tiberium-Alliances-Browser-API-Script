#########################################################################################################
##
##  Command & Conquer - Tiberium Alliance API Crowler
##  
##  Idea by             Gerald Günther
##  Base coded by:      Christian Bergs & Gerald Günther
##  Tested by:          Pascal Hassenberg
##
##
#########################################################################################################

## Basic Imports
import os
import time
import atexit

## Custom Imports
from config import log_file
from modules.exceptions import *
from modules.utils import startscreen, wait_for_tab_ready
from modules.browser_utils import start_chrome, initialize_browser
from modules.network_utils import print_page_source
from modules.log_analyzer import extract_first_session

## Main Function (RunScript)

if __name__ == "__main__":
    # Leeren der Konsole
    os.system('cls')

    # Erstelle Start Bildschirm
    startscreen()

    # Starte Chrome
    print('[DEV] Starte Chrome Browser mit Debugging Modus')
    start_chrome()

    # Initialisiere den Browser
    browser, tab = initialize_browser()

    # Starte Netzwerk-Tracking
    try:
        tab.start()
        wait_for_tab_ready(tab)
        tab.call_method("Network.enable")

        tab.call_method("Page.navigate", url="https://www.ea.com/de-de/games/command-and-conquer/command-and-conquer-tiberium-alliances")
        print("[Dev] Navigation erfolgreich.")

        # Speichere den Quelltext nach einer kurzen Wartezeit
        time.sleep(20)
        print_page_source(tab)
    except Exception as e:
        print(f"[Error] Fehler beim Laden der Webseite oder beim Speichern: {e}")

    # Quelltext speichern
    print_page_source(tab, log_file)

    # Session-Wert extrahieren
    extract_first_session(log_file)

    # Cleanup-Funktion registrieren
    atexit.register(lambda: tab.stop())