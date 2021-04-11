# gsheet_experiment
Ping a route to increament counter in a google sheet.

Route: https://gsheet-experiments.herokuapp.com/
Google Sheet: https://docs.google.com/spreadsheets/d/1xrWKBZOEf4hWXlrA4RcPO7kOS-GK2K9qu8eVgYP61Y8/edit?usp=sharing


Fire up the given route and see the counter increasing in the google spreadsheet.

# Installation

- Install the last commit of gspread https://github.com/burnash/gspread
```
pip install -e git+https://github.com/burnash/gspread#master#egg=gspread
```

Install flask and other dependencies
```
pip install -r requirements.txt
```

We require the lastest commits to read credentials from Dictionary. As of now (2020-10-24), this commit isn't part of the last release. See https://github.com/burnash/gspread/pull/785

- To get Google service account creds, follow https://gspread.readthedocs.io/en/latest/oauth2.html#for-bots-using-service-account

- As specified in the document above, share your spreadsheet with the bot account

- Save the creds ot `service_account.json` file

- Install flask https://flask.palletsprojects.com/en/1.1.x/installation/#installation


# Local Developement

- Export credentials as environment variable
```
export GSHEETS_CREDS=$(cat service_account.json)
```
- Run the server
```
python main.py
```


# Deployment on Heroku

- Create a new Heroku app
- Install Heroku commandline https://devcenter.heroku.com/categories/command-line
- Set the account creds as Heroku configs
```
heroku config:set GSHEETS_CREDS="$(cat service_account.json)"
```
- Push the lastest code to heroku
```
git push heroku main
```
