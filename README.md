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
1. Create the logging and Exception file as per the generic code of logging and exception.
2. __main__ file in exception can be used to test if exception is working fine or not. 


## ETL Pipeline (Extract, Transform, Load)
1. We have our Source and Destination between that 'Transformation' happens.
2. Source here is our local database from which we EXTRACT the csv dataset, we apply TRANSFORMATION to this dataset to change it to json, then we LOAD the data in the destination i.e our MongoDB.


## MongoDB Connection
1. Create a new Free account in MongoDB Atlas. 
2. Create a default Cluster0 cluster.
3. Let the default username and password remain. 
4. Click Next -> Choose a connection Method -> Click on Drivers
5. Select Driver as Python and version.
6. Add the pymongo libraray version in requirements.txt file.
7. Then click on Done and the Cluster0 will be created.
8. Then click on Connect on the cluster. Check the full code sample. Copy that code. 
9. Create a new file - push_data.py in root folder and paste that code. 
10. In the code, we have to change the dbpassword (in uri object) to our password. (If you have forgotten, go to Quickstart and then you can update the password for your username).
11. The uri object shouldn't be hardcoded, so to ensure that, we add the same uri string in our .env file. 
12. Now run python push_data.py and if all is good, it will show You successfully connected to MongoDB.
13. Cut the push_data.py code into a new file - test_mongodb.py as we will use it later. 
14. In push_data.py, load that env variable. Get the MONGO_DB_URL from env file and print. 



## ETL Pipeline Setup with Python
1. Import certifi in push_data.py
2. Certifi - Python package that provides a set of root certificates - commonly used to make a secure HTTP connection.
3. Now we will write the function for converting our csv data to json. 
4. Json data is basically One row's data in key:value pairs while key being column and value being row value. And one row's data would be in a dict with key values pairs.
5. cv_to_json_converter() - converts the csv data into json and stores the json records in records.
6. insert_data_mongodb() - create the database, collection and records. Connect to your mongodb client and then create the database and collection. Then insert and return the records.
7. __main__() - To run this, pass in the FILE_PATH for your dataset (i.e phisingData.csv), give some random name to your dataset and collection, Call the NetworkDataExtract() to convert the data to json, and then insert_data_mongodb() - to insert your data into MongoDB cluster.
8. After you run python push_data.py - the data gets inserted into MongoDB cluster database. Open that Cluster0 in browser, and open the database, and you can find your json data inserted into it. 





