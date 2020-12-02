import os

print("Launching new terminal to install python dependencies\n\n")
os.system("start /wait pip3 install -r ./requirements.txt")
print("Now running script to setup database............:)\n")
os.system("python Backend/conn.py")
os.system("python Backend/setup_database.py")
os.system("start /b jupyter notebook Main.ipynb")
os.system("exit")
