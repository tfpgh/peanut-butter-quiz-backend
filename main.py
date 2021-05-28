from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import pymongo

app = FastAPI()
client = pymongo.MongoClient("10.0.0.67", 27017)
db = client.responses
col = db.responses


@app.get("/", response_class=HTMLResponse)
def root():
    with open("index.html") as f:
        return f.read()


@app.get("/results", response_class=HTMLResponse)
def results(
    peanut_like: str,
    peanut_butter_like: str,
    crunchy_smooth: str = None,
    brand: str = None,
    way_to_eat: str = None,
    sweetened: str = None,
    salt: str = None,
    general_thoughts: str = None,
):
    data_dict = {
        "peanut-like": peanut_like,
        "peanut_butter_like": peanut_butter_like,
        "crunchy_smooth": crunchy_smooth,
        "brand": brand,
        "way_to_eat": way_to_eat,
        "sweetened": sweetened,
        "salt": salt,
        "general_thoughts": general_thoughts,
    }
    col.insert_one(data_dict)
    return '<meta http-equiv="refresh" content="0; URL=/stats" />'


@app.get("/stats", response_class=HTMLResponse)
def stats():
    with open("results.html") as f:
        file_contents = f.read()
        file_contents = file_contents.replace("PEANUT_REPLACE", str(peanut_like_func()))
        file_contents = file_contents.replace(
            "PEANUT_BUTTER_REPLACE", str(peanut_butter_like_func())
        )
        file_contents = file_contents.replace(
            "CRUNCHY_SMOOTH_REPLACE", str(crunchy_smooth_func())
        )
        file_contents = file_contents.replace("BRAND_REPLACE", str(brand_func()))
        file_contents = file_contents.replace(
            "WAY_TO_EAT_REPLACE", str(way_to_eat_func())
        )
        file_contents = file_contents.replace(
            "SWEETENED_REPLACE", str(sweetened_func())
        )
        file_contents = file_contents.replace("SALT_REPLACE", str(salt_func()))
    return file_contents


def peanut_like_func():
    cursor = col.find({})
    yes = 0
    no = 0
    sorta = 0
    for doc in cursor:
        peanut_like = doc["peanut-like"]
        if peanut_like == "Yes":
            yes += 1
        elif peanut_like == "No":
            no += 1
        elif peanut_like == "Sorta":
            sorta += 1
    return [yes, no, sorta]


def peanut_like_func():
    cursor = col.find({})
    yes = 0
    no = 0
    sorta = 0
    for doc in cursor:
        peanut_like = doc["peanut-like"]
        if peanut_like == "Yes":
            yes += 1
        elif peanut_like == "No":
            no += 1
        elif peanut_like == "Sorta":
            sorta += 1
    return [yes, no, sorta]


def peanut_butter_like_func():
    cursor = col.find({})
    yes = 0
    no = 0
    sorta = 0
    for doc in cursor:
        peanut_like = doc["peanut_butter_like"]
        if peanut_like == "Yes":
            yes += 1
        elif peanut_like == "No":
            no += 1
        elif peanut_like == "Sorta":
            sorta += 1
    return [yes, no, sorta]


def crunchy_smooth_func():
    cursor = col.find({})
    crunchy = 0
    smooth = 0
    dont_care = 0
    for doc in cursor:
        peanut_like = doc["crunchy_smooth"]
        if peanut_like == "Crunchy":
            crunchy += 1
        elif peanut_like == "Smooth":
            smooth += 1
        elif peanut_like == "Don't Care":
            dont_care += 1
    return [crunchy, smooth, dont_care]


def brand_func():
    cursor = col.find({})
    jif = 0
    skippy = 0
    justin = 0
    store_brand = 0
    dont_care = 0
    other = 0
    for doc in cursor:
        peanut_like = doc["brand"]
        if peanut_like == "Jif":
            jif += 1
        elif peanut_like == "Skippy":
            skippy += 1
        elif peanut_like == "Justin's":
            justin += 1
        elif peanut_like == "Store Brand":
            store_brand += 1
        elif peanut_like == "Don't Care":
            dont_care += 1
        elif peanut_like == "Other":
            other += 1
    return [jif, skippy, justin, store_brand, dont_care, other]


def way_to_eat_func():
    cursor = col.find({})
    spoon = 0
    bread = 0
    pbj = 0
    pretzels = 0
    apple = 0
    other = 0
    for doc in cursor:
        peanut_like = doc["way_to_eat"]
        if peanut_like == "Spoon":
            spoon += 1
        elif peanut_like == "Bread":
            bread += 1
        elif peanut_like == "PB&J":
            pbj += 1
        elif peanut_like == "Pretzels":
            pretzels += 1
        elif peanut_like == "Apple":
            apple += 1
        elif peanut_like == "Other":
            other += 1
    return [spoon, bread, pbj, pretzels, apple, other]


def sweetened_func():
    cursor = col.find({})
    yes = 0
    no = 0
    sorta = 0
    dont_care = 0
    for doc in cursor:
        peanut_like = doc["sweetened"]
        if peanut_like == "Yes":
            yes += 1
        elif peanut_like == "No":
            no += 1
        elif peanut_like == "Sorta":
            sorta += 1
        elif peanut_like == "Don't Care":
            dont_care += 1
    return [yes, no, sorta, dont_care]


def salt_func():
    cursor = col.find({})
    yes = 0
    no = 0
    sorta = 0
    for doc in cursor:
        peanut_like = doc["salt"]
        if peanut_like == "Yes":
            yes += 1
        elif peanut_like == "No":
            no += 1
        elif peanut_like == "Sorta":
            sorta += 1
    return [yes, no, sorta]
