""" 21 - Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3. """

import pygame
pygame.mixer.init()  #Inicializa o mixer do PyGame
pygame.init()  #Inicializa o PyGame
pygame.mixer.music.load('ex021.mp3')  #Importa a música
pygame.mixer.music.play()  #Toca
pygame.event.wait()
