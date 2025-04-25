# Write a class called Converter. The user will pass a length and a unit when declaring an object
# from the class—for example, c = Converter(9,'inches'). The possible units are inches, feet,
# yards, miles, kilometers, meters, centimeters, and millimeters. For each of these units there
# should be a method that returns the length converted into those units. For example, using the
# # Converter object created above, the user could call c.feet() and should get 0.75 as the result.

conversion_dict = { "inches" : 39.3701,
                        "feet" : 3.28084,
                        "yards":1.09361,
                        "miles" : 0.000621371,
                        "kilometers" :0.001,
                        "centimeters" : 100,
                        "millimeters" : 1000
                        }

class Converter:
    def __init__(self,leng,unit_):
        # if unit_ == "inches":
        self.leng = leng/conversion_dict[unit_]#in meters
        

        
    def inches(self):
        self.inch = self.leng * 39.3701
        return print(self.inch)
    def feet(self):
        self.feet = self.leng * 3.28084
        return print(self.feet)
    def yards(self):
        self.yards = self.leng * 1.09361
        return print(self.yards)

    def miles(self):
        self.miles = self.leng * 0.000621371
        return print(self.miles)

    def kilometers(self):
        self.kilometers = self.leng / 1000
        return print(self.kilometers)

    def meters(self):
        self.meters = self.leng
        return print(self.meters)

    def centimeters(self):
        self.centimeters = self.leng * 100
        return print(self.centimeters)

    def millimeters(self):
        self.millimeters = self.leng * 1000
        return print(self.millimeters)

u1 = Converter(9,"inches")
u1.feet()
    



