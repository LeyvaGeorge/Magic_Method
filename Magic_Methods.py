class Currency:
    currencies = {
        "CHF": 0.930023,  # swiss franc
        "CAD": 1.264553,  # canadian dollar
        "GBP": 0.737414,  # british pound
        "JPY": 111.019919,  # japanese yen
        "EUR": 0.862361,  # euro
        "USD": 1.0,
    }  # us dollar

    def __init__(self, value, unit="USD"):
        self.value = value
        self.unit = unit

    def changeTo(self, new_unit):
        """
        An Currency object is transformed from the unit "self.unit" to "new_unit"
        """
        self.value = (
            self.value / Currency.currencies[self.unit] * Currency.currencies[new_unit]
        )
        self.unit = new_unit

    # add magic methods here
    def __repr__(self):
        # This method returns the string to be printed. This should be the value rounded to two digits, accompanied by its acronym.
        return f"{round(self.value,2)} {self.unit}"

    def __str__(self):
        # This method returns the same value as __repr__(self).
        return f"{round(self.value,2)} {self.unit}"

    def __add__(self, other):
        # Defines the '+' operator. If other is a Currency object, the currency values are added and the result will be the unit of self. If other is an int or a float, other will be treated as a USD value.
        if type(other) == int or type(other) == float:      #checkes the other if it's a float or integer
            x = (other * Currency.currencies[self.unit])    # changes it to the self data type
        else:
            x = (other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit])    #removes other's unit value before changing it to self's unit value
        return Currency(x + self.value, self.unit)          # Adds both values and sends it to change to __repr__ or __str__ not sure

    def __iadd__(self,other):
        return Currency.__add__(self,other)                 # sends it __add__ method
    
    def __radd__(self,other):
        response = self + other                             # adds both values
        if self.unit != "USD":                              # checks to see if It is not "USD"
            response.changeTo("USD")
        return response                                     # returns new response 
    
    def __sub__(self,other):                                # Subtracts two classes
        if type(other) == int or type(other) == float:      # checks other if is integer or float
            x = (other * Currency.currencies[self.unit])    # changes it to the self data type
        else:
            x = (other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit])    #removes other value to chang it to self unit
        return Currency(self.value - x, self.unit)          # Subtracts both values and seds it to change to string value
    
    def __isub__(self,other):
        return Currency.__sub__(self,other)                 # Calls __sub__
    
    def __rsub__(self,other):                               
        res = other - self.value                            # result other min self value
        res = Currency(res,self.unit)                       # makes res into class currency
        if self.unit != "USD":                              # checks to self if does not equal to "USD"
            res.changeTo("USD")                             # changes response.unit to "USD"
        return res                                          # returns response

v1 = Currency(23.43, "EUR")
v2 = Currency(19.97, "USD")
print(v1 + v2)
print(v2 + v1)
print(v1 + 3) # an int or a float is considered to be a USD value
print(3 + v1)
print(v1 - 3) # an int or a float is considered to be a USD value
print(30 - v2) 


