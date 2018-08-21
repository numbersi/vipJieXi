import re
import requests
from flask import request
from . import api2


@api2.route('/')
def index():
    return 'Api2'