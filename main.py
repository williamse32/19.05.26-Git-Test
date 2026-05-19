import json

hourly_rate = 2
number_plate = str(input("whats the number plate"))
parking_duration = int(input("how many hours do you want to park"))

paymount_amount = (parking_duration * hourly_rate) - 0.01
print("Amount Due", f"£{(parking_duration * hourly_rate) - 0.01}")

infoSet = {"plate":number_plate,
           "duration":parking_duration,
           "paid":False,
           "inParkingArea":False,
           "chargeDue":paymount_amount
        }

json.dumps(infoSet)

with open("infoSet.txt", "w") as file:
    json.dump(infoSet, file)
