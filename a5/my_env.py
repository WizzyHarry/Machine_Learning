#!/usr/bin/env python3
import subprocess
import os
import shutil
import sys
import jupyterlab 
import pandas  
import numpy
import matplotlib 
import sklearn 
import django 
import tensorflow 
import scipy 
import keras 

def list_packages():
    print('Python version: \n{0}'.format(sys.version), "\n")
    print('jupyterlab: {0}'.format(jupyterlab.__version__))
    print('pandas: {0}'.format(pandas.__version__))
    print('numpy: {0}'.format(numpy.__version__))
    print('matplotlib: {}'.format(matplotlib.__version__))
    print('sklearn: {0}'.format(sklearn.__version__))
    print('django: {0}'.format(sklearn.__version__))
    print('tensorflow: {0}'.format(tensorflow.__version__))

print(list_packages())