from boot import do_connect
from microdot import Microdot, send_file, Response
from machine import Pin
import ds18x20
import onewire
import time

# Configuración del pin para la alarma sonora y el sensor de temperatura
buzzer = Pin(14, Pin.OUT)  # Pin que controla la alarma (buzzer)
temp_sensor_pin = Pin(19)  # Pin conectado al sensor DS18B20
temp_sensor = ds18x20.DS18X20(onewire.OneWire(temp_sensor_pin))  # Inicializa el sensor de temperatura
current_temperature = 24  # Valor inicial de la temperatura (en °C)

# Conexión a la red Wi-Fi
do_connect()

# Instancia de la aplicación web
app = Microdot()

# Ruta principal que sirve la página HTML
@app.route('/')
async def serve_homepage(request):
    try:
        return send_file('index.html')  # Envía el archivo 'index.html'
    except OSError as error:
        return Response(body=f"Error: {error}", status_code=500)  # Error si no se encuentra el archivo

# Ruta para manejar archivos estáticos en subdirectorios
@app.route('/<folder>/<filename>')
async def serve_static_files(request, folder, filename):
    try:
        return send_file("/{}/{}".format(folder, filename))  # Devuelve el archivo solicitado
    except OSError as error:
        return Response(body=f"Error: {error}", status_code=404)  # Error si el archivo no existe

# Ruta para obtener la temperatura del sensor DS18B20
@app.route('/sensors/ds18b20/read')
async def read_temperature(request):
    global temp_sensor, current_temperature
    try:
        devices = temp_sensor.scan()  # Busca sensores conectados
        if not devices:
            raise ValueError("No se detectaron sensores DS18B20")  # Error si no hay sensores

        temp_sensor.convert_temp()  # Inicia la medición de temperatura
        time.sleep_ms(750)  # Tiempo necesario para completar la conversión
        
        for device in devices:
            current_temperature = temp_sensor.read_temp(device)  # Lee la temperatura del sensor
        
        response_data = {'temperature': current_temperature}  # Prepara la respuesta en formato JSON
        return response_data
    except (OSError, ValueError) as error:
        return Response(body=f"Error al obtener la temperatura: {error}", status_code=500)  # Error durante la lectura

# Ruta para comparar el valor de referencia con la temperatura y controlar la alarma
@app.route('/setpoint/set/<int:target_temp>')
async def compare_setpoint(request, target_temp):
    global current_temperature
    response_data = {}
    try:
        print("Evaluando el setpoint")  # Log de depuración
        if target_temp >= current_temperature:
            buzzer.on()  # Activa la alarma si el setpoint es mayor o igual a la temperatura actual
            response_data = {'buzzer': 'Encendido'}
        else:
            buzzer.off()  # Desactiva la alarma si el setpoint es menor
            response_data = {'buzzer': 'Apagado'}
        
        return response_data  # Devuelve el estado de la alarma
    except Exception as error:
        return Response(body=f"Error al evaluar el setpoint: {error}", status_code=500)  # Error genérico

# Ejecuta el servidor web en el puerto 80
app.run(port=80)

# Aplicacion del servidor
