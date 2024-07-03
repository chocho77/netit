import csv

db = []

def get_db():
    global db
    
    return db

def clear_db():
    global db
    
    return db.clear()



def add_vehicle(make: str,
                      model: str,
                      year: int,
                      color: str,
                      range: float):
    db.append((make, model, year, color, range))


def delete_vehicle(id: int):
    db.pop(id)

def view_vehicle(id: int):
    return db[id]

def update_vehicle(id: int,
                   make: str,
                   model: str,
                   year: int,
                   color: str,
                   range: float
                   ):
    db[id] = (make, model, year, color, range)

def export_data(filepath: str):
    with open(filepath, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile)
        for row in get_db():
            spamwriter.writerow(row)





 
    