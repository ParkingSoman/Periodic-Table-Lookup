#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 09:56:11 2021
"""

import json
from Lookup import LookupTable

# Load periodic table info from file
table_path = "/Users/shonu/Downloads/periodic-table-lookup.json"
with open(table_path, 'r') as data:
    periodic_table = json.load(data)

table = LookupTable(periodic_table)

while True:
    # Enter value of fragmented info
    attribute = input("ENTER INFO: ")

    if attribute.lower() == 'quit':
        break

    print()
    print()

    try:
        # Incite error if there is one
        int(float(attribute))

        if "." not in attribute:
            attribute = int(attribute)
            table.print_info(table.group_number(attribute))

        else:
            attribute = float(attribute)
            table.print_info(table.group_mass(attribute))

    except ValueError:
        if len(attribute) <= 2:
            attribute = attribute.capitalize()
            table.print_info(table.group_symbol(attribute))

        else:
            attribute = attribute.capitalize()
            table.print_info(table.group_name(attribute))

    print("___________________________")
