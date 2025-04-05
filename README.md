# 🎙️ Voice Recorder - Grabador de Audio en Python

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![GitHub Repo](https://img.shields.io/badge/Repo-Open%20Source-success)
![GitHub Stars](https://img.shields.io/github/stars/LFDIAZDEV2209/voice-recorder?style=social)

Aplicación de línea de comandos para grabación de audio profesional con salida en formato WAV. Proyecto desarrollado con Python y librerías de procesamiento de audio de alto rendimiento.

![Demo](https://via.placeholder.com/800x400.png?text=Grabación+en+tiempo+real) <!-- Agregar captura real -->

## 🌟 Características Principales
- **Calidad de Estudio**: 44.1 kHz, 16-bit, estéreo
- **Auto-incremento de nombres de archivo** (out_1.wav, out_2.wav)
- **Sistema de grabación no bloqueante** usando multi-hilos
- **Control interactivo** mediante entrada de teclado
- **Optimización de recursos** con buffers en memoria
- **Formato WAV** estándar industrial
- **Multiplataforma**: Windows, Linux y macOS

## 📦 Instalación

### Requisitos previos
- Python 3.8 o superior
- Administrador de paquetes pip
- Permisos de micrófono

### Pasos de instalación
```bash
# Clonar repositorio
git clone https://github.com/LFDIAZDEV2209/voice-recorder.git
cd voice-recorder

# Instalar dependencias
pip install -r requirements.txt

## 📦 Dependencias
sounddevice==0.4.6
numpy==1.23.5
scipy==1.10.1

# Iniciar grabación
python recorder.py

# Durante la ejecución:
Grabando... Presiona ENTER para detener.

# Al detener:
Grabación detenida... Guardando archivo.
Archivo guardado como out_3.wav
Finalizado.
```

## Estructura del codigo
```python
# Configuración profesional
fs = 44100  # Frecuencia de muestreo estándar para audio de alta calidad
canales = 2  # Grabación estéreo
```

# Flujo de trabajo principal
1. Inicio de hilo de grabación
2. Captura de audio en buffer no bloqueante
3. Control de usuario por entrada de teclado
4. Concatenación de buffers y guardado en WAV