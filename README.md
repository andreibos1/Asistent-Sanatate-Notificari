# Asistent de sanatate - notificari pe desktop

Tema Lectia 33.
Script care ruleaza in fundal si trimite o notificare pop-up pe desktop la
fiecare 45 de minute, amintindu-ti sa bei un pahar cu apa sau sa iti odihnesti ochii.
Mesajul alterneaza: o data "apa", o data "ochi".

## Biblioteci folosite

- **schedule** (`pip install schedule`) - programeaza sarcini la intervale fixe
  cu o sintaxa clara, fara `while True` + `time.sleep()` scris de mana.
- **plyer** (`pip install plyer`) - biblioteca cross-platform care lasa Python
  sa foloseasca functii native ale sistemului, printre care notificarile pe desktop.

## Cum functioneaza

1. `send_reminder()` cheama `plyer.notification.notify()` cu titlu si mesaj si
   afiseaza notificarea pe desktop. Un contor tinut intr-un dictionar decide daca
   mesajul e despre apa sau despre odihna ochilor.
2. `porneste_asistentul(interval_minute)` programeaza sarcina cu
   `schedule.every(interval_minute).minutes.do(send_reminder)`.
3. Bucla `while True` cu `schedule.run_pending()` + `time.sleep(1)` tine scriptul
   pornit si verifica in fiecare secunda daca a venit momentul unei notificari.

La pornire se trimite si o notificare imediat, ca sa nu astepti primul interval.
Oprire cu `CTRL + C`.

## Cum se porneste

Ai nevoie de Python 3.

1. Instaleaza dependintele:
   ```
   pip install -r requirements.txt
   ```
2. Ruleaza:
   ```
   cd "Lectia 33/Tema"
   python main.py
   ```
3. Lasa fereastra deschisa. Notificarile apar la fiecare 45 de minute.

Pentru o proba rapida, in `main.py` la final schimba `porneste_asistentul(45)`
in `porneste_asistentul(1)` ca sa vezi notificarea la fiecare minut.

## Structura

```
Tema/
├── main.py
├── requirements.txt
└── README.md
```
