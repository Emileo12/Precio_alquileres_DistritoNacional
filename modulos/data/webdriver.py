from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def iniciar_chrome():

    # Instalamos la version de chromedriver correspondiente
    ruta = ChromeDriverManager().install()
    # Opciones de Chrome:
    options = Options()
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
    options.add_argument(f"user-agent={user_agent}") #Definimos un user agent personalizado
    options.add_argument("--window-size=1000,1000") #Configurar el alto y ancho de la ventana
    #options.add_argument("--start-maximized") #para maximizar la ventana (usar este o el window size)
    options.add_argument("--disable-web-security") #Deshabilita la politica del mismo origen o Same Origin Policy
    options.add_argument("--disable-extensions") #Para que no cargue las extensiones de chrome
    options.add_argument("--disable-notifications") #bloquea las notificaciones de chrome
    options.add_argument("--ignore-certificate-errors") #Para ignorar el aviso de su conexion no es privada
    options.add_argument("--no-sandbox") #deshabilita el modo sandbox
    options.add_argument("--log-level=3") #para que chromedireve no muestre nada en la terminal
    options.add_argument("--allow-running-insecure-content") #desactiva el aviso de contenido no seguro
    options.add_argument("--no-default-browser-check") #Evita el aviso de que chrome no es el navegador por defecto
    options.add_argument("--no-first-run") #Evita la ejecucion de ciertas tareas que se realizan la primera vez que se ejecuta chrome
    options.add_argument("--no-proxy-server") #Para no usar proxy, sino conexiones directas
    options.add_argument("--disable-blink-features=AutomationControlled") #Evita que selenium sea detectado
    
    #Parametros a omitir en el inicio de chromedriver
    exp_opt = [
        'enable-automation', # para que no muestre la notificacion de un software automatizado de pruebas
        'ignore-certificate-errors', # para ignorar errores de certificados
        'enable-logging' # para que no se muestre en la terminal "devtools listening on..."
    ]

    options.add_experimental_option("excludeSwitches", exp_opt)
    
    # Parametros que definen preferencias en chromedriver
    prefs = {
        "profile.default_content_setting_values.notifications" : 2, # notificaciones, 0 = preguntar | 1 = permitir | 2 = no permitir
        "intl.accept_languages" : ["es-ES","es"], # para definir el idioma del navegador
        "credentials_enable_service" : False # para evitar que chrome pregunte si queremos guardar la contraseña
    }
    
    options.add_experimental_option("prefs",prefs)

    #instaciamos el servicio de chromedriver
    servicio = Service(ruta)
    
    #Instanciamos webdriver de selenium con Chrome
    driver = webdriver.Chrome(service=servicio, options=options)
    
    #Devolvemos el driver
    return driver

if __name__ == "__main__":
    driver = iniciar_chrome()
    input("Pulsa Enter para Salir...")
    driver.quit()