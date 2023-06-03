import dbhelper
import menu
import validators
import classification

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
                inputDescs = ["MP10: ", "MP2.5: ", "O3: ", "CO: ", "NO2: ", "SO2: "]
                for desc in inputDescs:
                    rowAppend = "-1"
                    while not validators.isValidMeasure(rowAppend):
                        print(desc)
                        rowAppend = input()
                        if validators.isValidMeasure(rowAppend): row.append(rowAppend)

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
                    print("Proceed to delete row "+rowId+"? (y/n)")
                    deleteOpt = input()
                    if deleteOpt == "y" or deleteOpt == "Y":
                        db.deleteRow(rowId)
                    else:
                        print("Canceled")
            case "5":
                db.printTable()
                if db.checkTableExists():
                    print("Type the ID of the Row to be classified:")
                    row = input()
                    rowData = db.getRow(row)
                    if (rowData != []):
                        classification.classify(rowData)
            case "6":
                if db.checkTableExists():
                    classification.classify(db.getAllRowData())
            case "7":
                print("Proceed to delete all data? (y/n)")
                deleteOpt = input()
                if deleteOpt == "y" or deleteOpt == "Y":
                    db.dropTable()
                else:
                    print("Canceled")
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



