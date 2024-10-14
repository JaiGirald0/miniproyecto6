import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controller import user_repository
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
    
# Crear la ventana principal
master = tk.Tk()
master.title("Formulario de Registro")

def go_to_training():
    notebook.select(frame2)

# Crear un Notebook para gestionar pestañas
notebook = ttk.Notebook(master)
notebook.pack(pady=10)

# Pestaña de registro (puedes ajustar width y height)
frame1 = ttk.Frame(notebook, width=500, height=400)  # Modifiqué el tamaño de la pestaña
frame1.pack(fill="both", expand=True)
notebook.add(frame1, text="Registro")

# Pestaña de entrenamiento (puedes ajustar width y height)
frame2 = ttk.Frame(notebook, width=500, height=400)  # Modifiqué el tamaño de la pestaña
frame2.pack(fill="both", expand=True)
notebook.add(frame2, text="Entrenamiento")

# Etiquetas y campos de entrada en la pestaña de registro
tk.Label(frame1, text="Username:").grid(row=0)
tk.Label(frame1, text="name:").grid(row=1)
tk.Label(frame1, text="Password:").grid(row=2)
tk.Label(frame1, text="Occupation:").grid(row=3)

e1 = tk.Entry(frame1)
e2 = tk.Entry(frame1)
e3 = tk.Entry(frame1, show="*")
e4 = tk.Entry(frame1)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)



# Checkbuttons para seleccionar género
var1 = tk.IntVar()
tk.Checkbutton(frame1, text="Male", variable=var1).grid(row=4, sticky=tk.W)

var2 = tk.IntVar()
tk.Checkbutton(frame1, text="Female", variable=var2).grid(row=5, sticky=tk.W)

# Función para validar credenciales desde un archivo JSON
def validate_credentials():
    username = e1.get()
    password = e3.get()
    dataUsers = user_repository.load_users()
    for key,value in dataUsers.items():
        if "username" in value and "password" in value:
            if username == value["username"] and password == value["password"]:
                go_to_training()
                return 
        
    messagebox.showerror("Error", "Usuario o contraseña incorrectos")

# Validación de credenciales a través del boton "iniciar"
start_button = tk.Button(frame1, text="Iniciar", command=validate_credentials)
start_button.grid(row=6, columnspan=2, pady=10)

# Aqui metes las imagenes de las rutinas y demás
def routineWindows(routineName):
    newWindow = tk.Toplevel(master)
    newWindow.title(f"Rutina: {routineName}")
    
    # Aquí puedes agregar las imágenes o gifs para cada rutina
    label = tk.Label(newWindow, text=f"Insertar las imágenes y/o GIFs para {routineName}")
    label.pack(pady=20)
    
    # Si vas a ingresar imagenes, debes usar este formato
    # img_label = tk.Label(newWindow, image=tu_imagen)  # Sustituye 'tu_imagen' por el objeto de la imagen
    # img_label.pack()
    # Debajo de cada imagen que insertes, si deseas colocar un label, debes colocarlo
    # asi : 
    # label = Label(newWindow,text="¡Hola Mundo!")
    # label.pack()

# Botones para actividades de entrenamiento en la pestaña de entrenamiento
button1 = tk.Button(frame2, text="Brazo", command=lambda: routineWindows("Brazo"))
button2 = tk.Button(frame2, text="Espalda", command=lambda: routineWindows("Espalda"))
button3 = tk.Button(frame2, text="Pecho", command=lambda: routineWindows("Pecho"))
button4 = tk.Button(frame2, text="Pierna", command=lambda: routineWindows("Pierna"))
button5 = tk.Button(frame2, text="Full Body", command=lambda: routineWindows("Full Body"))

# Colocar los botones verticalmente
button1.grid(row=0, column=0, padx=5, pady=5)
button2.grid(row=0, column=1, padx=5, pady=5)
button3.grid(row=1, column=0, padx=5, pady=5)
button4.grid(row=1, column=1, padx=5, pady=5)
button5.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Pie de página
footer_label = tk.Label(master, text="BodyBuilder", fg="black")
footer_label.pack(pady=10)

# Ejecutar el bucle principal
master.mainloop()
