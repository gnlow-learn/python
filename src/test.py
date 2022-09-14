from inspect import isclass, signature, isfunction
from numpy.typing import NDArray, DTypeLike
import typing
import re
from types import GenericAlias
import numpy as np

def plus(a: NDArray[np.int8], b: NDArray | str):
    return a + b

def parseType(annotation):
    return re.compile(r'<class \'(.*)\'>').match(str(annotation)).group(1)

for k, v in signature(plus).parameters.items():
    print(k, v.annotation, v.annotation == NDArray[np.int8])

#print(re.compile(r'<class \'(.*)\'>').match("<class 'int'>").group(1))
print(type(np.array([1,2,3])))
print(list(signature(plus).parameters.items()))