# Alice has some cards with 
# numbers written on them. 
# She arranges the cards in decreasing order, 
# and lays them out face down in a sequence on a table. 
# She challenges Bob to pick out the card containing a given number by turning over as few cards as possible.
# Write a function to help Bob locate the card.
# FOR INSTANCE:
# We need to write a program to find the position of a given number 
# in a list of numbers arranged in decreasing order.
# We also need to minimize the number of times we access elements from the list.
from os import environ
from jovian.pythondsa import evaluate_test_case
 
 
# use dictionary to test
# ** SOLUTION **
def locate_card(cards, query):
    # Create a variable position with the value 0
    position = 0
    print("cards: ", cards)
    print("query: ", query)
    # Set up a loop for repetition
    while position < len(cards):
        print("positions: ", position)
        # Check if element at the current position matche the query
        if cards[position] == query:
            # Answer found! Return and exit..
            return position
        # Increment the position
        position += 1
        # Number not found, return -1
        return -1

test = {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 1},'output': 3}
result = locate_card(test['input']['cards'],test['input']['query'])

def locate_card2(cards,query):
    lo,hi = 0, len(cards) - 1
    while lo <= hi:
        mid = (lo + hi) // 2

        mid_number = cards[mid]

        print("lo: ", lo, ", hi", hi,", mid:", mid, ", mid_number:", mid_number)
        if mid_number == query:
            return mid
        elif mid_number < query:
            hi = mid - 1
        elif mid_number > query:
            lo = mid + 1
    return -1


a = locate_card2(test['input']["cards"],test['input']["query"])
print(a)
