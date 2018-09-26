# most-starred-python-projects

This project uses the github api to find the most starred public python projects.
The web app is served with Flask
Requests is used to fetch the data from GitHub API and stored in SQLite by using SQLAlchemy 


To run this, clone the repository
```
git clone https://github.com/xanderpac24/most-starred-python-projects.git
```
Create a virtualenv and activate it
```
virtualenv -p python3.6 .venv
source .venv/bin/activate
```
Install dependencies using pip
```
pip install -r requirements.txt
```
Run the program
```
python app.py
```
