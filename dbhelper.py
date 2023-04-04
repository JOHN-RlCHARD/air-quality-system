import getpass
import oracledb


class DbHelper:
    status = "disconnected"

    def __init__(self):
        pw = getpass.getpass("Enter password: ")

        try:
            self.connection = oracledb.connect(
                user="system",
                password=pw,
                dsn="localhost/xepdb1")

            self.cursor = self.connection.cursor()
            self.status = "connected"
            print("Successfully connected to Oracle Database")

        except:
            print("Could not connect to Database")

        
        
    ## CREATE TABLE
    def createTable(self):
        self.cursor.execute("""
            CREATE TABLE airquality (
                id NUMBER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1),
                measuredate TIMESTAMP,
                mp10 NUMBER(3),
                mp25 NUMBER(3),
                o3 NUMBER(3),
                co NUMBER(3),
                no2 NUMBER(3),
                so2 NUMBER(3)
            )""")
        
    ## INSERT
    def insertRow(self, row):
        if not self.checkTableExists(): self.createTable()
        
        self.cursor.execute("INSERT INTO airquality (measuredate, mp10, mp25, o3, co, no2, so2) VALUES (TO_TIMESTAMP(:1, 'DD-MM-YYYY'), :2, :3, :4, :5, :6, :7)", row)
        print(self.cursor.rowcount, "Row Inserted")

        self.connection.commit()

    ## UPDATE ROW
    def updateRow(self, row):
        if not self.checkTableExists():
            print("Table is empty")
            return

        self.cursor.execute("UPDATE airquality SET "+row[1]+" = "+row[2]+" WHERE id = "+row[0])
        print(self.cursor.rowcount, "Row Altered")
        if (self.cursor.rowcount == 0): print("There is no Row with id = "+row[0])

        self.connection.commit()

    ## PRINT TABLE
    def printTable(self):
        if not self.checkTableExists():
            print("Table is empty")
            return

        print("\n-------------------------------------------------------------------------")
        print("| ID\tDATE\t\tMP10\tMP2.5\tO3\tCO\tNO2\tSO2\t|")
        for row in self.cursor.execute('SELECT * FROM airquality'):
            print("| "+str(row[0])+"\t"+str(row[1].day)+"-"+str(row[1].month)+"-"+str(row[1].year)+"\t"+str(row[2])+"\t"+str(row[3])+"\t"+str(row[4])+"\t"+str(row[5])+"\t"+str(row[6])+"\t"+str(row[7])+"\t|")
        print("-------------------------------------------------------------------------")

    ## DELETE ROW
    def deleteRow(self, rowId):
        self.cursor.execute("DELETE FROM airquality WHERE id = "+rowId)
        print(self.cursor.rowcount, "Row Deleted")
        if (self.cursor.rowcount == 0): print("There is no Row with id = "+rowId)

        self.connection.commit()

    ## DROP TABLE
    def dropTable(self):
        if not self.checkTableExists():
            print("Table is empty")
            return

        self.cursor.execute("DROP TABLE airquality")
        print("Table droped")

        self.connection.commit()

    ## GET DATA FROM ROW
    def getRow(self, rowId):
        res = []
        if not self.checkTableExists():
            print("Table is empty")
            return

        for row in self.cursor.execute('SELECT * FROM airquality'):
            if (str(row[0]) == rowId): 
                res.append(row[2])
                res.append(row[3])
                res.append(row[4])
                res.append(row[5])
                res.append(row[6])
                res.append(row[7])

        if (res == []): print("There is no Row with id = "+rowId)

        return res
    
    ## GET DATA FROM ALL ROWS AND RETURN AVARAGE
    def getAllRowData(self):
        res = []
        mp10, mp25, o3, co, no2, so2 = 0, 0, 0, 0, 0, 0
        if not self.checkTableExists():
            print("Table is empty")
            return
        i = 0
        for row in self.cursor.execute('SELECT * FROM airquality'):
            i = i+1
            mp10 = mp10 + int(row[2])
            mp25 = mp25 + int(row[3])
            o3 = o3 + int(row[4])
            co = co + int(row[5])
            no2 = no2 + int(row[6])
            so2 = so2 + int(row[7])
        res.append(mp10/i)
        res.append(mp25/i)
        res.append(o3/i)
        res.append(co/i)
        res.append(no2/i)
        res.append(so2/i)

        return res

    def checkTableExists(self):
        try:
            self.cursor.execute("SELECT * FROM airquality")
        except:
            return False
        return True
    