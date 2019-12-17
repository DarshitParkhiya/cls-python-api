from pymongo import MongoClient

if __name__  == "__main__":
    con = MongoClient()
    db = con.test_database

    people = db.people

    people.insert({'name':'Mike','food':'chesee'})
    people.insert({'name': 'Darshit', 'food': 'Panipuri'})

    peeps= people.find()

    print("insert data")
    for person in peeps:
        print(person)