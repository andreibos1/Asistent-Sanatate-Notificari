"""
# Tema Lectia 33 - Asistentul de sanatate (notificari pe desktop)

# Misiunea:
# Scrie un script care ruleaza in fundal si trimite o notificare de tip
# pop-up pe desktop la fiecare 45 de minute, amintindu-ti sa bei un pahar
# cu apa sau sa iti odihnesti ochii.

# Biblioteci de invatat:
# * schedule (pip install schedule) - ruleaza sarcini la intervale specifice
#   cu o sintaxa clara, fara sa scrii manual while True + time.sleep().
# * plyer  (pip install plyer)  - biblioteca cross-platform care lasa Python
#   sa foloseasca functii native ale sistemului, printre care notificarile.

# Checklist pentru implementare:
# 1. O functie simpla send_reminder() care foloseste plyer.notification.notify()
#    pentru a crea o alerta pop-up cu titlu si mesaj.
# 2. Folosim biblioteca schedule ca sa programam send_reminder() la fiecare 45 minute.
# 3. O bucla care mentine scriptul pornit si verifica programarea cu schedule.run_pending().
"""

import time                              # ne trebuie pentru pauza scurta din bucla principala
import schedule                          # biblioteca care programeaza sarcini la interval
from plyer import notification           # de aici luam functia de notificare pe desktop


# tinem minte ce mesaj am trimis ultima data ca sa alternam apa / ochi
ultimul_mesaj: dict = {"rand": 0}        # dictionar simplu ca sa putem modifica valoarea din functie


def send_reminder() -> None:
    """Trimite o notificare pop-up pe desktop (apa sau odihna ochilor, alternativ)."""

    # cele doua mesaje intre care alternam la fiecare rulare
    mesaje: list = [
        ("Pauza de apa", "Bea un pahar cu apa ca sa ramai hidratat!"),   # index 0
        ("Odihna pentru ochi", "Priveste 20 de secunde la ceva aflat departe."),  # index 1
    ]

    index: int = ultimul_mesaj["rand"] % 2         # 0, 1, 0, 1... in functie de cate ori am rulat
    titlu, mesaj = mesaje[index]                    # despachetam tuplul in titlu si mesaj

    notification.notify(                            # apelam functia native de notificare
        title=titlu,                               # titlul ferestrei pop-up
        message=mesaj,                             # textul din pop-up
        app_name="Asistent Sanatate",              # numele aplicatiei care trimite alerta
        timeout=10,                                # cate secunde ramane notificarea pe ecran
    )

    print(f"[{time.strftime('%H:%M:%S')}] Notificare trimisa: {titlu}")  # log in consola
    ultimul_mesaj["rand"] += 1                      # crestem contorul ca data viitoare sa fie celalalt mesaj


def porneste_asistentul(interval_minute: int = 45) -> None:
    """Programeaza notificarea la fiecare 'interval_minute' minute si tine scriptul pornit."""

    schedule.every(interval_minute).minutes.do(send_reminder)  # programam sarcina la interval fix

    print("Asistentul de sanatate a pornit.")                  # mesaj de start
    print(f"Vei primi o notificare la fiecare {interval_minute} minute.")
    print("Lasa fereastra deschisa. Opreste cu CTRL + C.\n")

    send_reminder()                                            # trimitem una acum, sa nu astepti primul interval

    while True:                                                # bucla care tine scriptul viu
        schedule.run_pending()                                # verifica daca a venit momentul unei sarcini
        time.sleep(1)                                          # pauza scurta ca sa nu incarce procesorul


# --- cod de test ---
# Rulat direct, scriptul porneste asistentul cu intervalul cerut in tema (45 minute).
# Pentru o proba rapida poti chema porneste_asistentul(1) ca sa vezi notificarea la 1 minut.
if __name__ == "__main__":
    try:
        porneste_asistentul(45)                               # intervalul cerut in enunt
    except KeyboardInterrupt:                                 # cand apesi CTRL + C
        print("\nAsistentul de sanatate a fost oprit. O zi buna!")
