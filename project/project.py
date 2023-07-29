import cv2,csv,pyttsx3,sys
from prettytable import PrettyTable
from validator_collection import is_email
from pyzbar.pyzbar import decode
students=[]

def main():

  if len(sys.argv) == 2 and is_argument(sys.argv[1]):

    if sys.argv[1] =="-man":
      sys.exit("\033[1mArguments    Use  \033[0m\n-v   --Validate a Qrcode or Barcode of Student and print details\n   -a   --Add Student Details to Qrcode or Barcode\n   -d   --Delete Details of Student")

    if C:=BarcodeReader():

      if sys.argv[1] == "-v":

        if validate(C):

          x=PrettyTable(["name","department","code","phone","address","email"])
          with open("students.csv") as file1:
            reader=csv.DictReader(file1)
            for r in reader:
              if r["code"] == C :
                x.add_row([r["name"],r["department"],r["code"],r["phone"],r["address"],r["email"]])
          print(x)
          Say("Student Found")
        else:
          Say("Student Not Found")
          print("Student Not Found")

      elif sys.argv[1] == "-a":

        if validate(C):
          Say("Student Already Present")
          sys.exit("Student Already Present")

        name,department,phone,address,email=InputReader()
        code=C

        if name and department and phone and address and email:
          with open("students.csv","a",newline="") as file:
            writer=csv.DictWriter(file,fieldnames=["name","department","code","phone","address","email"])
            writer.writerow({"name":name,"department":department,"code":code,"phone":phone,"address":address,"email":email})

        else:
          sys.exit("Input All Values Correctly")

      elif sys.argv[1] == "-d":

        temp=[{"name":"name","department":"department","code":"code","phone":"phone","address":"address","email":"email"}]
        with open("students.csv") as file1:
          reader=csv.DictReader(file1)
          for r in reader:
              if r["code"] != C :
                  temp.append({"name":r["name"],"department":r["department"],"code":r["code"],"phone":r["phone"],"address":r["address"],"email":r["email"]})

        with open ("students.csv","w",newline="") as fw:
              writer=csv.DictWriter(fw,fieldnames=["name","department","code","phone","address","email"])
              for i in temp:
                writer.writerow(i)
    else:
      sys.exit()
  else:
    sys.exit("Invalid Arguments")

def BarcodeReader():

    f=False
    cap = cv2.VideoCapture(0)
    ret,frame=cap.read()
    while ret:

      ret,frame=cap.read()
      cv2.imshow("RealTime Scanner",frame)
      if barcode := decode(frame):
        f = barcode[0].data.decode("ascii")
      if (cv2.waitKey(1) & 0xFF == ord('q') ) or f :
        break

    cap.release()
    cv2.destroyAllWindows()
    return f

def BarcodeReaderImg(x):
      if open(x):
        img=cv2.imread(x)
        if barcode := decode(img):
          f = barcode[0].data.decode("ascii")
          return f
        else:
          return "Invalid Barcode or Qrcode"
      else:
        raise FileNotFoundError

def InputReader():

  try:

    N=input("Name: ").title().strip()
    B=input("Department: ").upper().strip()
    P=input("Phone_Number: ")
    A=input("Address: ")
    E=input("Email: ")


    assert N.replace(" ","").isalpha()
    assert B.replace(" ","").isalpha()
    assert P.isdigit()
    assert is_email(E)

  except AssertionError:

    sys.exit("Input All Values Correctly")

  return N,B,P,A,E

def validate(x):

  with open("students.csv") as file:

      reader=csv.DictReader(file)

      for r in reader:
          students.append({"name":r["name"],"department":r["department"],"code":r["code"],"phone":r["phone"],"address":r["address"],"email":r["email"]})

      for sd in students:

        if sd["code"]==x:
          return True

  return False

def Say(m):

  engine=pyttsx3.init()
  engine.say(m)
  engine.runAndWait()

def is_argument(s):
  if s in ("-man","-v","-a","d"):
    return True
  else:
    return False

if __name__ == "__main__":
    main()