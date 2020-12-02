import getpass
print("Enter field values:")
hosturl = input("host:")
username = input("user:")
password = getpass.getpass(prompt="password:")
with open("./config.txt", "w+") as f:
    f.write(
        f"hosturl='{hosturl}'\nusername='{username}'\npassword='{password}'")
