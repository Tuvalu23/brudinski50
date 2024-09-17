'''
Ben Rudinski
Topher's Lovers
SoftDev
K05: File Parsing
2024-09-17
time spent:
'''

import random

with open("krewes.txt", "r") as file: # open the krewes text file and read its contents
    content = file.read()
    
tuples = content.split("@@@") # create the tuples split with @@@

devos_list = []
for tup in tuples:
    parts = tup.split("$$$")
    if len.parts == 3:
        period, devo, ducky = tup.split("$$$")
        devos_list.append({'period': period, 'devo': devo, 'ducky': ducky})
        
random_devo = random.choice(devos_list)
print(f"Devo: {random_devo['devo']}, Period: {random_devo['period']}, Ducky: {random_devo['ducky']}")