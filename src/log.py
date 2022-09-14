from inspect import isclass, isfunction, signature
import numpy as np
from numpy.typing import NDArray

Int = np.int8
Float = np.float16
Arr = NDArray

def amap(f, arrayLike):
    return list(map(f, list(arrayLike)))

def paramTypes(f):
    return amap(
        lambda param: param[1].annotation,
        signature(f).parameters.items()
    )

def mock(t):
    match t:
        case Arr[Int]:
            


def iprint(indent, *str):
    print(" " * (4 * indent - 1), *str)

def log(data, indent=0):
    for k, f in data.__dict__.items():
        if isclass(f):
            iprint(indent, k.replace("_", " ") + ":")
            log(f, indent + 1)
        else:
            if isfunction(f):
                input = amap(
                    lambda t: ,
                    paramTypes(f)
                )
                iprint(
                    indent,
                    k.replace("_", " ") + ":",
                    paramTypes(f)
                )

def star(f):
    return lambda args: f(*args)