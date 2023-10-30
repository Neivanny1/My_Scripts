#!/usr/bin/bash python3
with open('webstr.log', 'r') as file:
  word = 'word to search'
    for line in file:
        if word in line.lower():
            print(line)
