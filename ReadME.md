# Controlador IR con Arduino y Scripts Bash

Este proyecto permite controlar acciones en un sistema Linux utilizando un control remoto por infrarrojos (IR) y un Arduino. Cada botón del mando envía una señal IR que el Arduino interpreta y transmite por puerto serie. Un script en Python escucha estas señales y ejecuta scripts Bash predefinidos para realizar acciones como controlar el volumen, la reproducción multimedia, el brillo de la pantalla, entre otros.

## 📦 Requisitos

- Arduino (cualquier modelo con puerto serie, como UNO o Nano)
- Sensor IR VS1838b conectado al Arduino
- Control remoto IR compatible
- Sistema Linux con:
  - Python 3
  - `pyserial` instalado (`pip install pyserial`)
  - Scripts Bash para cada acción (ubicados en `~/scripts_ir/`)

## 🔧 Instalación

1. **instalar_dependencias**
   Para instala las dependencias necesarias ejecuta `1-instalar_dependencias.sh`

2. **Crea tus scripts Bash**  
   Asegúrate de tener los scripts correspondientes a cada acción en la carpeta `~/scripts_ir/`, y que tengan permisos de ejecución. Ejecuta `2-inicializar-scripts.py`

   python3 2-inicializar-scripts.py

3. **Sube el código Arduino**  
   Usa un sketch compatible que reciba señales IR y las envíe por `Serial.println()` al detectar un botón. Por ejemplo, usando la librería `IRremote`.
   Cargá `3-sketch-para-cargar.ino` a tu Arduino UNO

4. **Configura el script Python**

   Guarda el siguiente código como `ArduinoIRBridge.py`:

   chmod +x ArduinoIRBridge.py

   Luego ejecútalo:

   python3 ArduinoIRBridge.py

🧠 Funcionamiento

    El script se conecta al puerto serie del Arduino (/dev/ttyUSB0 por defecto).

    Lee continuamente los códigos IR enviados.

    Si el código recibido coincide con uno de los definidos, se ejecuta el script Bash asociado.

    Se aplica un cooldown de 1 segundo para evitar la ejecución repetida por mantener presionado un botón.

🎮 Mapeo de botones

Ejemplo de algunos botones definidos en el script:
   | Código IR | Acción          | Script ejecutado     |
   | --------- | --------------- | -------------------- |
   | `C`       | Subir volumen   | `subir_volumen.sh`   |
   | `18`      | Bajar volumen   | `bajar_volumen.sh`   |
   | `13`      | Mute            | `toggle_mute.sh`     |
   | `1F`      | Play            | `play.sh`            |
   | `12`      | Apagar pantalla | `apagar_pantalla.sh` |
   | `0`       | Bloquear sesión | `bloquear_sesion.sh` |
   | ...       | ...             | ...                  |
    Nota: Puedes personalizar los códigos IR y scripts según tus necesidades editando el diccionario acciones en el script Python.

🔍 Debug

Puedes activar el modo debug editando la variable:

debug = True

Esto imprimirá en consola las señales IR recibidas y los eventos ignorados por cooldown.
🚨 Seguridad

Evita ejecutar scripts que requieran permisos elevados directamente desde este sistema. Si lo haces, asegúrate de tomar precauciones adecuadas (por ejemplo, usando sudoers con comandos específicos).
📃 Licencia

Este proyecto es de uso libre y puede ser modificado y distribuido según los términos de la licencia MIT.
