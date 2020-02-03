from PIL import Image
import random

Imgs_to_crop = [
    'None_WhiteLine'
]

for i in Imgs_to_crop:

    im = Image.open(i+'.JPG')
    truewidth, trueheight = im.size

    for j in range(0, 50):
        ranleft = random.randint(0, truewidth//4)
        rantop = random.randint(0, trueheight//4)

        ranwidth = random.randint(3*truewidth//4, truewidth)
        ranheight = random.randint(3*trueheight//4, trueheight)

        left = ranleft
        top = rantop

        height = ranheight - rantop
        width = ranwidth - ranleft

        print('Training_Data_Created/'+i+'_'+str(j)+'.JPG')
        im1 = im.crop((left, top, left+width, top+height))
        im1 = im1.save('Training_Data_Created/'+i+'_'+str(j)+'.JPG')
