README.MD

Readme
======

Projektbeschreibung
-------------------

Dieses Projekt ist zur einfachen erkenung von Menschen auf einem Bild.

Installation
------------

*   Downloads
    *   Python 3.11: https://www.python.org/downloads/
    *   Visual Studio Code: https://code.visualstudio.com/
*   Installation
    *   Folgen sie den Anweisungen des Python installers
    *   DownloDEN Sie in VS Code unter _Extentions_ `⇧` + `⌘` + `X` oder `STRG` + `⇧` + `X` die _Python_ Extention von Microsoft
*   Installation der Python Bibliotheken etc.
    *   **Instaliere Virtuelle Umgebung** -- `python3 -m venv AI` _AI_ ist der Name der Virtuellen Umgebung Aktivierung
        *   **Windows**              `AI\Scripts\activate`
        *   **MacOS / Linux**   `source AI/bin/activate`
    *   **Installiere Bibliotheken** -- `pip install -r requirements.txt`
    *   **Virtuelle Umgebung auswählen** -- `Auf [Python versionsbezeichnung (z.B. 3.11.5)] klicken. → Auf [Python [Version (z.B. 3.11.5)] (64-bit) ('AI': venv)] klicken.`

Beschreibung des Codes
----------------------

*   Importieren der Bibliotheken. Mit ultralytics wird YOLOv8 geladen und/oder importiert. Mit cv2 wird das Bild geladen und mit numpy wird das Bild in ein Array umgewandelt.
    
    `from ultralytics import YOLO import cv2 import numpy as np`  
                    
*   Laden des Models und des Bildes.
    
    `# Lade YOLO model model = YOLO('yolov8x.pt')  img = "test.jpg" img = cv2.imread(img)`
                    
*   Erkennen des Menschens auf dem Bild.
    
    `for r in results:     # Iteriere durch alle erkannten Bounding Boxes in r.boxes     for box, c in zip(r.boxes.xyxy, r.boxes.cls):         class_name = model.names[int(c)]         if class_name == "person":             x1, y1, x2, y2 = map(int, box)             # Zeichne jede Bounding Box auf das Bild             cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 4)`
                    
    
    Erläuterung des Loops
    
    *   `for r in results` -- Für jedes Bild, welches verarbeitet wird, wird ein neues Objekt `r` erstellt.
    *   `for box, c in zip(r.boxes.xyxy, r.boxes.cls):` -- Für jede Bounding Box in `r.boxes.xyxy` wird ein neues Objekt `box` erstellt. Für jede Klasse in `r.boxes.cls` wird ein neues Objekt `c` erstellt.
    *   `class_name = model.names[int(c)]` -- Die Klasse wird in einen String umgewandelt.
    *   `if class_name == "person":` -- Wenn die Klasse `person` ist, dann wird der Code ausgeführt.
    *   `x1, y1, x2, y2 = map(int, box)` -- Die Koordinaten der Bounding Box werden in Integer umgewandelt.
    *   `cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 4)` -- Die Bounding Box wird auf das Bild gezeichnet.
*   Zeige das Bild an.
    
    `# Zeige das Bild an cv2.imshow('YOLOv8n Detection', img) cv2.waitKey(0) cv2.destroyAllWindows()`
