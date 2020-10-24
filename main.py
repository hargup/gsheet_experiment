import gspread
from flask import Flask

def init():
    gc = gspread.service_account()
    return gc.open("Ping Counter").sheet1


def read_count(gs, count_cell):
    return int(gs.get(count_cell).first())

def increment_count(gs, count_cell):
    new_count = str(read_count(gs, count_cell) + 1)
    gs.update(count_cell, new_count)
    return new_count

App = Flask(__name__)
Sheet = init()
count_cell = "B1"
assert Sheet

@App.route('/')
def counter():
    return increment_count(Sheet, count_cell)
