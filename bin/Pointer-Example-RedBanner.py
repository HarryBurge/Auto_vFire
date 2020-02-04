from AI_models import AIUtil
from tensorflow.python.client import device_lib
from PIL import Image, ImageDraw
import numpy

im = Image.open('image002.JPG')
outputim = im.copy()
draw = ImageDraw.Draw(outputim)

width, height = im.size
segwidth, segheight = width//20-5, height//20

aimodel = AIUtil.AIModel('AI_models/Example-BannerLabelingAI/')

def max_index(list1):
    return numpy.argmax(list1)

for i in range(0, 2):
    for j in range(0, 21):
        left = j*segwidth+18
        top = i*segheight
        segment_im = im.crop((left, top, left+segwidth, top+segheight))
        pred = aimodel.use_model_on_image(segment_im)
        if aimodel.get_label(max_index(pred)) != 'Nothing':
            #draw.line([left, top, left+segwidth, top+segheight], fill='red', width = 10)
            draw.rectangle([left, top, left+segwidth, top+segheight], outline='red', width=5)

del draw
outputim.show()