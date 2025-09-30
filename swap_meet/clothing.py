class Clothing:

    """
    Clothing

Has an attribute id that is by default a unique integer
Has an attribute fabric that is by default the string "Unknown"
This attribute describes what fabric the clothing is made from; 
some example values might be "Striped", "Cotton", or "Floral"
When we instantiate an instance of Clothing, we can optionally pass in a string 
with the keyword argument fabric
Has a function get_category that returns "Clothing"
Has a stringify method that returns "An object of type Clothing with id <id value>. 
It is made from <fabric value> fabric."
For example, if we had a Clothing instance with an id of 123435 and a fabric attribute 
that holds "Wool", its stringify me
    

All three new classes and the Item class have an attribute called condition, 
which can be optionally provided in the initializer. The default value should be 0

All three new classes and the Item class have an instance method named condition_description,
 which should describe the condition in words based on the value, assuming they all range from 0 to 5.

These can be basic descriptions (eg. 'mint', 'heavily used') but feel free to have fun with 
these (e.g. 'You probably want a glove for this one...").
The one requirement is that all the classes share the same condition_description behavior.
    
    Tip: Importing Item
You'll need to refer to Item in order to declare it as a parent. To reference the Item class from these modules, try this import line:

from swap_meet.item import Item
    """

    def __init__():
        pass
