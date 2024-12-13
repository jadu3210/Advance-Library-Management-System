import json

def save_all_data(data):
    with open('library_data.json', "w") as fp:
        json.dump(data, fp, indent=4)

def load_all_data():
    try:
        with open('library_data.json', "r") as fp:
            return json.load(fp)
    except FileNotFoundError:
        return {"all_books": [], "lend_info": []}