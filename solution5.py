# Write code for algorithm 5 below
#Write a function that checks whether a string is a palindrome or not. The program should take in a string and return True if the string is a palindrome and False if not.

def reverse(string):
    if string == string[::-1]:
        print('True')
    else:
        print('False')

reverse('racecar')
#prints true

reverse('pie')
#prints false