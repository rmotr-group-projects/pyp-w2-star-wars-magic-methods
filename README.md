Star Wars Magic Methods
=====================

Today we will be exploring some of Python's magic methods while having fun with Star Wars! We are going to create some basic objects and use magic methods to do some weird things with them.

http://www.diveintopython3.net/special-method-names.html will be your guide to the various magic methods

We are also going to get you into the habit of reading tests so the readme wilbe somewhat sparse.

> **People**
> The init for the people class should take two parameters: *name* and *dark_side* (this one is an optional parameter that should have a default value of `False`)
> You need to implement methods for the following operators:  callable(`x()`), /, *, <<, >>, negative(`-x`), positive(`+x`), invert(`~x`), ^, ==
> You should also have two *properties* `light_side` and `dark_side`

> **SaberCrystal**
> Init should take one optional parameter, color, which defaults to (255,0,0), which is a tuple representing red, green, blue. There should be 3 instance attributes, red, green, and blue. There needs to also be a *property* `color` that returns a tuple with the values of red, green, and blue
> Finally you need to implement methods for the following operators: equality `==`, addition `+`, in place addition `+=`, subtraction `-`, in place subtraction `-=`, and contains `x in y`
