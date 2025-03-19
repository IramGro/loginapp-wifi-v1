import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time
import pickle
import webbrowser
import sys

def ejecutar_modificar(usuario, contra):
    try:
        # Configurar el driver de Selenium 
        time.sleep(3)
        edge_options = webdriver.EdgeOptions()
        edge_options.add_argument("--ignore-certificate-errors")
        driver = webdriver.Edge(options=edge_options)

        # Abrir la página de inicio de sesión
        url = 'http://192.0.2.1/login.html'
        driver.get(url)      
        driver.maximize_window()     
        time.sleep(3)
      
        # Ingresar el usuario y contraseña en los campos correspondientes
        username = driver.find_element(By.XPATH, "//td//input[@name='username']")
        username.send_keys(usuario)

        password = driver.find_element(By.XPATH, "//td//input[@name='password']")
        password.send_keys(contra)

        # Dar click en "Aceptar"
        submit = driver.find_element(By.XPATH, "//input[@name='Submit']").click()

        # Visitar una página web después del inicio de sesión
        google = 'https://www.google.com'
        driver.get(google)
        driver.quit()
        # Verificar conexión a Internet
        response = requests.get(google)
        
        if response.status_code == 200:
            messagebox.showinfo("", "Conexión exitosa a Internet.")
        else:
            messagebox.showwarning("Error", "No se pudo conectar a Internet.")

    except Exception as e:
        messagebox.showerror("Error", f"Usuario o contraseña incorrecta.")
        
        

    finally:
      
        # Cerrar el programa
        sys.exit()



def aceptar():
    # Obtener los datos de usuario y contraseña desde el .pkl
    usuario = entry_usuario.get()
    contra = entry_password.get()

    # Guardar los datos usuario y contraseña en un .pkl
    try:
        with open('.datos.pkl', 'wb') as f:
            pickle.dump((usuario, contra), f)
    except Exception as e:
        messagebox.showerror("Error", f"Error al guardar los datos: {str(e)}")
        
    ejecutar_modificar(usuario, contra)

# Crear la ventana principal
root = tk.Tk()
root.lift()
root.title("Login APP")

# Configurar el tamaño de la ventana
root.geometry("250x190")
root.resizable(width=False, height=False) 

# Configurar el color de fondo con transparencia
root['bg'] = 'black'
root.wm_attributes('-alpha', 0.78)  # Configurar el color de fondo

# Cargar los datos almacenados (si existen)
try:
    with open('.datos.pkl', 'rb') as f:
        usuario_guardado, contra_guardada = pickle.load(f)
except FileNotFoundError:
    usuario_guardado, contra_guardada = '', ''

# Función para cambiar el fondo de un widget
def cambiar_fondo(widget):
    widget.config(bg=root.cget('bg'), fg='white')




# Crear etiquetas y campos de entrada
label_usuario = tk.Label(root, text="Usuario:", fg="white", bg="#000000")
cambiar_fondo(label_usuario)
label_usuario.pack()


def usuario_aceptar(event):
    aceptar()

entry_usuario = tk.Entry(root)
cambiar_fondo(entry_usuario)
entry_usuario.pack(pady=5)
entry_usuario.insert(0, usuario_guardado)  
entry_usuario.configure(bg="#000000", insertbackground='white')
entry_usuario.bind("<Return>", usuario_aceptar)

# Darle el foco al entry del usuario al iniciar la aplicación
entry_usuario.focus()

label_password = tk.Label(root, text="Contraseña:", fg="white")
cambiar_fondo(label_password)
label_password.pack()

def pass_aceptar(event):
    aceptar()
    
entry_password = tk.Entry(root)
cambiar_fondo(entry_password)
entry_password.pack()
entry_password.insert(0, contra_guardada) 
entry_password.configure(bg="#000000", insertbackground='white')
entry_password.bind("<Return>", pass_aceptar)


# Botón de aceptar
btn_aceptar = tk.Button(root, text="Aceptar", command=aceptar, bg="black", fg="white")
cambiar_fondo(btn_aceptar)
btn_aceptar.pack(pady=20) 

# Boton del enlace webdrive Edge
def abrir_enlace_descarga():
    webbrowser.open("https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/")


# Label con enlace de descarga
link_label = tk.Label(root, text="Descarga Edge WebDriver", bg="black", fg="blue", cursor="hand2")
link_label.pack()
link_label.bind("<Button-1>", lambda e: abrir_enlace_descarga())

# Abrir al centro de la pantalla

root.update_idletasks() 
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = root.winfo_width()
window_height = root.winfo_height()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"+{x}+{y}")

# Autor
autor_label = tk.Label(root, text="by Coré Guerrero", bg="black", fg="white")
autor_label.pack(side=tk.RIGHT)

# Bucle de la interfaz
root.mainloop()