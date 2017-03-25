import os
from keras.models import model_from_yaml




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
            file_path = os.path.join(module_dir, 'model.yaml')
            yaml_file = open(file_path, 'r')
            loaded_model_yaml = yaml_file.read()
            yaml_file.close()
            loaded_model = model_from_yaml(loaded_model_yaml)
            # load weights into new model
            file_path = os.path.join(module_dir, "model.h5")
            loaded_model.load_weights(file_path)
            KerasManager.loaded_model = loaded_model
            KerasManager.isModelLoaded = True
            print("Loaded model from disk")
            return KerasManager.loaded_model
