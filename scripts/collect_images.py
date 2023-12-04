import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.environ.get("API_KEY")
SECRET = os.environ.get("SECRET")


INPUT = 'data/Q1ProjectStructureList.xlsx'
OUTPATH = 'data/images/'


from collect_images.phi import create_images as images_phi
from collect_images.mateo import generate_images as images_mateo
from collect_images.tram import create_images as images_tram

if __name__== "__main__":
    #images_phi(INPUT, OUTPATH)
    images_mateo(OUTPATH)
    #images_tram(OUTPATH)