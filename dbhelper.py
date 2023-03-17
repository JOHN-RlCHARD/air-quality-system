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
    
    def checkTableExists(self):
        try:
            self.cursor.execute("SELECT * FROM airquality")
        except:
            return False
        return True
    