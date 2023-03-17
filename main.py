import dbhelper
import menu

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
                db.insertRow(row)
            case "2":
                back = None
                db.printTable()
                while back == None:
                    print("\nPRESS [ENTER] TO GO BACK")
                    back=input()
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



