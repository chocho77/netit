db = []

def get_db():
    global db
    
    return db

def clear_db():
    global db
    
    return db.clear()



def add_vehicle_to_db(make: str,
                      model: str,
                      year: int,
                      color: str,
                      range: float):
    db.append((make, model, year, color, range))


def delete_vehicle(id: int):
    db.pop(id)

def view_vehicle(id: int):
    pass

def update_vehicle(id: int,
                   make: str,
                   model: str,
                   year: int,
                   color: str,
                   range: float
                   ):
    pass


 
    