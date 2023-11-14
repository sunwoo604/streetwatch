# Streetwatch: Utility and Wildfire Risks Detected From Street View Imagery

San Diego Gas & Electric leverages many different public and private data sources to make critical decisions that impact our communities. We would like to explore Google Street View as a publicly available source of data to help us identify risks that can be observed from the perspective of San Diego citizens. The project goals are to quantify the ability to observe damaged assets or fire from commonly traveled paths, determine whether there are clear compliance infractions that can be seen from the citizen's perspective, and identify other utility-related hazards that can be seen from this public data source.
 
## Data Sources

- https://developers.google.com/maps/documentation/streetview/overview

## Setup

### Conda Environment

After cloning repo, navigating to root level and run:

```
conda env create -f environment.yml
```

### Credentials

Store credentials in `.env` file and load using [python-dotenv](https://pypi.org/project/python-dotenv/).

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