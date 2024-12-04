import sqlite3
def initiate_db():
   contec = sqlite3.connect("Products.db")
   cursor = contec.cursor()

   cursor.execute('''
   CREATE TABLE IF NOT EXISTS Prod(
   id INTEGER PRIMARY KEY,
   title TEXT NOT NULL,
   description TEXT,
   price INTEGER NOT NULL
   )
   ''')
   cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Prod (title)")

   #for i in range(4):
      #cursor.execute("INSERT INTO Prod (title, description, price) VALUES (?, ?, ?)", (f"{input()}", f'{input()}', f"{int(input())}"))
   cursor.execute("SELECT * FROM Prod")
   produ = cursor.fetchall()
   o = []
   for i in produ:
      a = []
      for j in i:
         a.append(j)
      o.append(a)

   contec.commit()
   contec.close()
   return o

def get_all_products():
   o = initiate_db()
   return o
get_all_products()