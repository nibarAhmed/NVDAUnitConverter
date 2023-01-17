import Unit
class Converter:
#the convert function will convert between diferent units. It needs a unit to convert to and the value to be converted. The function then compares the unit recieved from the UI to an enum of weights and performs the convertion.
    def convert(unit, value):
        if Unit.Unit.celsiusToFarenheight.value ==unit:
            return (value*9/5)+32
        elif Unit.Unit.farenheightToCelsius.value==unit:
            return round ((value-32)*5/9, 3)