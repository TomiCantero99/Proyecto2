from PIL import Image, ImageOps, ImageFilter
import numpy as np
import matplotlib.pyplot as plt
import os
import requests
import cv2
from io import BytesIO

# ----------------------------
# 1) Función para leer/redimensionar según la red social
# ----------------------------

sizes = {
    "instagram": (1080, 1350),
    "facebook": (1200, 630),
    "twitter": (1600, 900),
    "youtube": (1280, 720)
}

def cargar_y_redimensionar(ruta, plataforma):
    plataforma = plataforma.lower()

    if plataforma not in sizes:
        raise ValueError("Plataforma no válida. Usa Instagram, Facebook, Twitter o Youtube.")

    # Leer imagen desde Drive o URL
    try:
        if ruta.startswith("http"):
            img = Image.open(BytesIO(requests.get(ruta).content))
        else:
            img = Image.open(ruta)
    except:
        raise FileNotFoundError("Error al cargar la imagen.")

    # Redimensionar sin deformar (mantener proporción)
    img.thumbnail(sizes[plataforma])

    return img


# ----------------------------
# 2) Ajuste de contraste usando histograma (ecualización)
# ----------------------------

def ecualizar_contraste(img):
    img_gray = img.convert("L")
    ecualizada = ImageOps.equalize(img_gray)
    return ecualizada


# ----------------------------
# 3) Aplicación de filtros Pillow
# ----------------------------

filtros = {
    "blur": ImageFilter.BLUR,
    "contour": ImageFilter.CONTOUR,
    "detail": ImageFilter.DETAIL,
    "edge_enhance": ImageFilter.EDGE_ENHANCE,
    "edge_enhance_more": ImageFilter.EDGE_ENHANCE_MORE,
    "emboss": ImageFilter.EMBOSS,
    "find_edges": ImageFilter.FIND_EDGES,
    "sharpen": ImageFilter.SHARPEN,
    "smooth": ImageFilter.SMOOTH
}

def aplicar_filtro(img, filtro):
    filtro = filtro.lower()
    if filtro not in filtros:
        raise ValueError("Filtro no reconocido.")
    return img.filter(filtros[filtro])


# ----------------------------
# 4) Boceto para pintores (detección de bordes)
# ----------------------------

def boceto(img):
    img_gray = img.convert("L")
    edges = img_gray.filter(ImageFilter.SMOOTH)
    edges = cv2.Canny(img_gray, 126, 128)
    return edges


# ----------------------------
# 5) Menú interactivo
# ----------------------------

def menu():
    img = None
    while True:
        print("\n--- FOTOAPP MENU ---")
        print("1. Cargar imagen")
        print("2. Ecualizar contraste")
        print("3. Aplicar filtro")
        print("4. Generar boceto")
        print("5. Salir")

        opcion = input("Elija una opción: ")

        try:
            if opcion == "1":
                ruta = input("Ruta o URL: ")
                plataforma = input("Plataforma: ")
                img = cargar_y_redimensionar(ruta, plataforma)
                print("Imagen cargada.")

            elif opcion == "2":
                if img is None:
                    raise Exception("Primero debe cargar una imagen.")
                resultado = ecualizar_contraste(img)
                resultado.show()

            elif opcion == "3":
                if img is None:
                    raise Exception("Primero debe cargar una imagen.")
                filtr = input("Filtro: ")
                resultado = aplicar_filtro(img, filtr)
                resultado.show()

            elif opcion == "4":
                if img is None:
                    raise Exception("Primero debe cargar una imagen.")
                resultado = boceto(img)
                resultado.show()

            elif opcion == "5":
                break

        except Exception as e:
            print("Error:", e)