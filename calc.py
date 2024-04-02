def main():
    print()
    x=int(input("x> "))
    y=int(input("y> "))

    if y!=0:
        print("%d/%d=%.3f" % (x,y,div(x,y)))
    else:
        div(x,y)

def div(x,y):
    if y==0:
        print("Error: cannot divide by zero.")
    else:
        return x/y
    
if __name__=="__main__":
    main()