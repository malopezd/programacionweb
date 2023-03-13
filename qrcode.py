import qrcode
from PIL import Image

url= input("introduzca el url o texto a conevretir en codigo QR :")
imagen = qrcode.make(url)

nombre_imagen=input("introdusca el nombre a la imagen generada:")+'png'
archivo_imagen=open(nombre_imagen,'wb')
imagen.save(archivo_imagen)
archivo_imagen.close()

ruta_imagen='./'+nombre_imagen
Image.open(ruta_imagen).show()