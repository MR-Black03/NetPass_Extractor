from subprocess import getoutput as cmd
from Banner import banner
from colorama import Fore,Style
from time import sleep
import json
#------------------------------------------------------
def show_all():
    print(Fore.GREEN+"This may take alittle time. Please wait ... "+"\n")
    #This is the first function
    result = cmd("netsh wlan show profile").split()
    #don't change this i
    first_index = 18
    #make a list to add the wifi names to it
    wifi_list = []
    #add the wifi names to list
    while True:
        try:
            if result[first_index] not in wifi_list:
                wifi_list.append(result[first_index])
                first_index = first_index+5
        except IndexError : break

    for i in wifi_list:
        wifi_details = cmd("netsh wlan show profile name="+i).split()[100]
        if wifi_details == "Present": pass
        else:
            wifi_list.remove(i)
    #make a dict to add the wfi name and its pass to it
    passwd_dict = {}

    for i in wifi_list:
        wifi_passwd = cmd("netsh wlan show profile name="+i+" key=clear").split()
        wifi_passwd = wifi_passwd[104]
        passwd_dict[i] = wifi_passwd

    print(Fore.GREEN+"Here is the list of your saved password : "+"\n")
    sleep(1)
    print(Fore.MAGENTA+str(passwd_dict))
    choice = input("Do you want to turn back to main page?(y/n) => ")
    if choice == "y":
        banner()
        main()
    else: 
        print("So I am going to determine my self ... "+"\n")
        input("Please press any key to exit ... ")
        print(Style.RESET_ALL)
        exit()
#-------------------------------------------------------------------
#Extraction function
def extract():
    print(Fore.GREEN+"This may take alittle time. Please wait ... "+"\n")
     #This is the second function
    result = cmd("netsh wlan show profile").split()
    #don't change this:
    first_index = 18
    #make a list to add the wifi names to it
    wifi_list = []
    #add the wifi names to list
    while True:
        try:
            if result[first_index] not in wifi_list:
                wifi_list.append(result[first_index])
                first_index = first_index+5
        except IndexError : break

    for i in wifi_list:
        wifi_details = cmd("netsh wlan show profile name="+i).split()[100]
        if wifi_details == "Present": pass
        else:
            wifi_list.remove(i)
    #make a dict to add the wfi name and its pass to it
    passwd_dict = {}

    for i in wifi_list:
        wifi_passwd = cmd("netsh wlan show profile name="+i+" key=clear").split()
        wifi_passwd = wifi_passwd[104]
        passwd_dict[i] = wifi_passwd
    file_name = input(Fore.LIGHTBLACK_EX+"Please Enter your filename(without .txt,etc) => ")
    f= open(f"{file_name}.txt","w").write(json.dumps(passwd_dict))
    print(Fore.GREEN+f"The {file_name} has been created successfully.")
    choice = input(Fore.RED+"Do you want to turn back to main page?(y/n) => ")
    if choice == "y":
        banner()
        main()
    else: 
        print("So I am going to determine my self ... ")
        input("Please press any key to exit ... ")
        print(Style.RESET_ALL)
        exit()
#--------------------------------------------------------------------
#User choice function
def you_choose():
    #This is the third function
    result = cmd("netsh wlan show profile").split()
    #don't change this
    first_index = 18
    #make a list to add the wifi names to it
    wifi_list = []
    #add the wifi names to list
    while True:
        try:
            if result[first_index] not in wifi_list:
                wifi_list.append(result[first_index])
                first_index = first_index+5
            else:pass
        except IndexError : break
    number = 0
    for i in wifi_list:
        print(Fore.CYAN+f"{number}.{i}")
        number = number+1
    while True:
        try:
            user_choice = int(input(Fore.LIGHTGREEN_EX+"Please Enter the number of the WIFI SSID which you want to extract its password => "))
            wifi = wifi_list[user_choice]
            wifi_passwd = cmd("netsh wlan show profile name="+i+" key=clear").split()
            wifi_passwd = wifi_passwd[104]
            print(Fore.LIGHTBLUE_EX+f"The password of '{wifi}' is "+Fore.BLUE+f"'{wifi_passwd}'")
            print("-------------------------------------------------------------------------")
            print(Style.RESET_ALL)
            choice = input(Fore.RED+"Do you want to turn back to main page?(y/n/exit) => ")
            if choice == "y":
                banner()
                main()
            if choice == "n":
                banner()
                you_choose()
            if choice == "exit": 
                print("So I am going to determine my self ... ")
                input("Please press any key to exit ... ")
                print(Style.RESET_ALL)
                exit()
        except ValueError:
            print(Fore.RED+"You are entering your Value in a wrong form.Please try again ..."+Style.RESET_ALL)
#----------------------------------------------------------
#Authorize Function
#if you changed the program and want to add your name do it but don't delete my name please.
def authorize():
    print(Fore.BLUE+"Author : MR-Black03")
    print(Fore.GREEN+"My Github Profile is : https://github.com/MR-Black03")
    choice = input(Fore.RED+"Do you want to turn back to main page?(y/n) => ")
    if choice == "y":
        banner()
        main()
    else: 
        print("So I am going to determine my self ... ")
        input("Please press any key to exit ... ")
        print(Style.RESET_ALL)
        exit()
#----------------------------------------------------------
#main function
def main():
    print(Fore.CYAN+"Welcome , hope this app can be helpful")
    print(Fore.LIGHTRED_EX+"""Options:
    1-Extract Selected WIFI Password
    2-Extract All Saved WIFI Password
    3-Extract All Saved WIFI Password(in a txt fil)
    4-Authorize

Note:if you want to exit press 'CTRL+C'"""+Style.RESET_ALL)
    print("\n")
    choice = input(Fore.LIGHTYELLOW_EX+"Please Choose The Option You Want => ")
    if choice == "1":
        banner()
        you_choose()
    if choice == "2":
        banner()
        show_all()
    if choice == "3":
        banner()
        extract()
    if choice == "4":
        banner()
        authorize()
    else:
        print(Fore.RED+"Please read the Manual first the try to use this app")
        input(Fore.RED+"Press any key to exit"+Style.RESET_ALL)
#----------------------------------------------------------
#Now the main code began
try:
    while True:
        banner()
        main()
except KeyboardInterrupt:
    print("\n"+Fore.GREEN+"Goodbye ... "+Style.RESET_ALL)
    input("Press any key to exit ... ")
except ModuleNotFoundError:
    banner()
    print(Fore.RED+"Please install denpendencies by "+Fore.BLUE+"'python3 -m pip install -r requirements.txt'"+Fore.RED+" first"+Style.RESET_ALL)