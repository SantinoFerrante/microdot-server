from microdot import Microdot, send_file  # Importamos la clase Microdot para crear una aplicación web y send_file para enviar archivos
from machine import Pin, PWM  # Importamos las clases Pin y PWM para manejar los pines de la placa
import time  # Importamos el módulo time para manejar funciones relacionadas con el tiempo

app = Microdot()  # Creamos una instancia de la clase Microdot para nuestra aplicación

# Definimos los pines de los LEDs como salidas
led_red = Pin(32, Pin.OUT)  # Pin 32 para el LED rojo
led_green = Pin(33, Pin.OUT)  # Pin 33 para el LED verde
led_blue = Pin(25, Pin.OUT)  # Pin 25 para el LED azul

# Definimos la ruta principal de la aplicación
@app.route('/')  
async def home(request):
    return send_file('index.html')  # Retornamos el archivo index.html al acceder a la ruta raíz





@app.route('/<dir>/<file>') # Definimos la ruta con dos parámetros
async def index(request, dir, file):
    return send_file("/" + dir + "/" + file) # Cambiamos el nombre del archivo a enviar



@app.route('/toggle/led/<int:id>') # Definimos la ruta con un parámetro entero
async def index(request, id):

    # Dependiendo del valor del parámetro id, encendemos o apagamos un LED
    if id == 1:
        LED1.value(not LED1.value())

    elif id == 2:
        LED2.value(not LED2.value())

    elif id == 3:
        LED3.value(not LED3.value())

    return 'OK'

# Corremos el servidor creado en el puerto 80
app.run(port=80)