import getpass
import oracledb

## DB CONNECTION
pw = getpass.getpass("Enter password: ")

connection = oracledb.connect(
    user="system",
    password=pw,
    dsn="localhost/xepdb1")

print("Successfully connected to Oracle Database")

cursor = connection.cursor()


## CREATE TABLE
def createTable():
    cursor.execute("""
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

##createTable()

## INSERT
def insertRow(row):
    rows = [ ("Task 1", 0 ),
            ("Task 2", 0 ),
            ("Task 3", 1 ),
            ("Task 4", 0 ),
            ("Task 5", 1 ) ]

    ##cursor.executemany("insert into measures (description, done) values(:1, :2)", rows)
    cursor.execute("INSERT INTO airquality (measuredate, mp10, mp25, o3, co, no2, so2) VALUES (TO_TIMESTAMP(:1, 'DD-MM-YYYY'), :2, :3, :4, :5, :6, :7)", row)
    print(cursor.rowcount, "Row Inserted")

    connection.commit()

data = [ '13-03-2023', 15, 12, 13, 15, 10, 11]
##insertRow(data)

#Now query the rows back


def printMenu():
    print("\n***** MENU *****")
    print("[1] - INSERT DATA")
    print("[2] - PRINT ALL DATA\n")

## MAIN
print("\n\n******************************************")
print("****** WELCOME TO AIRQUALITY SYSTEM ******")
print("******************************************\n")

opt = -1

while opt != 0:

    printMenu()

    opt = input()

    match opt:
        case "1":
            ## INSERT A ROW
            row = []
            print("Measure Date(DD-MM-YYYY): ")
            row.append(input())
            print("MP10: ")
            row.append(input())
            print("MP2.5: ")
            row.append(input())
            print("O3: ")
            row.append(input())
            print("CO: ")
            row.append(input())
            print("NO2: ")
            row.append(input())
            print("SO2: ")
            row.append(input())
            insertRow(row)
        case "2":
            ## PRINT TABLE
            print("\nID\tDATE\t\tMP10\tMP2.5\tO3\tCO\tNO2\tSO2")
            for row in cursor.execute('SELECT * FROM airquality'):
                print(str(row[0])+"\t"+str(row[1].day)+"-"+str(row[1].month)+"-"+str(row[1].year)+"\t"+str(row[2])+"\t"+str(row[3])+"\t"+str(row[4])+"\t"+str(row[5])+"\t"+str(row[6])+"\t"+str(row[7]))
        case "0":
            ## LEAVE SYSTEM
            print("LEAVING SYSTEM...")
            opt = 0
            break
        case _:
            ## DEFAULT CASE
            print("\nINVALID OPTION\n")



