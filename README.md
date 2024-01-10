# Streetwatch: Utility and Wildfire Risks Detected From Street View Imagery

San Diego Gas & Electric leverages many different public and private data sources to make critical decisions that impact our communities. We would like to explore Google Street View as a publicly available source of data to help us identify risks that can be observed from the perspective of San Diego citizens. The project goals are to quantify the ability to observe damaged assets or fire from commonly traveled paths, determine whether there are clear compliance infractions that can be seen from the citizen's perspective, and identify other utility-related hazards that can be seen from this public data source.
 
## Data Sources
Data for this project is collected from [Google Street View Static API](https://developers.google.com/maps/documentation/streetview/overview). 

To run sunny.py, you need specifically structured JSON file. The JSON file will have 2 main item(OH and UG) and each should be the list of 5 different pole and within each pole, there should be 'loc' for lat and long 'heading' for heading direction of the image.

### Additional Files

Add various files located in the HDSI Capstone 2023-2024 Sharepoint Documents/Data folder to the data directory. This is needed in order to run `scripts/collect_images.py`:
* `joshua_structures.json`
* `kevin_structures.json`
* `jonathan_structures.json`
* `structure_coordinates.json`

## Setup

### Conda Environment
After cloning repo, navigating to root level and run:
```
conda env create -f environment.yml
```

### Credentials
Store credentials in `.env` file and load using [python-dotenv](https://pypi.org/project/python-dotenv/).

### Training Data
Create training data by running the following after setup is complete:
```
python scripts/collect_images.py
```

## Scripts

### Annotation Process
Located under scripts directory. This enables to shuffle individual coco json annotation files and split into two different group:training and validation set.

### Finetuing DETR
Located under notebooks directory. This shows the steps on how I used the collected images to train DETR to detect overhead distribution structures(poles).

# Project Structure

```
├── data/               <- Local data files only (do not commit)
│
├── notebooks/          <- Jupyter notebooks
│
├── scripts/            <- Python scripts to run in command line
│
├── .env                <- Environment variables for the project
│
├── .gitignore          <- Git ignore file
│
├── environment.yml     <- Conda environment file
│
└── README.md           <- The top-level README for repo
```
