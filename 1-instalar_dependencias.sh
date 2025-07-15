#!/bin/bash

echo "🔧 Instalando dependencias necesarias..."

sudo apt update
sudo apt install -y \
  playerctl \
  brightnessctl \
  pulseaudio \
  scrot \
  vlc \
  xdotool \
  wmctrl \
  fswebcam \
  libnotify-bin

echo "✅ Dependencias instaladas correctamente."

