__Authour__ = 'Harry Burge'
__DateCreated__ = '01/02/2020'
__LastUpdated__ = '04/02/2020'


# Imports
from PIL import Image, ImageOps
import tensorflow.keras
import numpy as np


class AIModel:
    '''
    This is a class that holds an interface to using tensorflow for modeling images.

    attributes:-
        size : (int, int) : size of images to model off
        labels : [str, ...] : labels read in from model
        _model : tensorflow model
        _data : nparray
    '''
    
    def __init__(self, model_path, model_name="keras_model.h5", model_labels="labels.txt", size=(224,224)): 
        '''
        Initalises the model and loads labels
        
        params:-
            model_path : str : path to the model wanting to be initialised
            model_name : str : name of the h5 model
            model_labels : str : name of the txt filewhich holds labels
            size : (int,int) : size of images that models takes as input
        returns:-
            None
        '''
        self.size = size

        # Load AI model
        self._model = tensorflow.keras.models.load_model(model_path+model_name, compile=False)
        self._data = np.ndarray(shape=(1, size[0], size[1], 3), dtype=np.float32)

        # Load labels
        file = open(model_path+model_labels, 'r')
        lines = file.read().split('\n')

        # Removes blank line at end if exists
        if lines[-1] == '': del lines[-1] 

        for index, i in enumerate(lines):
            lines[index] = i.split(' ')[1]

        self.labels = lines


    def use_model_on_image(self, image):
        '''
        Takes an PIL.Image and runs it against the AI to make prediction

        params:-
            image : PIL.Image : Image to be ran against
        returns:-
            [float, ...] : Output node after input
        '''

        # Disable scientific notation for clarity
        np.set_printoptions(suppress=True)

        # Load image and fit to size
        image = ImageOps.fit(image, self.size, Image.ANTIALIAS)

        # Put data into input nodes
        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        self._data[0] = normalized_image_array
        
        # Run model
        prediction = self._model.predict(self._data)

        return prediction

    
    def get_label(self, index):
        return self.labels[index]
