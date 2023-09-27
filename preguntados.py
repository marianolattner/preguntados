# Desafío Preguntados
# Preguntados es una franquicia de entretenimiento de plataformas y una de las marcas más
# exitosas de la división de Gaming de Etermax.
# Preguntados es principalmente un juego de preguntas y respuestas de Cultura General tipo
# trivia. Digamos que este es el apartado en el que cabrían cuestiones de todo tipo. Si controlas
# datos históricos, orígenes de comidas, literatura y curiosidades de todo tipo, lograrás una buena
# puntuación.
# Recientemente Etermax ha decidido desarrollar el juego en Python, y para acceder a las
# entrevistas es necesario completar el siguiente desafío.
# La empresa compartió con todos los participantes cierta información confidencial de un grupo
# de preguntas y respuestas. Y semana a semana enviará una lista con los nuevos requerimientos.
# Quien supere todas las etapas accederá a una entrevista con el director para de la compañía.

# A. Analizar detenidamente el set de datos.
# B. Recorrer la lista guardando en sub-listas: la pregunta, cada opción y la respuesta
# correcta.
# C. Crear 2 botones (rectángulos) uno con la etiqueta “Pregunta”, otro con la etiqueta
# “Reiniciar”
# D. Imprimir el Score: 999 donde se va a ir acumulando el puntaje de las respuestas
# correctas. Cada respuesta correcta suma 10 puntos.
# E. Al hacer clic en el botón (rectángulo) “Pregunta” debe mostrar las preguntas
# comenzando por la primera y las tres opciones, cada clic en este botón pasa a la
# siguiente pregunta.
# F. Al hacer clic en una de las tres palabras que representa una de las tres opciones, si es
# correcta, debe sumar el score y dejar de mostrar las opciones.
# G. Solo tiene 2 opciones para acertar la respuesta correcta y sumar puntos, si agotó ambas
# opciones, deja de mostrar las opciones y no suma score
# H. Al hacer clic en el botón (rectángulo) “Reiniciar” debe mostrar las preguntas
# comenzando por la primera y las tres opciones, cada clic pasa a la siguiente pregunta.
# También debe reiniciar el Score.

import pygame
from datos_preguntados import *
from constantes import *
from funciones_preguntados import separar_lista


lista_preguntas = separar_lista(lista, "pregunta")
lista_respuestas_a = separar_lista(lista, "a")
lista_respuestas_b = separar_lista(lista, "b")
lista_respuestas_c = separar_lista(lista, "c")
lista_respuestas_correctas = separar_lista(lista, "correcta")


pygame.init()


pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Preguntados")


