import string
import math

hobie_list, link_list = [],[]
hobies, links = "",""

name = input("Name: ")
batch = input("Batch: ")

while True:
    hobies = input("Hobies: ")
    if hobies == "q":
        break
    hobie_list.append(hobies)


while True:
    links = input("Links: ")
    if links == "q":
        break
    link_list.append(links)

print(hobie_list)
print(link_list)

#find the longest sentance 
lenght_check = 0
lenght = 0
for hobie in hobie_list:
    lenght = len(hobie)
    if lenght > lenght_check:
        lenght_check = lenght

lenght_check_link = 0
link_lenght = 0
for link in link_list:
    link_lenght = len(link)
    if link_lenght > link_lenght:
        lenght_check_link = link_lenght

max_len = max(len(name), len(batch), lenght_check, lenght_check_link)

print(max_len)

#find check if hobies sentance exeeds the longest sentance then \n
hobie_len = 0
for hobie in hobie_list:
    hobie_len += len(hobie)
hobie_len += len(hobie_list)-1

#print the width of the id 

print("/"*int(max_len + 8))
print("=", end="") 

#ascci id
one_sideGap = math.floor((max_len + 6 - len(name))/2)
print(" "*one_sideGap, end="")
print("ID CARD", end="")
print(" "*(one_sideGap+((max_len + 6 -len(name))%2)), end="")
print("=")

print("=", end="")
print(" "*(max_len +6),end="")
print("=")

one_sideGap = math.floor((max_len + 6 - len(name))/2)
print("=", end="")
print(" "*one_sideGap, end="")
print(name, end="")
print(" "*(one_sideGap+((max_len + 6 -len(name))%2)), end="")
print("=")

one_sideGap = math.floor((max_len + 6 - len(name))/2)
print("=", end="")
print(" "*one_sideGap, end="")
print(batch, end="")
print(" "*(one_sideGap+((max_len + 6 -len(name))%2)), end="")
print("=")

leng = 0

for index, hobie in enumerate(hobie_list):
    one_sideGap = math.floor((max_len + 6 - len(name))/2)
    leng += len(hobie)+1

    if leng >= max_len:
        print("")
        
    print("=", end="")
    print(" "*one_sideGap, end="")
    print(hobie, end="")
    print(", ",end="")
    print(" "*(one_sideGap+((max_len + 6 -len(name))%2)), end="")
    print("=")

    if len(hobie_list) - 1 == index:
        break
#do the height
#"ID card" max length thing



    