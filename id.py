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

max_len = max(len(("name:" +name)), len(("batch: "+batch)), (("hobies: " + lenght_check)), (("links: "+lenght_check_link)))

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
one_sideGap = math.floor((max_len - 2)/2)
print(" "*one_sideGap, end="")
print("ID CARD", end="")
print(" "*(one_sideGap+((max_len - 2)%2)), end="")
print("=")



#do the height




    