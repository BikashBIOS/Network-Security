# Network Security Project for Phising Data

## Requirements & GitHub
1. Create new env -- python -m venv venv
2. Create files - requirements.txt, .gitignore, setup.py, .github/workflows/main.yaml, Dockerfile, .env
3. Create folders as per the project requirement :
- Network_Data - for your data (added phisingdata.csv)
- networksecurity - for your main codes(src)
- notebooks - for your jupyter notebooks
4. Specify your libraries in the requirements.txt and then run pip install -r requirements.txt
5. Write venv and .env files in the .gitignore for the git to ignore all these files while pushing the code to our github repo.
6. Create a new github repo - Network Security and then push the code : 
- git init
- git add .
- git commit -m "First commit"
- git branch -M main
- git remote add origin https://github.com/BikashBIOS/Network-Security.git
- git push -u origin main
7. Remember to add __init__.py in all the folders. Push again.


## Setup.py 
1. Specify the code in setup.py to get the libraries from requirements.txt
2. Specify the version, package info and retrieve from get_requirements()
3. After executing pip install -r requirments.txt, you can see your package folder getting created with all the info and requirements. 


## Logging and Exception
1. Create the logging and Exception file