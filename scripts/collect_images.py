import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.environ.get("API_KEY")
SECRET = os.environ.get("SECRET")


INPUT = 'data/Q1ProjectStructureList.xlsx'
OUTPATH = '../data/images/'


from collect_images.phi import create_images as images_phi
from collect_images.mateo import generate_images as images_mateo

if __name__== "__main__":
    #images_phi(INPUT, OUTPATH)
    images_mateo(OUTPATH)
