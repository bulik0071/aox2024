import re
from icecream import ic

def getNumbers(str):
    array = re.findall(r'[0-9]+', str)
    return array

def find_distance(el1:int,el2:int):
    return abs(el1-el2)

def find_similarity_score(el:int,times_appeared:int):
    return el*times_appeared

right_list=[]
left_list=[]

test='puzzle_example.txt'
prod='puzzle_input.txt'

with open(file=prod) as f:
    for element in f:
        numbers=getNumbers(element)
        right_list.append(int(numbers[0]))
        left_list.append(int(numbers[1]))
right_list.sort()
left_list.sort()
p1=0
p2=0

for idx,el1 in enumerate(right_list):
    dist=find_distance(el1,left_list[idx])
    p1=p1+dist
    times_appeared=0
    for el2 in left_list:
        if el1==el2:
            times_appeared += 1
    p2=p2+find_similarity_score(el1,times_appeared)
    
ic(p1)
ic(p2)
    
    