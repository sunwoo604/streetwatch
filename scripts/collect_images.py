
#%%
import os
import requests
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.environ.get("API_KEY")
SECRET = os.environ.get("SECRET")


INPUT = 'data/Q1ProjectStructureList.xlsx'
OUTPATH = 'data/images/'
JOSHUA_INPUT = 'data/joshua_structures.json'


from collect_images.phi import create_images as images_phi
from collect_images.alex import get_dataset as images_alex
from collect_images.brandon import collect_imgs as images_brandon
from collect_images.kevin import create_images as images_kevin
from collect_images.sunny import collect_struct_json as images_sunny
from collect_images.jonathan import get_images as images_jonathan
from collect_images.derek import derek_create_images
from collect_images.kelly import collect_imgs as images_kelly
from collect_images.noel import main as images_noel
from collect_images.joshua import create_images as images_joshua


if __name__== "__main__":
    images_phi(INPUT, OUTPATH)
    images_alex()
    images_brandon(OUTPATH)
    images_kevin('data/kevin_structures.json', OUTPATH)
    images_sunny('data/structure_coordinates.json', OUTPATH)
    images_jonathan('data/jonathan_structures.json', OUTPATH)
    derek_create_images()
    images_kelly(OUTPATH)
    images_noel(OUTPATH)
    images_joshua(JOSHUA_INPUT, OUTPATH)
