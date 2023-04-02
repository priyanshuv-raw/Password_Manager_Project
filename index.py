from cryptography.fernet import Fernet

# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key","wb") as key_file:
#           key_file.write(key)
# write_key()
def view():
        with open ('passwords.text','r') as f:
            for line in f.readlines():
                data=line.rstrip()
                user,passw = data.split("|")
                print("User:",user,"\t |    Password:",fer.decrypt(passw.encode()).decode())
def viewfalse():
        with open ('passwords.text','r') as f:
            for line in f.readlines():
                data=line.rstrip()
                user,passw = data.split("|")
                print("User:",user,"\t |    Password:",passw)


def add():
    name = input("Platform: ");
    password = input("Password: ")

    with open ('passwords.text','a') as f:
        f.write(name+" | " +fer.encrypt(password.encode()).decode()+"\n")


def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("Enter your Master Password: ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

if(master_pwd=="Mustang@123"):

    while True:
        mode = input ("Would you like to add a new password or view existing ones (view,add), press q to quit.").lower()
        if mode =="q":
            break
        if mode =="view":
            view()
        elif mode == "add":
            add()
        else:
            print("Invalid Mode: ")
            continue
else:
    viewfalse()
