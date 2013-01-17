def gates(*args):
    def decorator(func):
        def wrapped(a,b):
            return func(a, b, *args)
        return wrapped
    return decorator


@gates(1,2)
def integral(a,b,*args):
    if args:
        return str(((a/2.0)*args[1]*args[1]+b*args[1])-((a/2.0)*args[0]*args[0]+b*args[0]))
    else:
        a=a/2.0
        return str(a)+'x^2 + '+ str(b) + 'x+C'

def main():
    print integral(2,3)

if __name__ == "__main__":
    main()
