#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 09:56:11 2021
"""

import json
import decimal

# Load periodic table info from file
table_path = "Put the directory of json file here"
with open(table_path, 'r') as data:
    periodic_table = json.load(data)
    
class LookupTable():
    def info(self, element):
        return [periodic_table[element]['name'], periodic_table[element]['symbol'], periodic_table[element]['number'], periodic_table[element]['atomic_mass'], periodic_table[element]['category]]
    
    # Find all other info by name
    def groupName(self, name):
        for element in periodic_table:
            if periodic_table[element]['name'] == name:
                return self.info(element)
        
        return ["None", "None", -1, -1]
    
    # Find all other info by symbol        
    def groupSymbol(self, symbol):
        for element in periodic_table:
            if periodic_table[element]['symbol'] == symbol:
                return self.info(element)
            
        return ["None", "None", -1, -1]
            
    # Find all other info by atomic number        
    def groupNumber(self, number):
        for element in periodic_table:
            if periodic_table[element]['number'] == number:
                return self.info(element)
            
        return ["None", "None", -1, -1]
    
    # Find all other info by atomic mass
    def groupMass(self, mass):
        compare = decimal.Decimal(str(mass)).as_tuple().exponent
        compare = abs(compare)
        
        for element in periodic_table:
            if (round(periodic_table[element]['atomic_mass'], compare)) == mass:
                return self.info(element)
            
        return ["None", "None", -1, -1]

# Prints all info from list
def printInfo(element):
    if element == ["None", "None", -1, -1]:
        print("Does not exist")
        return
        
    print("Name: " + element[0])
    print("Symbol: " + element[1])
    print("Atomic Number: " + str(element[2]))
    print("Atomic Mass: " + str(element[3]))
    print("Neutrons: " + str(int(round(element[3], 0) - element[2])))  
    print("Category: " + element[4])

table = LookupTable()

while True:    
    # Enter value of fragmented info
    attribute = input("ENTER INFO: ")
    
    if (attribute.lower() == 'quit'):
        break
        
    print()
    print()
    
    try:
        # Incite error if there is one
        int(float(attribute))
        
        if "." not in attribute:
            attribute = int(attribute)
            printInfo(table.groupNumber(attribute))
            
        else:
            attribute = float(attribute)
            printInfo(table.groupMass(attribute))
    
    except ValueError:
        if (len(attribute) <= 2):
            attribute = attribute.capitalize()
            printInfo(table.groupSymbol(attribute))
        
        else:
            attribute = attribute.capitalize()
            printInfo(table.groupName(attribute))
            
            
    print("___________________________")
