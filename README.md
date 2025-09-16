El proyecto `brickBreaker-opencv` es el clasico juego de rompe bloques solo que este utiliza visión por computadora para el control mediante gestos de manos. El juego integra MediaPipe para detección de manos, OpenCV para procesamiento de video y Pygame para renderizado.

### Características principales implementadas:

**Control por gestos:** El juego detecta la posición del dedo índice para controlar la paleta, reemplazando controles tradicionales de teclado/mouse.

**Mecánicas de juego clásicas:** Incluye física de pelota con rebotes, detección de colisiones con paredes, paleta y bloques.

**Sistema de bloques:** Grid de 4x8 bloques (32 total) que se destruyen al contacto con la pelota.

**Renderizado en tiempo real:** Combina el feed de cámara como fondo con elementos del juego a 30 FPS.

## Instalación

### Requisitos previos
- Python 3.7 o superior
- Cámara web funcional
- Sistema operativo: Windows, macOS o Linux

### Dependencias necesarias

Instala las librerías requeridas usando pip:

```bash
pip install pygame opencv-python mediapipe numpy
```

### Instalación del proyecto

1. Clona el repositorio:
```bash
git clone https://github.com/Juand4rck12/brickBreaker-opencv.git
cd brickBreaker-opencv
```

2. Verifica que tienes todos los archivos necesarios:
   - `rompe.py` (archivo principal)
   - `paddle.png` (imagen de la paleta)
   - `esfera.png` (imagen de la pelota)
   - `ladrillo.png` (imagen de los bloques)

## Uso

### Ejecutar el juego

```bash
python rompe.py
```

### Controles

- **Control de la paleta:** Muestra tu mano frente a la cámara y mueve tu dedo índice horizontalmente para controlar la paleta.
- **Salir del juego:** Presiona la tecla `ESC` para cerrar el juego.

### Configuración de cámara

El juego utiliza la cámara predeterminada del sistema (índice 0). Si tienes múltiples cámaras, puedes cambiar el índice en la línea correspondiente del código.

### Consejos para mejor experiencia

- Asegúrate de tener buena iluminación para una mejor detección de manos
- Mantén tu mano visible en el campo de visión de la cámara
- El juego detecta una sola mano para evitar conflictos de control 

## Tecnologías utilizadas

- **MediaPipe:** Para detección y seguimiento de landmarks de manos
- **OpenCV:** Captura y procesamiento de video de cámara
- **Pygame:** Motor de renderizado y gestión de sprites
- **NumPy:** Manipulación de arrays para procesamiento de imágenes

## Estructura del proyecto

- `rompe.py`: Archivo principal con toda la lógica del juego
- `paddle.png`, `esfera.png`, `ladrillo.png`: Assets visuales del juego
- Licencia Apache 2.0 para uso permisivo

## Licencia

Este proyecto está licenciado bajo la Licencia Apache 2.0.
