import os
from colorama import Fore,Back,Style
import getpass
import subprocess


username = getpass.getuser()



print (f"{Fore.RED}redhat, {Fore.BLUE}archlinux, {Fore.LIGHTBLUE_EX}arcolinux, {Fore.WHITE}fedora, {Fore.MAGENTA}garuda" + "\n")


num1 = str(input(f"{Style.RESET_ALL}what logo would you like?: "))


if num1 == ("archlinux"):
    oldfile = f = open("/home/" + username + "/.config/neofetch/stupid.conf", "r").read()

    f = open("/home/" + username + "/.config/neofetch/config.conf", "w")
    f.write(oldfile)

    f = open("/home/" + username + "/.config/neofetch/config.conf", "a")
    f.write("ascii_distro='archlinux'")

    print (Fore.GREEN + "Sucessful!")

elif num1 == ("redhat"):
    oldfile = f = open("/home/" + username + "/.config/neofetch/stupid.conf", "r").read()

    f = open("/home/" + username + "/.config/neofetch/config.conf", "w")
    f.write(oldfile)

    f = open("/home/" + username + "/.config/neofetch/config.conf", "a")
    f.write("ascii_distro='redhat'")

    print (Fore.GREEN + "Sucessful!")

elif num1 == ("arcolinux"):
    oldfile = f = open("/home/" + username + "/.config/neofetch/stupid.conf", "r").read()

    f = open("/home/" + username + "/.config/neofetch/config.conf", "w")
    f.write(oldfile)

    f = open("/home/" + username + "/.config/neofetch/config.conf", "a")
    f.write("ascii_distro='arcolinux'")

    print (Fore.GREEN + "Sucessful!")
    
elif num1 == ("fedora"):
    oldfile = f = open("/home/" + username + "/.config/neofetch/stupid.conf", "r").read()

    f = open("/home/" + username + "/.config/neofetch/config.conf", "w")
    f.write(oldfile)

    f = open("/home/" + username + "/.config/neofetch/config.conf", "a")
    f.write("ascii_distro='fedora'")

    print (Fore.GREEN + "Sucessful!")
    

elif num1 == ("garuda"):
    oldfile = f = open("/home/" + username + "/.config/neofetch/stupid.conf", "r").read()

    f = open("/home/" + username + "/.config/neofetch/config.conf", "w")
    f.write(oldfile)

    f = open("/home/" + username + "/.config/neofetch/config.conf", "a")
    f.write("ascii_distro='garuda'")

    print (Fore.GREEN + "Sucessful!")
   


num2 = str(input(f"{Style.RESET_ALL}would you like neofetch to automatically run when you boot up any kind of console? [y/n]: "))

if num2 == ("y"):
    f = open("/home/" + username + "/.config/neofetch/config.conf", 'a')
    f.write("neofetch")
    

    os.system("gnome-terminal")

elif num2 == ("n"):
    print ("okay!")

    os.system("gnome-terminal")








