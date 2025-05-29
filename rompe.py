# Librerias necesarias
import pygame # Para el juego
import cv2 # Para la camara
import mediapipe as mp # Para el reconocimiento de manos
import numpy as np

# Se inicializan los módulos de pygame y MediaPipe para el reconocimiento y dibujo de manos
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
pygame.init()

WIDTH, HEIGHT = 800, 600 # Se define el tamaño de la ventana del juego
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego Rompe Bloques") # Titulo de la ventana del juego
running = True

paddle_image = pygame.image.load('paddle.png')
paddle_image = pygame.transform.scale(paddle_image, (150, 40))
paddle_x, paddle_y = WIDTH // 2, HEIGHT - 100
paddle_speed = 10

ball_image = pygame.image.load('esfera.png')
ball_image = pygame.transform.scale(ball_image, (40, 40))
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_speed_x, ball_speed_y = 8, 8
ball_radius = 20

block_image = pygame.image.load('ladrillo.png')
block_rows, block_columns = 4, 8 # 4 filas por 8 columnas
block_width, block_height = WIDTH // block_columns, 50
block_image = pygame.transform.scale(block_image, (block_width, block_height))

blocks = []

for row in range(block_rows):
    for col in range(block_columns):
        blocks.append(pygame.Rect(col * block_width,
                                  row * block_height,
                                  block_width,
                                  block_height))


cap = cv2.VideoCapture(0) # se inicia la captura de video frame por frame desde la camara

with mp_hands.Hands(min_detection_confidence = 0.5,
                    min_tracking_confidence = 0.5,
                    max_num_hands = 1) as hands:
    while running:
        ret, frame = cap.read()
        
        if not ret:
            break
        
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(rgb_frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        rgb_frame = cv2.resize(rgb_frame, (WIDTH, HEIGHT))
        rgb_frame = np.rot90(rgb_frame)  # Corrige la orientación para Pygame
        rgb_surface = pygame.surfarray.make_surface(rgb_frame)
        screen.blit(rgb_surface, (0, 0))
        
        for block in blocks:
            screen.blit(block_image, (block.x, block.y))
            
        pygame.display.flip()
        
        # cv2.imshow('Titulo CV2', frame) linea de prueba para ver si funciona
        
        if cv2.waitKey(1) & 0xFF == 27:
            break


cap.release()
cv2.destroyAllWindows()




