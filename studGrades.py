import os
import time
import sys
from colorama import init, Fore
import shutil

init()

grades = []
_dir_gradeAexist = os.path.exists("C:\Python-Works\FileHandling\Grade-A")
_dir_gradeBexist = os.path.exists("C:\Python-Works\FileHandling\Grade-B")
_dir_gradeCexist = os.path.exists("C:\Python-Works\FileHandling\Grade-C")
_dir_gradeDexist = os.path.exists("C:\Python-Works\FileHandling\Grade-D")
_dir_gradeEexist = os.path.exists("C:\Python-Works\FileHandling\Grade-E")
_dir_gradeFexist = os.path.exists("C:\Python-Works\FileHandling\Grade-F")

def peruse():
    file = open("C:\Python-Works\FileHandling\student_grades.txt", 'rt')
    txtArr = file.readlines()        
    for each in txtArr:
        if txtArr.index(each) != 0:
            grades.append(each)
    print(Fore.YELLOW + '\nChecking Student Results...')            
    time.sleep(2)
    print(Fore.GREEN + '\nDone') 
    isolate()
    
def isolate():
    print(Fore.YELLOW + '\nSeparating Results...')            
    time.sleep(2)
    for each in grades:
        if each.endswith(f"A\n") or each.endswith('A'):
            file = open("C:\Python-Works\FileHandling\Grade-A\grade-A.txt", 'a')
            file.write(each)
        elif each.endswith(f"B\n") or each.endswith('B'):
            file = open("C:\Python-Works\FileHandling\Grade-B\grade-B.txt", 'a')
            file.write(each)
        elif each.endswith(f"C\n") or each.endswith('C'):
            file = open("C:\Python-Works\FileHandling\Grade-C\grade-c.txt", 'a')
            file.write(each)
        elif each.endswith(f"D\n") or each.endswith('D'):
            file = open("C:\Python-Works\FileHandling\Grade-D\grade-D.txt", 'a')
            file.write(each)
        elif each.endswith(f"E\n") or each.endswith('E'):
            file = open("C:\Python-Works\FileHandling\Grade-E\grade-E.txt", 'a')
            file.write(each)
        elif each.endswith(f"F\n") or each.endswith('F'):
            file = open("C:\Python-Works\FileHandling\Grade-F\grade-F.txt", 'a')                  
            file.write(each)
        else:
            print('Grade cannot be determined')
    print(f"{Fore.GREEN}{'-'*98}\nResults successfully separated. Check the created folders to confirm...")        

def create():
    os.mkdir("C:\Python-Works\FileHandling\Grade-A")
    os.mkdir("C:\Python-Works\FileHandling\Grade-B")
    os.mkdir("C:\Python-Works\FileHandling\Grade-C")
    os.mkdir("C:\Python-Works\FileHandling\Grade-D")
    os.mkdir("C:\Python-Works\FileHandling\Grade-E")
    os.mkdir("C:\Python-Works\FileHandling\Grade-F")
    print(f"{Fore.GREEN}\n6 Folders Created Successfully\n{'-'*98}")
    print(Fore.RED + 'Press 1 Continue or 0 to Exit...\n' + '-'*98)
    res = input(">>>> ")
    if res == '1':
        peruse()
    elif res == '0':
        sys.exit()
    else:
        print('Invalid Response...')

def remove():
    shutil.rmtree("C:\Python-Works\FileHandling\Grade-A")
    shutil.rmtree("C:\Python-Works\FileHandling\Grade-B")
    shutil.rmtree("C:\Python-Works\FileHandling\Grade-C")
    shutil.rmtree("C:\Python-Works\FileHandling\Grade-D")
    shutil.rmtree("C:\Python-Works\FileHandling\Grade-E")
    shutil.rmtree("C:\Python-Works\FileHandling\Grade-F")
    print(f"\n{Fore.GREEN}Folders Deleted Successfully\n")
    print(f"{Fore.BLUE}>>> Press 1 to Exit Operation or 0 to Recreate Deleted Folders...\n{'-'*98}")
    res = input(">>>> ")
    if res == '0':
        create()
    elif res == '1':
        sys.exit()
    else:
        print('>>> Invalid Response...')
            
if _dir_gradeAexist and _dir_gradeBexist and _dir_gradeCexist and _dir_gradeDexist and _dir_gradeEexist and _dir_gradeFexist:
    print(Fore.RED + 'Folders Already Exist')
    print(f"{'-'*98}\nPress ENTER to Remove all Folder or 1 to Exit")
    res = input("")
    if res == '':
        remove()
    elif res == '1':
        sys.exit()
    else:
        print('\nInvalid Response...')    
else:
    print(Fore.YELLOW+'\n>>> Creating Folders...')
    time.sleep(2)
    create()
    