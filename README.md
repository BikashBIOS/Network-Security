## REQUIREMENTS
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
7. 