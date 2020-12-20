import os
import sys

"""
  These arguments can be run if you have a GPU accessible.
  Otherwise, they would be run in a cloud instance command line or notebook
"""

os.system('cmd /k pip install pycotools')
os.system('cmd /k cd /Users/jacksimonson/models/research')
os.system('cmd' /k protoc object_detection/protos/*.proto --python_out=.)

os.environ['PYTHONPATH'] += ":/Users/jacksimonson/models/"
sys.path.append("/Users/jacksimonson/models/")

os.system('cmd /k python setup.py build')
os.system('cmd /k python setup.py install')

os.system('cmd /k python ../official/pip_package/setup.py build')
os.system('cmd /k python ../official/pip_package/setup.py install')

os.system('cmd /k pip install lvis')

# Execute full model training
os.system('cmd /k python object_detection/model_main_tf2.py --pipeline_config_path="/Users/jacksimonson/model_new_three/pipeline.config" --model_dir="/Users/jacksimonson/model_new_three" --alsologtostderr)

# Evaluate
os.system('cmd /k python object_detection/model_main_tf2.py --pipeline_config_path="/Users/jacksimonson/model_new_three/pipeline.config" --model_dir="/Users/jacksimonson/model_new_three" --config_dir="Users/jacksimonson/models/research/object_detection/training" --alsologtostderr)
