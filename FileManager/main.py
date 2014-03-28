import shutil
import os
import sys

def cp(instr):
    try:
        spltd = instr.split()
        if os.path.isdir(spltd[0]):
            shutil.copytree(spltd[0], spltd[1])
        else:
            shutil.copy(spltd[0], spltd[1])
    except Exception as e:
        print(e.strerror)

def mv(instr):
    try:
        spltd = instr.split()
        shutil.move(spltd[0], spltd[1])
    except:
        print(e.strerror)

def cd(instr):
    try:
        spltd = instr.split()
        os.chdir(spltd[0])
    except:
        print(e.strerror)
        
def ls(instr):
    try: 
        for fil in os.listdir():
            print(fil)
    except:
        print(e.strerror)

def rm(instr):
    try:
        spltd = instr.split()
        
        if os.path.isdir(spltd[0]):
            shutil.rmtree(spltd[0])
        else:
            os.remove(spltd[0])
    except:
        print(e.strerror)
    
def pwd(instr):
    try:
        print(os.getcwd())    
    except Exception as e:
        print(e.strerror)
        
def ext(instr):
    sys.exit(0)
    
def hlp(instr):
    print('My commands:')
    print('cd dir        change directory to src')
    print('ls            show all files in current directory')
    print('cp dst src    copy file/dir dst to src')
    print('mv dst src    move file/dir dst to src')
    print('rm src        remove file/dir')
    print('pwd           show current directory')
    print('exit          close this program')
    
a = {'mv': mv, 'cp': cp, 'cd':cd, 'ls':ls, 'cp':cp, 'rm':rm, 'pwd':pwd, 'exit':ext, 'help':hlp}

print("Hello there! I'm file manager made by DenisK!")
print("Print help to get help")
print()

while(1):
    print('[',os.getcwd().split(os.sep)[-1],']',end='? ', sep='')
    instr = input().split(" ",1)
    instr.append("")
    try:
        a[instr[0]](instr[1])
    except Exception as e:
        print("Wrong command!")