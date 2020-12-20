import os
import sys

"""
  These arguments can be run if you have a GPU accessible.
  Otherwise, they would be run in a cloud instance command line or notebook
"""
try:
    models_path, pipeline_config_path, model_dir, checkpoint_dir = sys.argv
except Exception as err:
    print('Command line arguments mismatch \n{}'.format(err))


# install pycotools
print('Installing pycotools...')
os.system('cmd /k pip install pycotools')
print('Installed.')
print('Changing working directory to {}'.format(os.path.join(models_path, 'research')))
os.system('cmd /k cd {}'.format(os.path.join(models_path, 'research')))
print('Setting protos')
os.system('cmd /k protoc object_detection/protos/*.proto --python_out=.')

print('Adding {} to PYTHONPATH and sys.path'.format(models_path))
os.environ['PYTHONPATH'] += ":{}".format(models_path)
sys.path.append("{}".format(models_path))

print('Building and installing object_detection library...')
os.system('cmd /k python setup.py build')
os.system('cmd /k python setup.py install')

os.system('cmd /k python ../official/pip_package/setup.py build')
os.system('cmd /k python ../official/pip_package/setup.py install')

os.system('cmd /k pip install lvis')
print('Installed')

# Execute full model training
print('Running training...')
train_command = "python object_detection/model_main_tf2.py --pipeline_config_path={} --model_dir={} --alsologtostderr".format(pipeline_config_path, model_dir)
os.system('cmd /k {}'.format(train_command))
print('Trained successfully')

# Evaluate
print('Evaluating')
eval_command = "python object_detection/model_main_tf2.py --pipeline_config_path={} --model_dir={} --checkpoint_dir={} --alsologtostderr".format(pipeline_config_path, model_dir, checkpoint_dir)
os.system('cmd /k {}'.format(eval_command))
print('Evaluated.')
