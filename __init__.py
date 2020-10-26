import os 
import sys 
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import akivymd.factory_registers
from kivy.logger import Logger

__version__ = '1.2.1'
__description__ = 'A set of fancy widgets for KivyMD'
__author__ = "Sina Namadian"
__email__ = "quitegreensky@gmail.com"
Logger.info(f"akivymd: v{__version__}")
