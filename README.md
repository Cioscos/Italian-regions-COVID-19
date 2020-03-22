# Italian-regions-COVID-19
[![GitHub commit](https://img.shields.io/github/last-commit/pcm-dpc/COVID-19)](https://github.com/Cioscos/Italian-regions-COVID-19)

This software allows you to view data regarding the number of total infected, currently infected, deceased and recovered for each region, by COVID-19.

Data are automatically downloaded form Repository of "Protezione civile"

When you open the software you'll see this windows:

<img src="https://i.imgur.com/vcIO3kd.png" width=600 height=400/>

You can double click on a region to watch visual data about the selected region:

<img src="https://i.imgur.com/6MAaZwJ.png" />

## How to use
```
git clone https://github.com/Cioscos/Italian-regions-COVID-19.git
```
Then create a virtualenv if u prefer in the root of the project
```
python -m venv \path\to\new\virtual\environment
```
And then activate the venv
```
from\root\of\prject\> cd venv\scripts
>activate.bat
```
Now intall all the requirements typing:
```
pip install -r requirements.txt
```

### If u have some problem with PyQt4 and you are on Windows try this:
[Download this file from Google drive;](https://drive.google.com/file/d/1ACTmGWlawjbYoE5Q5ak-B2gDU4CrA_T6/view?usp=sharing)
It is a wheel that will install PyQt4 files

Then use type this on CMD:
```
path\of\whl_file> pip install PyQt4-4.11.4-cp37-cp37m-win_amd64.whl
```
Finally run the script:
```
Italian-regions-COVID-19\src> python main.py
```
