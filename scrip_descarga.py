import os
import subprocess
import pytube

def descarga(enlace):
    link = pytube.YouTube(f"{enlace}")

    #formatos = link.streams.all()
    #Opcion para ver los distintos formatos de descarga
    #for i in range(len(formatos)):
    #    print(i,'. ',formatos[i])

    opc_formato =  link.streams.get_by_itag(140) #Es el itag: mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2" progressive="False" type="audio">
    ruta = os.getcwd()
    opc_formato.download()
    #formatos[opc_formato].download(ruta)
    #nombre = formatos[opc_formato].default_filename
    nombre = opc_formato.default_filename
    nuevo_nombre = nombre[0:-4]
    print("========================================")
    print(f"Conviertiendo {nuevo_nombre}")
    print("========================================")
    subprocess.call([
        r'C:\Users\nikky\OneDrive\Escritorio\Musica\ffmpeg\bin\ffmpeg.exe',
        '-i', os.path.join(ruta, nombre),
        os.path.join(ruta, f"{nuevo_nombre}.mp3")
    ])
    os.remove(nombre)

def lectura():
    archivo = open("Enlaces.txt", "r")
    links = archivo.readlines()
    archivo.close()
    for i in range(len(links)):
        descarga(links[i])

lectura()