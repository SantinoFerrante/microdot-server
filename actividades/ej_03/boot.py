def connect_to_wifi():
    import network  # Se importa el módulo para manejo de red

    wifi_interface = network.WLAN(network.STA_IF)  # Inicializa la interfaz Wi-Fi en modo cliente

    if not wifi_interface.isconnected():
        print('Conectando a la red Wi-Fi...')
        wifi_interface.active(True)  # Activa la interfaz Wi-Fi
        wifi_interface.connect('Cooperadora Alumnos', '')  # Intenta conectarse a la red especificada
        while not wifi_interface.isconnected():
            pass  # Espera hasta que se establezca la conexión
    print('Configuración de red:', wifi_interface.ifconfig())  # Imprime los detalles de la conexión (IP, máscara, etc.)


# Configuracion inicial
