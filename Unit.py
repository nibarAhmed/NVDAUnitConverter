from enum import Enum
#in order to be able to use string based enums you need to inherit the str class. In python 3.11 this is no longer the case. 
class Unit(str, Enum):
    #this enum is used to store units. Each unit will also have diferent values that indicates from what they can be converted to.
    farenheightToCelsius="farenheight to celsius",
    celsiusToFarenheight="celsius to farenheight"
    def getAllValues():
        values=[]
        for i in Unit:
            values.append(i.value)
        return values