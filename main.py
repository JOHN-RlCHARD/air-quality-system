import dbhelper
import menu
import validators

db = dbhelper.DbHelper()

## MAIN
def main():
    print("\n\n******************************************")
    print("****** WELCOME TO AIRQUALITY SYSTEM ******")
    print("******************************************")

    opt = -1

    while opt != 0:

        menu.printMenu()

        opt = input()

        match opt:
            case "1":
                ## INSERT A ROW
                row = []
                date = ""
                while not (validators.isValidTimeStamp(date)):
                    print("Measure Date(DD-MM-YYYY): ")
                    date = input()
                row.append(date)
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
                db.insertRow(row)
            case "2":
                back = None
                db.printTable()
                if db.checkTableExists():
                    while back == None:
                        print("\nPRESS [ENTER] TO GO BACK")
                        back=input()
            case "3":
                row = []
                db.printTable()
                if db.checkTableExists():
                    print("Type the ID of the Row to be altered:")
                    row.append(input())
                    column = ""
                    while not (validators.isValidColumn(column)):
                        print("Type the column to be altered(mp10, mp25, o3, co, no2, so2):")
                        column = input()
                    row.append(column)
                    print("Type the new value for "+row[1]+":")
                    row.append(input())
                    db.updateRow(row)
            case "4":
                if db.checkTableExists():
                    db.printTable()
                    print("Type ID of the row to be deleted:")
                    rowId = input()
                    db.deleteRow(rowId)

            case "6":
                db.dropTable()
            case "0":
                ## LEAVE SYSTEM
                print("\nLEAVING SYSTEM...")
                opt = 0
                break
            case _:
                ## DEFAULT CASE
                print("\nINVALID OPTION\n")

if db.status == "connected":
    main()



