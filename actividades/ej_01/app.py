from microdot import Microdot
from microdot import send_file

# Crear una instancia de la aplicación Microdot
app = Microdot()

# Definir la ruta para la página principal ("/")
@app.route('/')
async def index(request):
    # Enviar el archivo index.html cuando se accede a la ruta raíz
    return send_file("index.html")

# Definir una ruta dinámica para servir archivos estáticos
@app.route('/<dir>/<file>')
async def static(request, dir, file):
    # Servir un archivo específico ubicado en el directorio dado
    # `dir` es el nombre del directorio y `file` es el nombre del archivo
    return send_file("/" + dir + "/" + file)

# Iniciar la aplicación y escuchar las solicitudes
app.run()

