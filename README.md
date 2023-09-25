# Readme

## Projektbeschreibung

Dieses Projekt dient zur einfachen Erkennung von Menschen auf einem Bild.

## Installation

* **Downloads:**
    * Python 3.11: [Python 3.11 Download](https://www.python.org/downloads/)
    * Visual Studio Code: [Visual Studio Code Download](https://code.visualstudio.com/)

* **Installation:**
    * Folgen Sie den Anweisungen des Python Installers.
    * Laden Sie in VS Code unter _Extensions_ die _Python_ Extension von Microsoft herunter, indem Sie `⇧` + `⌘` + `X` oder `STRG` + `⇧` + `X` drücken.

* **Installation der Python-Bibliotheken und mehr:**
    * **Virtuelle Umgebung erstellen:**
      ```shell
      python3 -m venv AI
      ```
      Hier ist "AI" der Name der virtuellen Umgebung.

    * **Aktiviere die virtuelle Umgebung:**
        * **Windows:** 
            ```shell 
            AI\Scripts\activate
            ```

        * **MacOS / Linux:** 
            ```shell
            source AI/bin/activate
            ```


    * **Bibliotheken installieren:**
      ```shell
      pip install -r requirements.txt
      ```

    * **Virtuelle Umgebung auswählen:**
      Klicken Sie auf die [Python-Version (z.B. 3.11.5)] → Klicken Sie auf [Python [Version (z.B. 3.11.5)] (64-bit) ('AI': venv)].

## Beschreibung des Codes

* **Importieren der Bibliotheken:**
    ```python
    from ultralytics import YOLO
    import cv2
    import numpy as np
    ```

* **Laden des Modells und des Bildes:**
    ```python
    # Lade das YOLO-Modell
    model = YOLO('yolov8x.pt')

    # Lade das Bild
    img = "test.jpg"
    img = cv2.imread(img)
    ```

* **Erkennung der Menschen auf dem Bild:**
    ```python
    for r in results:
        for box, c in zip(r.boxes.xyxy, r.boxes.cls):
            class_name = model.names[int(c)]
            if class_name == "person":
                x1, y1, x2, y2 = map(int, box)
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 4)
    ```

    **Erklärung des Loops:**
    * `for r in results`: Für jedes verarbeitete Bild wird ein neues Objekt `r` erstellt.
    * `for box, c in zip(r.boxes.xyxy, r.boxes.cls)`: Für jede Bounding Box in `r.boxes.xyxy` wird ein neues Objekt `box` erstellt. Für jede Klasse in `r.boxes.cls` wird ein neues Objekt `c` erstellt.
    * `class_name = model.names[int(c)]`: Die Klasse wird in einen String umgewandelt.
    * `if class_name == "person":`: Wenn die Klasse "person" ist, wird der Code ausgeführt.
    * `x1, y1, x2, y2 = map(int, box)`: Die Koordinaten der Bounding Box werden in Integer umgewandelt.
    * `cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 4)`: Die Bounding Box wird auf das Bild gezeichnet.

* **Zeige das Bild an:**
    ```python
    # Zeige das Bild an
    cv2.imshow('YOLOv8 Detection', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    ```
