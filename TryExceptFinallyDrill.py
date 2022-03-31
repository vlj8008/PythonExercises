




def getInfo():
    fnum = input("\nPlease provide your first num: ")
    snum = input("\nPlease provide your second num: ")
    return fnum,snum

def calc():
    go = True
    while go == True:
        fnum, snum = getInfo()
        try:
            var3 = int(fnum) - int(snum)
            go = False
        except ValueError as e:
            print("{}\n\nYou did not provide the right data".format(e))
        finally:
            print("\n\n moving on.....")
    print(" {}, minus {} equals {} !".format(fnum, snum, var3))


if __name__ == "__main__":
    calc()      
