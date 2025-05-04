# La temperatura sube...

## Explicación del código

Importamos dos módulos: **urllib.request** y **json**.

`import urllib.request, json`

Definimos la función principal del programa **show_menu_weather_app()**.

`def show_menu_weather_app():`

Declaramos la variable **option_menu** y le asignamos el valor **-1**.

`option_menu = -1`

Definimos un bucle **while** cuya condición de ejecución es que el valor de la variable **option_menu** sea distinto de **0**. Cuando la condición se evalúa como verdadera, se imprimen las siguientes cadenas de texto: **Weather App Menu**, **1. Barcelona**, **2. Madrid**, **3. Berlin**, **4. London**, **5. Paris**, **6.New York**, **0. Exit**.

```
while option_menu != 0:
  print("--- Weather App Menu ---")
  print("1. Barcelona")
  print("2. Madrid")
  print("3. Berlin")
  print("4. London")
  print("5. Paris")
  print("6. New York")
  print("0. Exit")
```

Luego, asignamos a la variable **option_menu** el valor ingresado por el usuario mediante la función **input()** y mostramos al usuario la siguiente cadena de texto: **Choose an option (0-6):**.

`option_menu = input("Choose an option (0-6): ")`

Comprobamos que el valor ingresado por el usuario sea un dígito mediante la función **isdigit()**.

`if option_menu.isdigit():`

Si se cumple dicha condición convertimos el valor en un número entero mediante el *casting* de **option_menu**.

`option_menu = int(option_menu)`

Utilizamos la estructura **match** para evaluar los diferentes casos (**case**) del valor de **option_menu**. Dentro de cada caso, se invoca la función **show_weather(city_name, latitude, longitude)**, la cual acepta tres parámetros (el nombre, la latitud y la longitud de la ciudad). Si el usuario ingresa el número **1**, se mostrará la opción del tiempo en Barcelona.

```
match option_menu:
  case 0:
    print("Goodbye.")
  case 1:
    show_weather("Barcelona", 41.3888, 2.159)
  case 2:
    show_weather("Madrid", 40.4165, -3.7026)
  case 3:
    show_weather("Berlin", 52.5244, 13.4105)
  case 4:
    show_weather("London", 51.5085, -0.1257)
  case 5:
    show_weather("Paris", 48.8534, 2.3488)
  case 6:
    show_weather("New York", 40.7143, -74.006)
  case _:
    print("Please, enter a number between 0 and 6.")
```

Si la entrada no es un número, se imprime el mensaje: **Error: You must enter a valid number.**

```
else:
  print("Error: You must enter a valid number.")
```

Definimos la función **show_weather(city_name, latitude, longitude)**.

`def show_weather(city_name, latitude, longitude):`

Asignamos a la variable **url_weather** el enlace a la API de Open-Meteo.

> [!NOTE]
> El *casting* de *latitude* y *longitude* mejora la escalabilidad del código.

`url_weather = "https://api.open-meteo.com/v1/forecast?latitude=" + str(latitude) + "&longitude=" + str(longitude) + "&current=temperature_2m,wind_speed_10m,relative_humidity_2m"`

Utilizamos la función **urlopen()** del módulo **urllib.request** para abrir una conexión a la URL de la API (**url_weather**). El uso de **with as data:** garantiza que la conexión a la API se gestione de manera segura, cerrándose automáticamente al finalizar el bloque de código (incluso si ocurren errores durante la lectura).

`with urllib.request.urlopen(url_weather) as data:`

Utilizamos la función **load()** del módulo **json** para parsear los datos que están en formato JSON y convertirlos en una estructura de datos de Python (generalmente un diccionario o una lista). El resultado de esta conversión se guarda en la variable **parsed**.

`parsed = json.load(data)`

Imprimimos **The weather in** y el nombre de la ciudad que ha escogido el usuario.

`print("--- The weather in " + str(city_name) + " ---")`

Imprimimos **Temperature** y la temperatura que hace en la ciudad que ha escogido el usuario.

`print("Temperature:", parsed["current"]["temperature_2m"])`

Imprimimos **Wind speed** y la velocidad del viento que hace en la ciudad que ha escogido el usuario.

`print("Wind speed:", parsed["current"]["wind_speed_10m"])`

Imprimimos **Relative humidity** y la humedad relativa que hace en la ciudad que ha escogido el usuario.

`print("Relative humidity:", parsed["current"]["relative_humidity_2m"])`




