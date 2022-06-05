# MotionDetector
A script that detects and counts the number of repetitions of jumping jacks in a video clip done by a person

## Run instructions

_Note: This script requires that your system has ffmpeg installed, and it's install directory added to_ `path`. _Download ffmpeg from https://www.gyan.dev/ffmpeg/builds/_

Fork this repository, and clone it to your local machine

Open a new terminal window, and navigate to the root of the repository

Start a new Python virtual environment by typing `python -m venv <your-env-name>`

While remaining in the root, type `your-env-name\Scripts\activate` to activate the virtual environment

Install the dependencies the script requires by using `pip install -r requirements.txt`

Add a video to the directory named `vid` for which you would like to count jumping jacks

Run the script by executing `python jumpingjackreader.py <your-vid-filename>`
