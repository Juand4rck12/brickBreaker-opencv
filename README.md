El proyecto `brickBreaker-opencv` es un juego de rompe bloques innovador que utiliza visión por computadora para el control mediante gestos de manos. El juego integra MediaPipe para detección de manos, OpenCV para procesamiento de video y Pygame para renderizado.

### Características principales implementadas:

**Control por gestos:** El juego detecta la posición del dedo índice para controlar la paleta, reemplazando controles tradicionales de teclado/mouse.

**Mecánicas de juego clásicas:** Incluye física de pelota con rebotes, detección de colisiones con paredes, paleta y bloques.

**Sistema de bloques:** Grid de 4x8 bloques (32 total) que se destruyen al contacto con la pelota.

**Renderizado en tiempo real:** Combina el feed de cámara como fondo con elementos del juego a 30 FPS.

### Tecnologías utilizadas:

- **MediaPipe:** Para detección y seguimiento de landmarks de manos
- **OpenCV:** Captura y procesamiento de video de cámara
- **Pygame:** Motor de renderizado y gestión de sprites
- **NumPy:** Manipulación de arrays para procesamiento de imágenes

### Estructura del proyecto:

- `rompe.py`: Archivo principal con toda la lógica del juego
- `paddle.png`, `esfera.png`, `ladrillo.png`: Assets visuales del juego
- Licencia Apache 2.0 para uso permisivo

El proyecto es una aplicación práctica de visión por computadora en entretenimiento interactivo, manteniendo la jugabilidad familiar del Brick Breaker clásico pero con una interfaz de control innovadora.
