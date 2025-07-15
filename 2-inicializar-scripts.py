import os

# Directorio donde se crearán los scripts
base_dir = os.path.expanduser("~/scripts_ir")

# Scripts y comandos asociados
scripts = {
    "subir_volumen.sh": "pactl set-sink-volume @DEFAULT_SINK@ +5%",
    "bajar_volumen.sh": "pactl set-sink-volume @DEFAULT_SINK@ -5%",
    "toggle_mute.sh": "pactl set-sink-mute @DEFAULT_SINK@ toggle",
    "subir_brillo.sh": "brightnessctl set +10%",
    "bajar_brillo.sh": "brightnessctl set 10%-",
    "play.sh": "playerctl play",
    "pause.sh": "playerctl pause",
    "stop.sh": "playerctl stop",
    "anterior.sh": "playerctl previous",
    "adelantar_tema.sh": "playerctl next",
    "apagar_pantalla.sh": "xset dpms force off",
    "suspender.sh": "systemctl suspend",
    "mostrar_info.sh": "notify-send 'Info' \"$(date)\"",
    "cambiar_salida_audio.sh": "pactl set-default-sink 1",
    "captura.sh": "scrot ~/Imágenes/captura_$(date +%s).png",
    "grabar.sh": "notify-send 'Grabando (ficticio)'",
    "toggle_stereo.sh": "notify-send 'Alternando modo estéreo (placeholder)'",
    "timeshift.sh": "notify-send 'Timeshift (ficticio)'",
    "radio.sh": "vlc http://stream-uk1.radioparadise.com/aac-320",
    "enter.sh": "xdotool key Return",
    "app_anterior.sh": "wmctrl -a $(wmctrl -l | tail -n 1 | cut -d' ' -f1)",
    "bloquear_sesion.sh": "loginctl lock-session",
    "foto_webcam.sh": "fswebcam ~/Imágenes/webcam_$(date +%s).jpg"
}

# Crear carpeta y scripts
os.makedirs(base_dir, exist_ok=True)

for nombre, comando in scripts.items():
    ruta = os.path.join(base_dir, nombre)
    with open(ruta, "w") as archivo:
        archivo.write(f"#!/bin/bash\n{comando}\n")
    os.chmod(ruta, 0o755)

print(f"Scripts creados en: {base_dir}")

