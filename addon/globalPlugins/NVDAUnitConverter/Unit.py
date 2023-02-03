# NVDA unit converter
# copyright 2023 Nibar Ahmed. Licensed under GPLv2.
from enum import Enum
#in order to be able to use string based enums you need to inherit the str class. In python 3.11 this is no longer the case. 
class Unit(str, Enum):
    #this enum is used to store units. Each unit will also have diferent values that indicates from what they can be converted to.
    farenheightToCelsius="farenheight to celsius",
    celsiusToFarenheight="celsius to farenheight"
    OunceToGram="ounce to gram"
    gramToOunce="gram to ounce"
    footToMeter="foot to meter"
    meterToFoot="meter to foot"
    def getAllValues():
        values=[]
        for i in Unit:
            values.append(i.value)
        return values
    #the convert function will convert between diferent units. It needs a unit to convert to and the value to be converted. The function then compares the unit recieved from the UI to an enum of weights and performs the convertion.
    def convert(unit, value):
        if Unit.celsiusToFarenheight.value ==unit:
            return (value*9/5)+32
        elif Unit.farenheightToCelsius.value==unit:
            return round ((value-32)*5/9, 3)
        elif Unit.OunceToGram.value==unit:
            return round(value*28.35, 3)
        elif Unit.gramToOunce.value==unit:
            return round(value/28.35, 3)
        elif Unit.footToMeter.value==unit:
            return round(value/3.281, 3)
        elif Unit.meterToFoot.value==unit:
            return round(value*3.281, 3)