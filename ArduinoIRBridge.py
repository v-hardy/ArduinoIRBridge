import serial
import subprocess
import os
import time
#import signal
#
# Evita que aparezca "^C" al presionar Ctrl+C
#signal.signal(signal.SIGINT, lambda sig, frame: None)
 
puerto = '/dev/ttyUSB0'
velocidad = 9600
debug = False

acciones = {
    'C': {'nombre': 'Boton-VOL+', 'script': '~/scripts_ir/subir_volumen.sh'},
    '18': {'nombre': 'Boton-VOL-', 'script': '~/scripts_ir/bajar_volumen.sh'},
    '13': {'nombre': 'Boton-Mute', 'script': '~/scripts_ir/toggle_mute.sh'},
    'B': {'nombre': 'Boton-CH+', 'script': '~/scripts_ir/subir_brillo.sh'},
    '15': {'nombre': 'Boton-CH-', 'script': '~/scripts_ir/bajar_brillo.sh'},
    '1F': {'nombre': 'Boton-Play', 'script': '~/scripts_ir/play.sh'},
    '1E': {'nombre': 'Boton-Pause', 'script': '~/scripts_ir/pause.sh'},
    'E': {'nombre': 'Boton-Stop', 'script': '~/scripts_ir/stop.sh'},
    'F': {'nombre': 'Boton-PREV', 'script': '~/scripts_ir/anterior.sh'},
    '1A': {'nombre': 'Boton-Next', 'script': '~/scripts_ir/adelantar_tema.sh'},
    '12': {'nombre': 'Boton-Power', 'script': '~/scripts_ir/apagar_pantalla.sh'},
    '10': {'nombre': 'Boton-Mode', 'script': '~/scripts_ir/toggle_modoPantallas.sh'},
    '14': {'nombre': 'Boton-OSD', 'script': '~/scripts_ir/mostrar_info.sh'},
    '11': {'nombre': 'Boton-Source', 'script': '~/scripts_ir/cambiar_salida_audio.sh'},
    '19': {'nombre': 'Boton-Snapshot', 'script': '~/scripts_ir/captura.sh'},
    '1D': {'nombre': 'Boton-Record', 'script': '~/scripts_ir/grabar.sh'},
    'D': {'nombre': 'Boton-Stereo', 'script': '~/scripts_ir/toggle_stereo.sh'},
    '1B': {'nombre': 'Boton-TimeShift', 'script': '~/scripts_ir/timeshift.sh'},
    '1C': {'nombre': 'Boton-Radio', 'script': '~/scripts_ir/radio.sh'},
    '16': {'nombre': 'Boton-OK', 'script': '~/scripts_ir/enter.sh'},
    'A': {'nombre': 'Boton-Recall', 'script': '~/scripts_ir/toggle_mostrar-escritorio.sh'},
    '17': {'nombre': 'Boton-Plus', 'script': '~/scripts_ir/cambiar_fondo.sh'},
    '0': {'nombre': 'Boton-0', 'script': '~/scripts_ir/bloquear_sesion.sh'},
    '1': {'nombre': 'Boton-1', 'script': '~/scripts_ir/modo1.sh'},
    '2': {'nombre': 'Boton-2', 'script': '~/scripts_ir/modo2.sh'},
    '3': {'nombre': 'Boton-3', 'script': '~/scripts_ir/modo3.sh'},
    '4': {'nombre': 'Boton-4', 'script': '~/scripts_ir/modo4.sh'},
    '5': {'nombre': 'Boton-5', 'script': '~/scripts_ir/modo5.sh'},
    '6': {'nombre': 'Boton-6', 'script': '~/scripts_ir/modo6.sh'},
    '7': {'nombre': 'Boton-7', 'script': '~/scripts_ir/modo7.sh'},
    '8': {'nombre': 'Boton-8', 'script': '~/scripts_ir/modo8.sh'},
    '9': {'nombre': 'Boton-9', 'script': '~/scripts_ir/modo9.sh'}
}

print(f'Escuchando IR en {puerto}...')

# Cooldown en segundos
cooldown = 1.0
ultima_vez = {}

def conectar_arduino():
    while True:
        try:
            arduino = serial.Serial(puerto, velocidad)
            print(f'✅ Conectado al Arduino en {puerto}. Escuchando señales IR...')
            return arduino
        except serial.SerialException as e:
            print(f"❌ No se pudo abrir el puerto {puerto}: {e}")
            print("🔁 Reintentando en 5 segundos...")
            time.sleep(5)

arduino = conectar_arduino()

try:
    while True:
        try:
            linea = arduino.readline().decode('utf-8').strip().upper()
            if debug:
                print(f'📡 Señal IR capturada: {linea}')
            
            if not linea:
                continue

            ahora = time.time()

            if linea in acciones:
                ultima = ultima_vez.get(linea, 0)
                if ahora - ultima < cooldown:
                    if debug:
                        print(f"⏳ Ignorado por cooldown: {acciones[linea]['nombre']}")
                    continue

                ultima_vez[linea] = ahora

                accion = acciones[linea]
                print(f"🚀 Ejecutando: {accion['nombre']}")
                script = os.path.expanduser(accion['script'])
                subprocess.Popen(f"bash -c \"{script}\"", shell=True)

        except serial.SerialException as e:
            print(f"⚠️  Conexión perdida con el Arduino: {e}")
            print("🔌 Intentando reconectar...")
            arduino.close()
            arduino = conectar_arduino()

except KeyboardInterrupt:
    print("\n👋 Saliendo del programa...")
    arduino.close()