imagen = pygame.image.load("Preguntados.jpg")
imagen = pygame.transform.scale(imagen, (200, 200))
pygame.mixer.music.load("sonido_fondo.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.05)
sonido_correcto = pygame.mixer.Sound("sonido_correcto.mp3")
sonido_incorrecto = pygame.mixer.Sound("sonido_incorrecto.mp3")


fuente = pygame.font.SysFont("Arial", 35)
texto_reiniciar = fuente.render("REINICIAR", True, COLOR_GRIS)
texto_siguiente_pregunta = fuente.render("PREGUNTA", True, COLOR_GRIS)
texto_score = fuente.render("SCORE", True, COLOR_GRIS)
texto_pregunta = fuente.render("", True, COLOR_GRIS)
texto_respuesta_a = fuente.render("", True, COLOR_GRIS)
texto_respuesta_b = fuente.render("", True, COLOR_GRIS)
texto_respuesta_c = fuente.render("", True, COLOR_GRIS)
texto_puntaje = fuente.render("0", True, COLOR_GRIS)
texto_fin_juego = fuente.render("GAME OVER", True, COLOR_GRIS)


posicion = 0
puntaje = 0
errores = 0
bandera_correcta = False
bandera_fin_juego = False


flag_corriendo = True
respuesta_seleccionada = ""

while flag_corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            flag_corriendo = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            posicion_click = list(evento.pos)
            
            # Lógica para el botón "PREGUNTA"
            if (300 < posicion_click[0] < 490) and (20 < posicion_click[1] < 80):
                if not bandera_correcta and posicion < len(lista_preguntas):  # Agregar comprobación
                    pregunta = lista_preguntas[posicion]
                    respuesta_a = lista_respuestas_a[posicion]
                    respuesta_b = lista_respuestas_b[posicion]
                    respuesta_c = lista_respuestas_c[posicion]

                    texto_pregunta = fuente.render(str(pregunta), True, COLOR_GRIS)
                    texto_respuesta_a = fuente.render(str(respuesta_a), True, COLOR_GRIS)
                    texto_respuesta_b = fuente.render(str(respuesta_b), True, COLOR_GRIS)
                    texto_respuesta_c = fuente.render(str(respuesta_c), True, COLOR_GRIS)
                    bandera_correcta = True
                    errores = 0

            # Lógica para el botón "REINICIAR"
            elif (300 < posicion_click[0] < 500) and (534 < posicion_click[1] < 594):
                puntaje = 0
                posicion = 0
                errores = 0
                respuesta_seleccionada = ""
                texto_puntaje = fuente.render(str(puntaje), True, COLOR_GRIS)
                texto_pregunta = fuente.render("", True, COLOR_GRIS)
                texto_respuesta_a = fuente.render("", True, COLOR_GRIS)
                texto_respuesta_b = fuente.render("", True, COLOR_GRIS)
                texto_respuesta_c = fuente.render("", True, COLOR_GRIS)
                bandera_correcta = False
                bandera_fin_juego = False

            # Lógica para seleccionar respuestas
            elif (16 < posicion_click[0] < 210) and (400 < posicion_click[1] < 450):
                respuesta_seleccionada = "a"
            elif (300 < posicion_click[0] < 447) and (400 < posicion_click[1] < 450):
                respuesta_seleccionada = "b"
            elif (549 < posicion_click[0] < 775) and (400 < posicion_click[1] < 450):
                respuesta_seleccionada = "c"

            # Verificar si la respuesta seleccionada es correcta
            if posicion < len(lista_respuestas_correctas):
                if respuesta_seleccionada == lista_respuestas_correctas[posicion] and errores < 2:
                    puntaje += 10
                    texto_puntaje = fuente.render(str(puntaje), True, COLOR_GRIS)
                    sonido_correcto.play()
                    posicion += 1
                    bandera_correcta = False
                elif respuesta_seleccionada != "" and respuesta_seleccionada != lista_respuestas_correctas[posicion]:
                    errores += 1
                    sonido_incorrecto.play()
                    if respuesta_seleccionada == "a":
                        respuesta_a = ""
                        texto_respuesta_a = fuente.render(str(respuesta_a), True, COLOR_GRIS)
                    elif respuesta_seleccionada == "b":
                        respuesta_b = ""
                        texto_respuesta_b = fuente.render(str(respuesta_b), True, COLOR_GRIS)
                    elif respuesta_seleccionada == "c":
                        respuesta_c = ""
                        texto_respuesta_c = fuente.render(str(respuesta_c), True, COLOR_GRIS)
                    if errores == 2:
                        posicion += 1
                        bandera_correcta = False


            respuesta_seleccionada = ""


            if posicion >= len(lista_preguntas):
                bandera_fin_juego = True
                bandera_correcta = False

    pantalla.fill(COLOR_AZUL)
    pygame.draw.rect(pantalla, COLOR_VERDE, (300, 20, 200, 60))
    pygame.draw.rect(pantalla, COLOR_VERDE, (300, 534, 200, 60))

    if bandera_fin_juego:
        pantalla.fill(COLOR_AMARILLO)
        pantalla.blit(texto_fin_juego, (310, 300))
        pregunta = ""
        texto_pregunta = fuente.render(str(pregunta), True, COLOR_GRIS)
        texto_reiniciar = fuente.render("", True, COLOR_GRIS)
        texto_siguiente_pregunta = fuente.render("", True, COLOR_GRIS)
    elif bandera_correcta and errores < 2:
        pantalla.blit(texto_respuesta_a, (16, 400))
        pantalla.blit(texto_respuesta_b, (300, 400))
        pantalla.blit(texto_respuesta_c, (549, 400))

    pantalla.blit(imagen, (POSICION_IMAGEN))
    pantalla.blit(texto_siguiente_pregunta, (310, 30))
    pantalla.blit(texto_reiniciar, (310, 550))
    pantalla.blit(texto_pregunta, (20, 300))
    pantalla.blit(texto_score, (310, 120))
    pantalla.blit(texto_puntaje, (310, 160))

    pygame.display.flip() 

pygame.quit()
