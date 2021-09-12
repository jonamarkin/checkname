import sqlite3


def checkname():
    name = input("What is your name?\n")

    # Connect to the database
    db = sqlite3.connect('example.db')
    cursor = db.cursor()

    # Query all user Ids where the firstname matches the user's input
    cursor.execute("SELECT id from users WHERE firstname = ?", (name,))

    # Fetch the first result of the query above
    result = cursor.fetchone()

    # If the result is not empty then we have found a match
    if result and len(result) > 0:
        print("Hello", name, "you user id is ", result[0])

    # otherwise we have not found this user by name
    else:
        print("We could not find your user id in the system", name)

        answer = input("Do you want to add your name? (yes/no)\n")

        if answer.lower() == "yes":
            addname(name)
        else:
            print("Thanks for your time")

    db.close()


def addname(name):

    # Connect to the database
    db = sqlite3.connect('example.db')
    cursor = db.cursor()

    # Insert the users's name into the database
    cursor.execute("INSERT INTO users (firstname) values(?)", (name,))

    db.commit()

    print("Your name has been added to the database", name)

    db.close()


checkname()
