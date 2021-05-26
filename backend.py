import sqlite3

class Database:
    
    def __init__(self, db):                           # Constructor # when you call the class this function is executed but not the other once. The other ones are executed only when you refer to them.
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        self.conn.commit()
        #conn.close()                    # Means connection is open as this(conn.close()) is commented

    def insert(self,title,author,year,isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()
        return rows

    def search(self,title="",author="",year="",isbn=""):            # Now by using ="" we can pass any argument of our choice and it will not give an error.
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
        rows=self.cur.fetchall()
        return rows  
    
    def delete(self,id):                      # In delete function we expect the id of the book to be given to delete that entire row of tuple.
        self.cur.execute("DELETE FROM book WHERE id=?", (id,))
        self.conn.commit()


    def update(self,id,title,author,year,isbn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title,author,year,isbn,id))      #put parameters in correct order as stated in query i.e 1st title,then author and at last id. because order matters
        self.conn.commit()     
    
    def __del__(self):         
        self.conn.close()


#insert("The Earth","John Smith",1918,52265415262)
#print(search(author="John Smith"))    
#delete(3)
#update(1,"The moon","John Smith",1971,6252622526)
#print(view())

