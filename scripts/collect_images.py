import os
import requests
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.environ.get("API_KEY")
SECRET = os.environ.get("SECRET")


INPUT = 'data/Q1ProjectStructureList.xlsx'
OUTPATH = 'data/images/'


from collect_images.phi import create_images as images_phi
from collect_images.noel import main as images_noel


if __name__== "__main__":
    images_phi(INPUT, OUTPATH)
    images_noel(OUTPATH)