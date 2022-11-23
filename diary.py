from replit import db
import datetime, time, os

password = "boomShakaLaka"
userPassword = input("Input your password? > ")
print()
time.sleep(.3)
os.system("clear")

while True:
  print("My Diary")
  print()
  if password != userPassword:
    break

  if password == userPassword:
    menu = input("1.Add\n2.View\n> ")
    if menu == "1":
      entry = input("Type entry: ")
      timestamp = datetime.datetime.now()
      key = f"mes{timestamp}"
      db[key] = entry
      
    elif menu == "2":
      matches = db.prefix("mes")
      keepGoing = True
      while keepGoing:
        for i in matches:
          print(db[i])
          print()
          carryOn = input("Do you want to exit or see the next entry? > ").lower()
          if carryOn == "exit":
            keepGoing = False
            break
          else:
            time.sleep(.5)
            os.system("clear")
            continue
  time.sleep(1)
  os.system("clear")
