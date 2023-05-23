import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image 


img = np.ones((630,1350,3), dtype=np.uint8) * 80


img[210:310 , 210:310] = (30 , 80  , 240)
img[210:310 , 320:420] = (0  , 180 , 120)
img[320:420 , 210:310] = (240, 160 , 0  )
img[320:420 , 320:420] = (0  , 180 , 255)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = Image.fromarray(img)
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("inputs\Segoe UI.ttf", 160)
draw.text((470, 200), "Microsoft", font=font)
img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)



cv2.imwrite('outputs/microsoft_logo.jpg', img)