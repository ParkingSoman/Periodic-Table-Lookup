import decimal


class LookupTable:

    def __init__(self, periodic_table):
        self.periodic_table = periodic_table

    # Find all other info by name
    def group_name(self, name):
        for element in self.periodic_table:
            if self.periodic_table[element]['name'] == name:
                return self.info(element)

        return ["None", "None", -1, -1]

    # Find all other info by symbol
    def group_symbol(self, symbol):
        for element in self.periodic_table:
            if self.periodic_table[element]['symbol'] == symbol:
                return self.info(element)

        return ["None", "None", -1, -1]

    # Find all other info by atomic number
    def group_number(self, number):
        for element in self.periodic_table:
            if self.periodic_table[element]['number'] == number:
                return self.info(element)

        return ["None", "None", -1, -1]

    # Find all other info by atomic mass
    def group_mass(self, mass):
        compare = decimal.Decimal(str(mass)).as_tuple().exponent
        compare = abs(compare)

        for element in self.periodic_table:
            if (round(self.periodic_table[element]['atomic_mass'], compare)) == mass:
                return self.info(element)

        return ["None", "None", -1, -1]

    def info(self, element):
        return [self.periodic_table[element]['name'], self.periodic_table[element]['symbol'],
                self.periodic_table[element]['number'], self.periodic_table[element]['atomic_mass'],
                self.periodic_table[element]['category'], self.periodic_table[element]['period'],
                self.periodic_table[element]['xpos'], self.periodic_table[element]['shells']]

    @staticmethod
    # Prints all info from list
    def print_info(element):
        if element == ["None", "None", -1, -1]:
            print("Does not exist")
            return

        print("Name: " + element[0])
        print("Symbol: " + element[1])
        print("Atomic Number: " + str(element[2]))
        print("Atomic Mass: " + str(element[3]))
        print("Neutrons: " + str(int(round(element[3], 0) - element[2])))
        print("Period: " + str(element[5]))
        print("Group: " + str(element[6]))
        print("Category: " + element[4])
        print()
        print()

        for i in range(len(element[7])):
            print("Shell " + str(i + 1) + ": " + str(element[7][i]))
