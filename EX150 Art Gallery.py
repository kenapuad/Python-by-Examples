import sqlite3

with sqlite3.connect("Art Gallery.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Artists(
    artistid integer PRIMARY KEY,
    name text NOT NULL,
    address text,
    town text,
    county text,
    postcode text);""")

cursor.execute("""INSERT INTO Artist(ArtistID, Name, Address, Town, County, Postcode)
    VALUES("1","Martin Leighton","5 Park Place","Peterborough","Cambridgeshire","PE32 5LP")""")
db.commit()

cursor.execute("""INSERT INTO Artist(ArtistID, Name, Address, Town, County, Postcode)
    VALUES("2","Eva Czarniecka","77 Warner Close","Chelmsford","Essex","CM22 5FT")""")
db.commit()

cursor.execute("""INSERT INTO Artist(ArtistID, Name, Address, Town, County, Postcode)
    VALUES("3","Roxy Parkin","90 Hindhead Road","","London","SE12 6WM")""")
db.commit()

cursor.execute("""INSERT INTO Artist(ArtistID, Name, Address, Town, County, Postcode)
    VALUES("4","Nigel Farnworth","41 Whitby Road","Huntly","Aberdeenshire","AB54 5PN")""")
db.commit()

cursor.execute("""INSERT INTO Artist(ArtistID, Name, Address, Town, County, Postcode)
    VALUES("5","Teresa Tanner","70 Guild Street","","London","NW7 1SP")""")
db.commit()

cursor.execute("""CREATE TABLE IF NOT EXISTS Art(
    pieceID integer PRIMARY KEY,
    artistID integer,
    title text,
    medium text,
    price integer);""")

cursor.execute("""INSERT INTO Pieces(PieceID, ArtistID, Title, Medium, Price)
    VALUES("1","5","Woman with Blac Labrador","Oil","220")""")
db.commit()

cursor.execute("""INSERT INTO Pieces(PieceID, ArtistID, Title, Medium, Price)
    VALUES("2","5","Bees & Thistles","Watercolour","85")""")
db.commit()

cursor.execute("""INSERT INTO Pieces(PieceID, ArtistID, Title, Medium, Price)
    VALUES("3","2","A Stroll to Westminster","Ink","190")""")
db.commit()

cursor.execute("""INSERT INTO Pieces(PieceID, ArtistID, Title, Medium, Price)
    VALUES("4","1","African Giant","Oil","800")""")
db.commit()

cursor.execute("""INSERT INTO Pieces(PieceID, ArtistID, Title, Medium, Price)
    VALUES("5","3","Water Daemon","Acrylic","1700")""")
db.commit()

cursor.execute("""INSERT INTO Pieces(PieceID, ArtistID, Title, Medium, Price)
    VALUES("6","4","A Seagull","Watercolour","35")""")
db.commit()

cursor.execute("""INSERT INTO Pieces(PieceID, ArtistID, Title, Medium, Price)
    VALUES("7","1","Three Friends","Oil","1800")""")
db.commit()

cursor.execute("""INSERT INTO Pieces(PieceID, ArtistID, Title, Medium, Price)
    VALUES("8","2","Summer Breeze 1","Acrylic","1350")""")
db.commit()

cursor.execute("""INSERT INTO Pieces(PieceID, ArtistID, Title, Medium, Price)
    VALUES("9","4","Mr Hamster","Watercolour","35")""")
db.commit()

cursor.execute("""INSERT INTO Pieces(PieceID, ArtistID, Title, Medium, Price)
    VALUES("10","1","Pulpit Rock, Dorset","Oil","600")""")
db.commit()

cursor.execute("""INSERT INTO Pieces(PieceID, ArtistID, Title, Medium, Price)
    VALUES("11","5","Trawler Dungeness Beach","Oil","195")""")
db.commit()

cursor.execute("""INSERT INTO Pieces(PieceID, ArtistID, Title, Medium, Price)
    VALUES("12","2","Dance in the Snow","Oil","250")""")
db.commit()

cursor.execute("""INSERT INTO Pieces(PieceID, ArtistID, Title, Medium, Price)
    VALUES("13","4","St Tropez Port","Ink","45")""")
db.commit()

cursor.execute("""INSERT INTO Pieces(PieceID, ArtistID, Title, Medium, Price)
    VALUES("14","3","Pirate Assassin","Acrylic","420")""")
db.commit()

cursor.execute("""INSERT INTO Pieces(PieceID, ArtistID, Title, Medium, Price)
    VALUES("15","1","Morning Walk","Oil","800")""")
db.commit()

cursor.execute("""INSERT INTO Pieces(PieceID, ArtistID, Title, Medium, Price)
    VALUES("16","4","A Baby Barn Swallow","Watercolour","35")""")
db.commit()

cursor.execute("""INSERT INTO Pieces(PieceID, ArtistID, Title, Medium, Price)
    VALUES("17","4","The Old Working Mills","Ink","395")""")
db.commit()

db.close()