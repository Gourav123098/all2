import os

def folder(path , file , dot):
    os.chdir(path)
    filee = open(f"{file}")
    re = filee.read().split("\n")
    filee.close()    

    p = 1
    files2 = []
    files3 = []
    files = os.listdir(path)
    for i in files:
        if i not in re:
            files2.append(i)      
    for i in files:
        if i  in re:
            files3.append(i)      

    for i in files2:
        if ((f".{dot}") in i) and file not in i:
            os.rename(i,f"{p}.txt")
            p += 1
       
    for i in files3:
            os.rename(i,i.capitalize())  



folder("C:\\Python39\\code\\sample_for_folder","aaa.txt","txt")    
# a = input("\n")
# b = input("\n")
# c = input("\n")
# folder(a,b,c) 