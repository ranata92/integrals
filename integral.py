def gates(lower=None,upper=None):
    def decorator(func):
        def wrapped(a,b):
            if lower and upper:
                return str(((a/2.0)*upper*upper+b*upper)-((a/2.0)*lower*lower+b*lower))
            else:
                return func(a,b)
        return wrapped
    return decorator

@gates(1,2)
def integral(a,b):
    a=a/2.0
    return str(a)+'x^2 + '+ str(b) + 'x+C'

def main():
    print integral(2,3)

if __name__ == "__main__":
    main()
