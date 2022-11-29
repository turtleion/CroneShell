import os
import sys
import PySimpleInput
import shutil

class Library:
    def mov(self):
        print("yea")

    def print(self, printableStr):
        print(printableStr)

    def cop(self):
        print("bassas")

    def ren(self):
        print("ngenennnn")


class Shell():
    cache_dir = "data/cache/"
    def __init__(self):
        # onBoot clean cache
        print("Cleaning cache on: data/cache")
        os.system("rm " + self.cache_dir + "*")
        self.malibs = Library()
        self.s = PySimpleInput.PySimpleInput()
        self.CMD_TTL = 4
        self.CMD_PRINT = {"name": "print", "executetable": self.malibs.print,"argneeded": 1}
        self.CMD_MOV = {"name": "mov", "executetable": self.malibs.mov,"argneeded": 2}
        self.CMD_CP = {"name": "cop", "executetable": self.malibs.cop,"argneeded": 2}
        self.CMD_REN = {"name": "ren", "executetable": self.malibs.ren,"argneeded":2}
        self.CMD_EXIT = {"name": "exit"}
        self.CMD_ALL = [self.CMD_PRINT, self.CMD_MOV, self.CMD_CP, self.CMD_REN,self.CMD_EXIT]
    def libraries(self,usrI):
        CommandTemplate = { "command": "", "args": [] }
        if " " in usrI:
            #Nanti
            pass
        parsed = usrI.split(" ")
        CommandTemplate["command"] = parsed[0]
        parsed.pop(0)
        CommandTemplate["args"] = parsed
        if CommandTemplate["command"].lower() == "print":
            if (len(parsed)-1) == 1:
                pass
            else:
                #Nanti help_()
                pass
            self.CMD_PRINT["executetable"](" ".join(CommandTemplate["args"]))
        elif CommandTemplate["command"].lower() == "exit":
            exit(2)
        elif CommandTemplate["command"].lower() == "mov":
            if (len(parsed) - 1)== 2:
                pass
            else:
                #Nanti help_()
                pass
            if not os.path.isfile(CommandTemplate["args"][0]):
                print("MOV: Cannot move the file/Incorrect name/File not found")
                return None
            else:
                pass
            if "/" in CommandTemplate["args"][1]:
                dest = CommandTemplate["args"][1].split("/")
                fname = dest[len(dest) - 1]
                dest.pop(len(dest) - 1)
                destr = "/".join(dest)
                if dest[0] == "":
                    destr = "%s%s" % ("/",destr)
                if not os.path.isdir("/".join(dest)):
                    print("MOV: Cannot move the file/Incorrect patg directory")
                    return None
                try:
                    shutil.move(CommandTemplate["args"][0], CommandTemplate["args"][1])
                except shutil.Error as e:
                    print(e)
            else:
                try:
                    shutil.move(CommandTemplate["args"][0], CommandTemplate["args"][1])
                except shutil.Error as e:
                    print(e)



    def checkLibraries(self,passArg):
        e = 4
        c = 0
        while c <= self.CMD_TTL:
            try:
                if self.CMD_ALL[c]["name"] in passArg:
                    e = 5
                    break
                else:
                    e -= 1
                
                    pass   
                c+=1
            except IndexError:
                c = 0
                break
        if e >= 5:
            print("COOO")
            return True
        elif e == 0:
            return None
        

    def base(self):
        while True:
            inp = self.s.input("(SHELL:IO):",None)
            if inp == "" or inp.isspace():
                continue
            elif self.checkLibraries(inp):
                self.libraries(inp)
            else:
                print("Command not found!")
                continue
d = Shell()
d.base()
