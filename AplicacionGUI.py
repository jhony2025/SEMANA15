# ---------------------------------------------------
# APLICACIÓN GUI - LISTA DE TAREAS
# Autor: [Tu Nombre]
# Descripción:
# Aplicación en Tkinter que permite gestionar una lista de tareas:
# Añadir, marcar como completadas y eliminar.
# Incluye personalización de colores y fuentes.
# ---------------------------------------------------

import tkinter as tk
from tkinter import messagebox

# ---------------- Funciones ----------------
def agregar_tarea(event=None):
    """Agrega una nueva tarea al Listbox si no está vacía."""
    tarea = entrada_tarea.get().strip()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada vacía", "Por favor, escribe una tarea.")

def marcar_completada():
    """Marca la tarea seleccionada como completada cambiando su apariencia."""
    try:
        indice = lista_tareas.curselection()[0]
        tarea = lista_tareas.get(indice)
        # Si ya está marcada, la restauramos
        if tarea.startswith("✔ "):
            lista_tareas.delete(indice)
            lista_tareas.insert(indice, tarea[2:])
        else:
            lista_tareas.delete(indice)
            lista_tareas.insert(indice, "✔ " + tarea)
    except IndexError:
        messagebox.showinfo("Selección requerida", "Selecciona una tarea para marcarla.")

def eliminar_tarea():
    """Elimina la tarea seleccionada del Listbox."""
    try:
        indice = lista_tareas.curselection()[0]
        lista_tareas.delete(indice)
    except IndexError:
        messagebox.showinfo("Selección requerida", "Selecciona una tarea para eliminarla.")

def marcar_doble_click(event):
    """Marca o desmarca como completada al hacer doble clic."""
    marcar_completada()

# ---------------- Ventana Principal ----------------
ventana = tk.Tk()
ventana.title("Lista de Tareas - Tkinter")
ventana.geometry("500x500")
ventana.configure(bg="#E8F0F2")

# ---------------- Widgets ----------------
# Título
titulo = tk.Label(ventana, text="📌 Mi Lista de Tareas", 
                  font=("Arial", 18, "bold"), bg="#E8F0F2", fg="#2C3E50")
titulo.pack(pady=10)

# Entrada de texto
entrada_tarea = tk.Entry(ventana, font=("Arial", 14), width=30, bg="#FDFEFE", fg="#34495E")
entrada_tarea.pack(pady=5)

# Botones
frame_botones = tk.Frame(ventana, bg="#E8F0F2")
frame_botones.pack(pady=10)

btn_agregar = tk.Button(frame_botones, text="➕ Añadir Tarea", command=agregar_tarea,
                        font=("Arial", 12), bg="#2ECC71", fg="white", width=15)
btn_agregar.grid(row=0, column=0, padx=5)

btn_completar = tk.Button(frame_botones, text="✔ Marcar Completada", command=marcar_completada,
                          font=("Arial", 12), bg="#F39C12", fg="white", width=18)
btn_completar.grid(row=0, column=1, padx=5)

btn_eliminar = tk.Button(frame_botones, text="🗑 Eliminar Tarea", command=eliminar_tarea,
                         font=("Arial", 12), bg="#E74C3C", fg="white", width=15)
btn_eliminar.grid(row=0, column=2, padx=5)

# Lista de tareas
lista_tareas = tk.Listbox(ventana, font=("Arial", 14), width=40, height=12, 
                          selectbackground="#85C1E9", bg="white", fg="#2C3E50")
lista_tareas.pack(pady=10)

# ---------------- Eventos ----------------
ventana.bind("<Return>", agregar_tarea)        # Presionar Enter añade tarea
lista_tareas.bind("<Double-1>", marcar_doble_click)  # Doble clic marca como completada

# ---------------- Bucle Principal ----------------
ventana.mainloop()
