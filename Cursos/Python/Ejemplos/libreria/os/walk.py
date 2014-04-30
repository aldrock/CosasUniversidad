import os


for root, dirs, files in os.walk("/home/rock/Git/CosasUniversidad"):
    print(root)
    for _dir in dirs:
        print(_dir)
    for _file in files:
        print(_file)
