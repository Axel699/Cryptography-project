# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 09:34:23 2020

@author: Alex
"""

# In this part the functions that are used by the program are defined and 
# some variables that are used in the functions. For example the variable 
# accepted_letters is used below in the body of the find_words() function.
# Also here the modules that are used are imported.


import random

from colorama import Fore
from colorama import Style





accepted_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
small = "abcdefghijklmnopqrstuvwxyz"
capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 





def find_words(message):
    
    words=[]
    word=""
    i=0    
    while i < len(message):
        if message[i] in accepted_letters:
            word += message[i]
            i+=1
        elif message[i] not in " ":
            i += 1
        else:
            if word != "":
                words.append(word)
                word=""
                i += 1
            else:
                i+=1
                
    if message[i-1] != " ":
        words.append(word)
                
    return words




def break_code(text):
    
    for i in range(26):
        result = encryption(text , rotation_value = i)
        print(result)
        print("Are you happy with the encryption result?")
        flag = input("Type T for true or F for false: ")
        if flag == "T":
            break
        
    print("This is the result you desired.")
    print(result)



def file_exists(): 
    
    while True:
        try:
           
            
            file_name = input("Type here: ") + ".txt"
            my_file = open(file_name)
            my_file.close()
            
        except IOError:
            print("\nFile doesn't exist. Try again.")
            continue
        
        else:
            return file_name
        
        
def read_file():

    message = ""
    
    with open(file_name ,"r") as file:
        for line in file:
            message += line

    return message


def read_common_words():
    
    common_words = []
    
    with open("words.txt","r") as file:
        for line in file:
            common_words.append(line)
        
    return common_words





def integer_check1():
    
    userInput = 0
    while True:
      try:
         userInput = int(input("Choose a rotation value: "))       
      except ValueError:
         print("This field requires an integer number. Please insert one.")
         continue
      else:
         return   userInput







def roll():   
    return random.randint(1, 25)








rotation_value = 0       
def encryption(text , rotation_value = 0):
    
    result = ""
    for character in text:
        if character in capital:
            for i in range(26):
                if character ==  capital[i]:
                    temp = i
            result += capital[(temp + rotation_value)%26]
            
        else:
            result += character
        
    return result







def decryption(text):

    result = ""
    
    for character in text:
        if character in capital:
            for i in range(26):
                if character ==  capital[i]:
                    temp = i
            result += capital[(temp - rotation_value)%26]
                    
        else:
            result += character
                        
                    
    return result
    
        

def frequency_of_letters():
    
    letter_frequency = [0] * len(accepted_letters)
    
    for word in words:
        for i in range(len(word)):
            for j in range(len(accepted_letters)):
                if word[i] == accepted_letters[j]:
                    letter_frequency[j] += 1
    
    letters_with_frequencies = []
    for i in range(len(accepted_letters)):
        letters_with_frequencies.append((accepted_letters[i] , letter_frequency[i]))
        
    return letters_with_frequencies
    





#############################################################################################################################
#############################################################################################################################





                    


# Here the user must choose a cypher mode.

print("Would you like to encrypt or decrypt a message?")
print("Please type one of the coloured words depending on your prefered action.")
print(f"{Fore.CYAN}encrypt{Style.RESET_ALL} ,{Fore.CYAN} decrypt{Style.RESET_ALL} , {Fore.CYAN}auto-decrypt{Style.RESET_ALL}")
cypher_mode = input("Type here: ")


while cypher_mode not in {"encrypt" , "decrypt" , "auto-decrypt"}:
    print("Invalid input, please specify your action again.")
    cypher_mode = input("Type encrypt or decrypt to continue: ")



# Here the user chooses a message entry mode.

print("Please choose a message entry mode.")
print("You can give the message manually or the program can read it from a text file.")
print("Please type one of the coloured words depending on your prefered action.")
print(f"{Fore.CYAN}manual entry{Style.RESET_ALL} ,{Fore.CYAN} read from file{Style.RESET_ALL}")
entry_mode = input("Type here: ")

            
while entry_mode not in {"manual entry" , "read from file"}:
    print("Invalid input, please specify your action again.")
    entry_mode = input("Type manual entry or read from file to continue: ")
                    
if entry_mode == "manual entry":
    print("Please type the message you want to " , cypher_mode)
    message = input("Type here: ")
else:
    
      print("\nGive me the name of your file, please. Do not add a .txt")
      print("If for example your file name is test.txt, you type test")
      print("So just the name of your file, please.")
      print("The given file must be in the working directory for the program to work.")
     
      file_name = file_exists()
      message = read_file()
    

# Here the user chooses a rotation value in case the option auto-decrypt on
# the cypher mode was not chosen.    

if cypher_mode !=  "auto-decrypt":    
 
    print("Would you like to choose a specific rotation value , or a random generated one?")    
    print(f"Type {Fore.CYAN}specific{Style.RESET_ALL} or {Fore.CYAN}random{Style.RESET_ALL} ")
    type_of_rotation = input("Type here: ")
    
    
    while type_of_rotation not in {"specific" , "random"}:
        print("Invalid input, please specify your action again.")
        type_of_rotation = input("Type specific or random to continue: ")


    
    if type_of_rotation == "specific":
        rotation_value = integer_check1()
    elif type_of_rotation == "random":
        rotation_value = roll()
    else:
        pass



capitalized_message = ""
    
for i in range(len(message)):
        if message[i] in small:
            for j in range(len(small)):
                if message[i] == small[j]:
                    capitalized_message += capital[j]
        else:
            capitalized_message += message[i]   


if cypher_mode == "encrypt":
    new_message = encryption(capitalized_message , rotation_value = rotation_value)
    print("The encrypted message is: ")
    print(new_message)
elif cypher_mode == "decrypt":
    new_message = decryption(capitalized_message)
    print("The decrypted message is: ")
    print(new_message)
else:
    common_words = read_common_words()
    break_code(capitalized_message)
    



input("Press enter to continue.")
print()    




#############################################################################################################################
#############################################################################################################################














    
# From here it starts the part of the statistics on the original message.

# Here all the words in the message are found according to the definition
# of Part 2.

words = find_words(message)    
 


# To find the total number of words in the message we just have to count the 
# number of elements in the total_number_of_words list, with the len() function
# that operates on lists.

total_number_of_words = len(words)



# Now in order to find the number of unique words in the message we can change
# the type of our data structure from a list to a set. We know that each element 
# of a set only appears once and with the len() function again we can obtain the 
# number of unique words in the set.




unique_words_set = set(words)
number_of_unique_words = len(unique_words_set)

            





unique_words_list = list(unique_words_set)
counter_list = [0]*len(unique_words_list)





#We count the frequency of each unique word.
for i in range(len(unique_words_list)):
    for j in range(len(words)):
        if unique_words_list[i] == words[j]:
            counter_list[i] += 1



# Here a list of tuples is created, in every tuple the first element is a 
# unique word found in the original message and the second element is the 
# frequency of every word.

tuples_list = []


for i in range(len(unique_words_list)):
    tuples_list.append((unique_words_list[i],counter_list[i]))


sorted_tuples_list = sorted(tuples_list,  key=lambda word: word[1],reverse=True)



# Here we filter our list of tuples by the frequency of every word in the original
# message. The final_tupled_list is a list that contains at most 10 elements.

final_tupled_list = []

if len(sorted_tuples_list) <= 10:
    final_tupled_list = sorted_tuples_list
        
else:
    for i in range(10):
        final_tupled_list.append(sorted_tuples_list[i])












# Minimum and maximum word length.

max_word_length = len(unique_words_list[0])
max_word = unique_words_list[0]
min_word_length = len(unique_words_list[0])
min_word = unique_words_list[0]

for i in range(len(unique_words_list)):
    
    if max_word_length < len(unique_words_list[i]):
        max_word_length = len(unique_words_list[i])
        max_word = unique_words_list[i]
        
    if min_word_length > len(unique_words_list[i]):
        min_word_length = len(unique_words_list[i])
        min_word = unique_words_list[i]



# In this part the frequency of letters is calculated. The result is a list of tuples,
# each tuple contains the name of each letter and the frequency of it also inside the 
# message.


letters_with_frequencies = frequency_of_letters()


sorted_let_freq_list = sorted(letters_with_frequencies,  key=lambda letter: letter[1],reverse=True)

most_common_letter = sorted_let_freq_list[0][0]
most_common_letter_frequency = sorted_let_freq_list[0][1]






#############################################################################################################################
#############################################################################################################################

# In this part the message metrics are printed in the order that were given in Part 2.


print("This list contains all the words that are in the message: " , words)


input("Press enter to continue.")
print()   


print("The total numbers of words are: " , total_number_of_words)


print("The number of unique words are: " , number_of_unique_words)




print()
print("Below are printed the most common words in descending order.")
print("Each word appears with the frequency found in the message.")
print()




# This part of the code formats the common words in a more presentable way. First the maximum 
# length of all the words is found. Then the length of each word is subtracted from the maxim
# in order to find the number of spaces needed to format the : in a srtaight line!


max=0
for i in range(len(final_tupled_list)):
    if len(final_tupled_list[i][0]) > max:
        max = len(final_tupled_list[i][0])

for i in range(len(final_tupled_list)):
    print(final_tupled_list[i][0] , " " * (max - len(final_tupled_list[i][0])) , ": " ,final_tupled_list[i][1] )


print()
print("The minimum word length in the message is:" , min_word_length)
print("The maximum word length in the message is:" , max_word_length)




print()
print("The most common letter in the message and it's frequency is: ")
print(most_common_letter , ":" , most_common_letter_frequency)




























#############################################################################################################################
#############################################################################################################################

# In this part a txt file is created which contains all the metrics of the message.

# The txt file is saved in the working directory, the path is relative. To view your working
# directory simply type pwd.


  



metrics_dict = {
        "total number of words" : total_number_of_words,
        "number of unique words" : number_of_unique_words,
        "minimum word length" : min_word_length,
        "maximum word length" : max_word_length
        }


 



with open("metrics.txt","w") as file:

    for k,v in metrics_dict.items():
        file.write(k + ":  " + str(v) + "\n")

































