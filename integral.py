def gates(func):
    def wrapped(a,b,lower=2,upper=1):
        if lower and upper:
            return str((a/2.0)*upper*upper+b*upper-(a/2.0)*lower*lower+b*upper)
        else:
            return func(a,b)
    return wrapped

@gates
def integral(a,b):
    a=a/2.0
    print a
    return str(a)+'x^2 + '+ str(b) + 'x+C'

def main():
    print integral(2,3)

if __name__ == "__main__":
    main()
