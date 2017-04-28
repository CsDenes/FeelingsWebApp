import os
from keras.models import model_from_yaml
from keras.models import model_from_json
from keras.models import load_model




class KerasManager:
    isModelLoaded = False
    loaded_model = []

    @staticmethod
    def loadModel():
        if KerasManager.isModelLoaded:
            return KerasManager.loaded_model
        else:
            module_dir = os.path.dirname(__file__)  # get current directory
            # load YAML and create model
            file_path = os.path.join(module_dir, 'model.json')
            json_file = open(file_path, 'r')
            loaded_model_json = json_file.read()
            json_file.close()
            loaded_model = model_from_json(loaded_model_json)
            # load weights into new model
            file_path = os.path.join(module_dir, "model.h5")
            loaded_model.load_weights(file_path)
            KerasManager.loaded_model = loaded_model
            KerasManager.isModelLoaded = True
            print("Loaded model from disk")
            return KerasManager.loaded_model
