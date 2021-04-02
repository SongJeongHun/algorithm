def bin(x):
    tmp=x
    bin=""
    while(tmp>=1):
        if tmp%2==0:
            bin="0"+bin
            print(tmp)
        else:
            bin="1"+bin
            print(tmp)
        tmp=int(tmp/2)
    if tmp==1:
        bin="1"+bin
    return bin
print(bin(int(input())))
