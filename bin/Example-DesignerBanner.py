from AI_models import AIUtil
from tensorflow.python.client import device_lib
from PIL import Image
import numpy

#pred = AIUtil.use_model_on_image('AI_models/BannerLabelingAI/keras_model.h5', 'image002.JPG')

im = Image.open('Designer.JPG')

width, height = im.size
segwidth, segheight = width//20+25, height//20

aimodel = AIUtil.AIModel('AI_models/HighContrast_Designer_Banner/')

print(device_lib.list_local_devices())

def max_index(list1):
    return numpy.argmax(list1)

for i in range(1, 2):
    for j in range(0, 5):
        left = j*segwidth+5
        top = i*segheight
        segment_im = im.crop((left, top, left+segwidth, top+segheight))
        pred = aimodel.use_model_on_image(segment_im)
        if aimodel.get_label(max_index(pred)) != 'Nothing':
            segment_im.save('temp' + str(i) + '_' + str(j) + aimodel.get_label(max_index(pred)) + '.JPG')


