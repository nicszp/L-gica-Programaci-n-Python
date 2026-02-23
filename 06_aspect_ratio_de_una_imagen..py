### Aspect ratio de una imagen ###

"""

Crea un programa que se encargue de calcular el aspect ratio de una
imagen a partir de una url.

- Url de ejemplo:
 https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png

- Por ratio hacemos referencia por ejemplo a los "16:9" de una
imagen de 1920*1080px.

"""

import requests
from PIL import Image
from io import BytesIO
import math


r = requests.get("https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png")

Img = Image.open(BytesIO(r.content))
ancho, alto = Img.size
#print(ancho, alto)

mcd = math.gcd(ancho, alto)
#print(mcd)
ratio_ancho = ancho // mcd
ratio_alto = alto // mcd

print(f"El ratio es {ratio_ancho}:{ratio_alto}")