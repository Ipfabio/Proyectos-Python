import speech_recognition as sr   # Reconoce la voz
import pyttsx3  # Para escuchar SU voz
import pywhatkit  # Para que realice las acciones
import datetime
import wikipedia  # Para que realice busquedas en wikipedia

# Para que nos diga algo en concreto https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa3NHc0VZeGpDN0lleWFPdmNFVUxHUV9yZTNkUXxBQ3Jtc0ttaHA1UE9XazV1RlAtQTlFMWZvenV2WG5QaEJTLURmRDBVSm8zVHR5UHVIT1RPclo2YjhWWWZlNjBwaWJ4T1NIX2NmejM5bEJoR1FyUktKZlNORnJHLTZ1MS1SWlJNTzNjc3dDMHBNZmgyaGh1OVFNNA&q=https%3A%2F%2Fconsole.developers.google.com%2F&v=8WKjX0dbh4E
# Hay que generar la api key e ingresar a biblioteca youtube apiv3 y 'Habilitar'. En este caso no lo voy a hacer

# import urllib.request
# import json


name = 'Jarvis'  # Declaramos SU nombre
listener = sr.Recognizer()  # Nos reconoce

engine = pyttsx3.init()  # inicializamos

voices = engine.getProperty('voices')  # Regresa una lista de las voces
engine.setProperty('voice', voices[0].id)  # Establecemos una voz

# for voice in voices: Podemos iterar para ver los distintos registros de voces
#   print(voice)


def talk(text):
    engine.say(text)  # Diga el texto que le pasamos
    engine.runAndWait()


def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            voice = listener.listen(source)  # source = microphone
            # Utilizamos la api de google
            rec = listener.recognize_google(voice)
            rec = rec.lower()
            if name in rec:  # Si no decimos el nombre, no responde
                # Para evitar que diga su nombre al repetir
                rec = rec.replace(name, '')
                print(rec)  # Repite lo que decimos
    except:
        pass
    return rec


def run():
    rec = listen()  # aquí asignamos a la var 'rec' lo que sale de 'listen'
    if 'reproduce' in rec:
        music = rec.replace('reproduce', '')  # Para que no repita 'reproduce'
        talk(f'Reproduciendo {music}')
        pywhatkit.playonyt(music)  # Para que realmente busque en YT
    elif 'hora' in rec:
        hora = datetime.datetime.now().strftime('%H:%M')
        talk(f'Son las {hora}')
    elif 'busca' in rec:
        order = rec.replace('busca', '')
        info = wikipedia.summary(order, 1)
        talk(info)
    else:
        talk('Vuelve a intentarlo')


while True:
    run()

#   elif 'cuantos suscriptores tiene' in rec:
#        name_subs = rec.replaces('cuantos suscriptores tiene', '')
#        data = urllib.request.urlopen('https://www.googleapis.com/youtube/v3... + name_subs.strip() + '&key=' + key).read() # Se pega el link de la api youtube
#        subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
#        talk(f'{name_subs} tiene {int(subs)} suscriptores!')
