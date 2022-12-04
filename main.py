#try:
import lib

#init class InstallPackage and setup default configuration for pentest
tools = lib.InstallPackage("default.txt")

while True:
    print(lib.InstallPackage.__doc__)

    command = input("Введи название команды(): ")
    eval(f"tools.{command}")
#except:
#    print("ОшибОЧКА")