import os
import gspread
from flask import Flask

def init():
    creds_dict = eval(os.getenv("GSHEETS_CREDS"))
    gc = gspread.service_account_from_dict(creds_dict)
    return gc.open("Ping Counter").sheet1

def read_count(gs, count_cell):
    return int(gs.get(count_cell).first())

def increment_count(gs, count_cell):
    new_count = str(read_count(gs, count_cell) + 1)
    gs.update(count_cell, new_count)
    return new_count


# =============== Main ====================

Sheet = init()
count_cell = "B1"
assert Sheet


# ---------- Webserver --------------------

App = Flask(__name__)
@App.route('/')
def counter():
    return increment_count(Sheet, count_cell)
