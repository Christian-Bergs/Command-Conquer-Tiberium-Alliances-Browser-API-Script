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
import signal
from threading import Event

## Custom Imports
from config import log_file
from modules.browser.exceptions import *
from modules.browser.utils import startscreen, wait_for_tab_ready
from modules.browser.browser_utils import start_chrome, initialize_browser
from modules.browser.network_utils import print_page_source
from modules.browser.log_analyzer import extract_first_session

# Event für sauberes Beenden
shutdown_event = Event()

# Signalhandler zum Abfangen von CTRL+C (SIGINT) oder SIGTERM
def handle_shutdown_signal(signum, frame):
    print("\n[INFO] Beende das Skript...")
    shutdown_event.set()

# Signale registrieren
signal.signal(signal.SIGINT, handle_shutdown_signal)
signal.signal(signal.SIGTERM, handle_shutdown_signal)

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

    # Cleanup-Funktion registrieren
    atexit.register(lambda: tab.stop())

    # Starte Netzwerk-Tracking
    try:
        tab.start()
        wait_for_tab_ready(tab)
        tab.call_method("Network.enable")

        tab.call_method("Page.navigate", url="https://www.ea.com/de-de/games/command-and-conquer/command-and-conquer-tiberium-alliances")
        print("[DEV] Navigation erfolgreich.")

        # Speichere den Quelltext nach einer kurzen Wartezeit
        time.sleep(30)

        # Quelltext speichern
        print_page_source(tab, log_file)

        # Session-Wert extrahieren
        extract_first_session(log_file)
        os.remove(log_file)

        print("[INFO] Warte auf das Schließen des Browsers oder Abbruch mit STRG+C...")

        # Warten, bis das Browserfenster geschlossen oder das Script abgebrochen wird
        while not shutdown_event.is_set():
            try:
                # Prüfe, ob der Browser-Tab noch geöffnet ist
                tab.call_method("Page.getNavigationHistory")
                time.sleep(1)  # Kurze Pause, um CPU-Auslastung zu minimieren
            except Exception:
                print("[INFO] Browser-Tab wurde geschlossen.")
                shutdown_event.set()

    except Exception as e:
        print(f"[ERROR] Fehler beim Laden der Webseite oder beim Speichern: {e}")

    finally:
        print("[INFO] Bereinige Ressourcen...")
        try:
            tab.stop()
            browser.close_tab(tab)
        except Exception as cleanup_error:
            print(f"[WARNUNG] Fehler beim Bereinigen: {cleanup_error}")

    print("[INFO] Skript beendet.")
