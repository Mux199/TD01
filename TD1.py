class Devise:
    devises = {
        'GBP': 0.89,
        'JPY': 114.34,
        'EUR': 1,
        'USD': 1.11
    }
    def __init__(self, value, devises, unit ="EUR"):
        self.value = value
        self.unit = unit

    def __str__(self):
        return "Valeur" + str(self.__value)+" "+ self.__unit

    def changeTo(self,new_unit):
        self.value = (self.value/Devise.devises[self.unit]*Devise.devises[new_unit])
        self.unit = new_unit

    def __addition__(self, other):
        #res = self.__value +other.__value
        #return res
        if type(other) == int or type(other) == float:
            res = Devise(self.value + other, self.unit)
        else:
            res = Devise(self.value +other.value, self.unit)
            return res

    def __iadd__(self,other):
        self.__value = self + other
        return self.__value

    def __mul__(self,other):
        return self.__value*other.__value

    if __name__ == "__main__":
        m = Devise(12,"USD")
        print (m)