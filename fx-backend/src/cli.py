#!/usr/bin/env python3
from project import Project

p = Project()
p.parse()

print("Send commands")

while True:
    command = input("$ ")
    splitted = command.split(' ')
    if splitted[0] == "show" and splitted[1] == "data":
        print(p.generate_json())
    if splitted[0] == "update":
        print(p.update_expression((int(splitted[1]), int(splitted[2])), splitted[3], " ".join(splitted[4:])))
