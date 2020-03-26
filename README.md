# Italian-regions-COVID-19
[![GitHub commit](https://img.shields.io/github/last-commit/Cioscos/Italian-regions-COVID-19)](https://github.com/Cioscos/Italian-regions-COVID-19.git)
[![GitHub license](https://img.shields.io/badge/License-Creative%20Commons%20Attribution%204.0%20International-blue)](https://github.com/Cioscos/Italian-regions-COVID-19/blob/master/LICENSE)

This software allows you to view data regarding the number of total infected, currently infected, deceased and recovered for each region, by COVID-19.

Data are automatically downloaded form Repository of "Protezione civile"

When you open the software you'll see this windows:

<img src="https://i.imgur.com/fTXTjL1.png" width=600 height=400/>

You can double click on a region to watch visual data about the selected region:

<img src="https://i.imgur.com/VUlxMox.png" />

With the plot window, you can watch also last day info:

<img src="https://i.imgur.com/BRh02cp.png" />

## How to use
```
git clone https://github.com/Cioscos/Italian-regions-COVID-19.git
```

Or download the project directly from Github.

If u don't have virtualenv installed, install it typing:
```
pip install virtualenv
```

Then create a virtualenv, if you prefer, in the root of the project.
```
python -m venv \path\to\new\virtual\environment
```
And then activate the venv
```
from\root\of\prject\> cd venv\scripts
>activate.bat
```
Now install all the requirements typing:
```
pip install -r requirements.txt
```

Next, execute the script in the folder of the .py file:
```
python main.py
```

### If u have some problem with PyQt4 and you are on Windows try this:
[Download this file from Google drive;](https://drive.google.com/file/d/1ACTmGWlawjbYoE5Q5ak-B2gDU4CrA_T6/view?usp=sharing)
It is a wheel that will install PyQt4 files

Then type this on CMD:
```
path\of\whl_file> pip install PyQt4-4.11.4-cp37-cp37m-win_amd64.whl
```
Finally run the script:
```
Italian-regions-COVID-19\src> python main.py
```
## How to create an executable if you want to run it on a PC without Python
Open CMD and type:
```
pip install pyinstaller
```
Then go to the location where your Python script is stored
```DOS
cd path\to\python\script
```
Next, use the following template to create the executable:
```
pyinstaller --onefile main.py
```
Pyinstaller will create a new folder called dist in which there is the executable just created.
Once you click on the file, you should be able to launch your program (if you get an error message, 
you may need to install 
[Visual C++ Redistributable](https://support.microsoft.com/en-ca/help/2977003/the-latest-supported-visual-c-downloads)).
