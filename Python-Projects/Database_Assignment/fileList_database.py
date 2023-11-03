import sqlite3

# we create a tuple:

fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

# the conn variable is holding our connection to the database
# it creates an empty database file

conn = sqlite3.connect('fileList.db')

# the cur variable will be operating on the database by accessing the cursor() object.
# the cursor() object allows Python code to execute SQL queries in a database session.

with conn:
    cur = conn.cursor()
    # we create the table and its columns:
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files (\
    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
    col_fileNames TEXT)")
    # we loop through the global variable named fileList and find the files that end with .txt:
    for filename in fileList:
        if(filename.endswith('.txt')):
            # using the execute statement we insert those files into the column "col_fileNames"
            cur.execute("INSERT INTO tbl_files(col_fileNames) VALUES (?)", (filename,))
            print(filename)
    conn.commit() # = save
conn.close() # = close connection


