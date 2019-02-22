import os
import logging
import sys

BASE_DIR= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASE = {
    'engine':'file_storage',
    'name':'accounts',
    'path':'%s/db' % BASE_DIR

}

LOG_LEVEL = logging.INFO
LOG_TYPE = {
    'transaction':'transactions.log',
    'access':'access.log',

}

TRANSACTION_TYPE = {
    'repay':{'action':'plus','interest':0},
    'withdraw':{'action':'minus','interest':0.05},
    'transfer':{'action':'plus','interest':0.05},
    'consume':{'action':'plus','interest':0},
}