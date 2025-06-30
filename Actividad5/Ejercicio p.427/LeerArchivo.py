import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

# Función para leer el contenido del archivo y mostrarlo en el área de texto
def ver_contenido():
    try:
        with open("prueba.txt", "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, contenido)
            label_estado.config(text="")
    except Exception as e:
        text_area.delete("1.0", tk.END)
        label_estado.config(text="No se pudo leer el archivo.")

# Ventana principal
ventana = tk.Tk()
ventana.title("Lector de Archivos")
ventana.geometry("400x300")
ventana.resizable(False, False)

# Etiqueta superior
label_titulo = tk.Label(ventana, text="Contenido del Archivo", font=("Arial", 12))
label_titulo.pack(pady=10)

# Área de texto con scroll
text_area = scrolledtext.ScrolledText(ventana, width=40, height=8, font=("Arial", 10))
text_area.pack(pady=5)

# Botón para ver contenido
boton_ver = tk.Button(ventana, text="Ver Contenido", command=ver_contenido, width=20)
boton_ver.pack(pady=10)

# Etiqueta para mostrar mensajes de error
label_estado = tk.Label(ventana, text="", fg="red", font=("Arial", 10))
label_estado.pack(pady=5)

ventana.mainloop()
