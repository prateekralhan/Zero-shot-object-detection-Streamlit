# Zero Shot Object Detection (GroundingDINO) Streamlit [![Project Status: Active](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active) [![](https://img.shields.io/badge/Prateek-Ralhan-brightgreen.svg?colorB=ff0000)](https://prateekralhan.github.io/)
A minimalistic webapp to perform zero shot object detection based on textual prompts using GroundingDINO 


## Installation:
* Simply run the command ```pip install -r requirements.txt``` to install the dependencies.
* Make sure you have CUDA installed and setup. For more details in setting GroundingDINO, please refer [this.](https://github.com/IDEA-Research/GroundingDINO)

## Usage:
1. Clone this repository and install the dependencies as mentioned above.
2. Create a ```weights``` directory and save the model checkpoints which can be downloaded from [here.](https://github.com/IDEA-Research/GroundingDINO/releases/download/v0.1.0-alpha/groundingdino_swint_ogc.pth)
3. Simply run the command: 
```
streamlit run app.py
```
4. Navigate to http://localhost:8501 in your web-browser.
5. By default, streamlit allows us to upload files of **max. 200MB**. If you want to have more size for uploading images, execute the command :
```
streamlit run app.py --server.maxUploadSize=1028
```

### Running the Dockerized App
1. Ensure you have Docker Installed and Setup in your OS (Windows/Mac/Linux). For detailed Instructions, please refer [this.](https://docs.docker.com/engine/install/)
2. Navigate to the folder where you have cloned this repository ( where the ***Dockerfile*** is present ).
3. Build the Docker Image (don't forget the dot!! :smile: ): 
```
docker build -f Dockerfile -t app:latest .
```
4. Run the docker:
```
docker run -p 8501:8501 app:latest
```

This will launch the dockerized app. Navigate to ***http://localhost:8501/*** in your browser to have a look at your application. You can check the status of your all available running dockers by:
```
docker 
```


### Citation
```
@article{liu2023grounding,
  title={Grounding dino: Marrying dino with grounded pre-training for open-set object detection},
  author={Liu, Shilong and Zeng, Zhaoyang and Ren, Tianhe and Li, Feng and Zhang, Hao and Yang, Jie and Li, Chunyuan and Yang, Jianwei and Su, Hang and Zhu, Jun and others},
  journal={arXiv preprint arXiv:2303.05499},
  year={2023}
}
```



