import csv
with open("aaa.csv", "w") as x:
    file=csv.writer(x)
    for i in range(1,6):
           sr=input("enter serial number")
           data=input("enter data")
           file.writerow([sr,data])
    x.close()
