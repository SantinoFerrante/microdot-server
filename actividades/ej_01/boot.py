def do_connect():
    # Importar el módulo de red para manejar conexiones Wi-Fi
    import network
    
    # Crear una instancia del interface de estación (STA) de Wi-Fi
    sta_if = network.WLAN(network.STA_IF)
    
    # Verificar si el dispositivo ya está conectado a la red
    if not sta_if.isconnected():
        print('connecting to network...')  # Imprimir un mensaje indicando que se está intentando conectar
        sta_if.active(True)  # Activar el interface de estación (STA)
        
        # Intentar conectarse a la red Wi-Fi especificada
        sta_if.connect("Cooperadora Alumnos", "")  # Aquí se especifica el nombre de la red y la contraseña (vacía en este caso)
        
        # Esperar hasta que se establezca la conexión
        while not sta_if.isconnected():
            print(".", end="25")  # Imprimir un punto cada vez que se verifica la conexión
        
    # Imprimir la configuración de la red una vez conectado
    print('network config:', sta_if.ifconfig())
    
# Llamar a la función para iniciar el proceso de conexión
do_connect()
