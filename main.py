import json

number_plate = str(input("whats the number plate"))
parking_duration = int(input("how many hours do you want to park"))

paymount_amount = (parking_duration * 2) - 0.01
print(f"£{(parking_duration * 2) - 0.01}")

infoSet = {"plate":number_plate,
           "duration":parking_duration,
           "paid":False,
           "inParkingArea":False,
           "chargeDue":paymount_amount
        }

json.dumps(infoSet)

with open("infoSet.txt", "w") as file:
    json.dump(infoSet, file)