import os, re,json
def file_present(fname):
    if not os.path.exists(fname):
        a=open(fname,"w+")
        a.write("[]")
def data_read(fname):
    b=open(fname,"r")
    c=json.loads(b.read())
    return c
def singup(fname):
    Name=input("Enter the name :")
    password= input("Enter your password :")
    if len(password)>=8:
        if not(re.search("[0-9]",password) and (re.search("[A-Z]",password)) ):
            print("invalid")
        else:
            print("right")
            com_password=input("Enter the comfirm password :")
            if password==com_password:
                print("correct")
                Age=int(input("Enter the age :"))
                if Age>10:
                    Mobile_no=input("Enter the mobile number :")
                    if len(Mobile_no)==10:
                        Gender=input("Enter the Gender :")
                        Hobbies=input("Enter the Hobbies :")
                        Description=input("Enter the Descreiption :")
                    else:
                        print("please enter valid mobil no ")
                else:
                    ("sorry your can't singup")
            else:
                print("wrong")
        json_data=data_read(fname)
        for i in json_data:
            if i["Name"]==Name:
                print("user name is already exist")
                # return " "
        # password=({"Name":Name,"Password":password,"Details":{"Age":Age,"Mobile Number":Mobile_no,"Hobbies":Hobbies,"Description":Description}})
        # json_data.append(password)
        json_data.append({"Name":Name,"Password":password,"Details":{"Age":Age,"Mobile Number":Mobile_no,"Hobbies":Hobbies,"Description":Description}})
        a=open(fname,"w+")
        b=json.dumps(json_data,indent=4)
        a.write(b) 
        print("singup sucessful")
def login(fname):
    name=input("Enter the name :")
    password1= input("Enter your password :")
    json_data=data_read(fname)

    for i in json_data:
        if i["Name"]==name and i["Password"]==password1:
            print("login sucessful")
            print(i)
        elif i["Name"]==name and i["Password"]!=password1:
            print("check password")
        elif i["Name"]!=name and i["Password"]==password1:
            print("check username")
fname="longin_singup.json"
file_present(fname)
print(".....Welcome to loging or singup page....")
option=input("login or singup (login,singup):")
if option=="login":
    login(fname)
elif option=="singup":
    singup(fname)
else:
    print("check")
