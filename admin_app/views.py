from django.shortcuts import render,HttpResponse
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
from selenium import *

# from emoji import random_emoji
import os
import random
from pathlib import Path
from random import randint
import array
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import random
from .driver import undetectable_driver

# Create your views here.
def insta_login(request):
    return render(request,'index.html')
    