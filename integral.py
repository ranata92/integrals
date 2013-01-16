def gates(func, *args):
#    def decorator(func): del...
    def wrapped(a,b):
        #return str(((a/2.0)*upper*upper+b*upper)-((a/2.0)*lower*lower+b*lower))
        return func(a, b, *args)
        
    return wrapped
    

@gates(1,2)
def integral(a,b):   ## here all logic should be encapsulated
    a=a/2.0
    return str(a)+'x^2 + '+ str(b) + 'x+C'

def main():
    print integral(2,3)

if __name__ == "__main__":
    main()
