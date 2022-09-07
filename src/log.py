from inspect import isclass, isfunction

def iprint(indent, *str):
    print(" " * (4 * indent - 1), *str)

def log(data, indent=0):
    for k, v in data.__dict__.items():
        if isclass(v):
            iprint(indent, k.replace("_", " ") + ":")
            log(v, indent + 1)
        else:
            if isfunction(v):
                iprint(indent, k.replace("_", " ") + ":", v())

def star(f):
    return lambda args: f(*args)