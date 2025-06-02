import os
import pickle
from box.exceptions import BoxValueError

def save_obj(file_path, obj):
    try:
        path_dir = os.path.dirname(file_path)
        os.makedirs(path_dir,exist_ok=True)
        
        with open(file_path,'wb') as file:
            pickle.dump(obj, file)
    
    except BoxValueError:
        raise ValueError(f'save obj error: {e}')
    except Exception as e:
        raise e