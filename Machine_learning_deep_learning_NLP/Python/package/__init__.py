"""

__init__.py file is used for converting the folder into a package.

there are few options for __init__.py file:

1. it can be empty and just act as a package indicator.

2. import specific functions or classes 
example : from .maths import addition , subtraction  -> this in __init__.py file 
from package import addition -> this in test.py file or main file 

3.control what gets exported using the __all__
example : from .maths import addition , subtraction ,multiply
__all__ = ["addition","multiply]


"""

