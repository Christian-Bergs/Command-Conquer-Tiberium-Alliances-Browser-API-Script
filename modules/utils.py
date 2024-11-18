import sys
import time

def startscreen():
    print("""
||***********************************************************************
||
||  Command & Conquer Tiberium Alliance Browser API Script
||
||    Idea by          Gerald Günther
||    coded by:        Christian Bergs
||    tested by:      Pascal Hassenberg
||
||***********************************************************************
""")


def wait_for_tab_ready(tab):
    print("[Dev] Warte, bis der Tab vollständig geladen ist...")
    time.sleep(5)  # Warte, um sicherzustellen, dass der Tab bereit ist
