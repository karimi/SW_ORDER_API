import os, sys

PROJECT_DIR = '/var/www/SW_order_API/SW_ORDER_API'

activate_this = os.path.join(PROJECT_DIR, 'bin', 'activate_this.py')
execfile(activate_this, dict(__file__=activate_this))
sys.path.append(PROJECT_DIR)

from __init__ import app as application
