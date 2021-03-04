Written and tested in ubuntu xenial 16.04 with python 3.5.2

Run chrome_driver.sh to install chrome_driver and the chromium_browser which includes all of the dependecies chrome_driver might need
Run requirements.txt to install python3 pip packages

For the information script, the form names to input can be given to the function at the bottom of the file in the main section; add the names to the form list that you require. The output will be returned as a list object, printed to stdout, and also dumped to a json file with the specified filename.
I left my debugging print statements in the information script to give you an idea of how I worked through the problem. 

The script can be run from the current directory as ./information.py

For the download_forms script, the inputs can be similarly applied in the main section at the bottom of the script file.

The script can be run from the current directory as ./download_forms.py

I left only the replacement lines commented out in the download_forms script so as to meet the exact requirements of the challenge, but I think the spaces should be replaced with underscores in the directory name and filename, and should maybe be updated in the project description.

