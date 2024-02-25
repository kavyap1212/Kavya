# 1. Counting the number of vowels in a string
str1 = "Guvi Geeks Network Private Limited"
count = 0
a, e, I, o, u = 0, 0,0,0,0
vowels = set("aeiouAEIOU")
for i in str1:
    if i in vowels:
        count = count+1
for i in range(len(str1)):
    if str1[i] == 'a' or str1[i] == 'A':
        a = a+1
    if str1[i] == 'e' or str1[i] == 'e':
        e = e+1
    if str1[i] == 'i' or str1[i] == 'I':
        I = I+1
    if str1[i] == 'o' or str1[i] == 'O':
        o = o+1
    if str1[i] == 'u' or str1[i] == 'U':
        u = u+1
print("In the given string with ", len(str1), "characters, there are ",count,"number of vowels")
print("There are ",a, "number of 'A's")
print("There are ",e, "number of 'E's")
print("There are ",I, "number of 'I's")
print("There are ",o, "number of 'O's")
print("There are ",u, "number of 'U's")

# 2. Printing 1-20 numbers in a pyramid form
n = 0
m = 6
#looping for creating number pyramid 
for i in range(0,m):
    #looping for spaces
    print(" "* (m-i), end=" ")
    #looping for numbers
    for j in range(0, i+1):
        # printing numbers
        print(n," ", end="")
        n = n+1
    print("\r")

#3. Take string input & remove all vowels
#taking the string input
print("Enter the string to get string without vowels:")
str2 = input()
str2_rm_vowels =""
vowels = set("aeiouAEIOU")
for i in range(0, len(str2)):
    if str2[i] not in vowels:
        str2_rm_vowels = str2_rm_vowels + str2[i]

print("\nAfter removing Vowels: ", str2_rm_vowels)

#4. Counting number of unique characters
#Tip: Using the set as it only outputs the unique charachters
print("Enter a string to count unique characters:")
str3 = input()
s = set(str3)
charcount = len(s)
print(charcount)

#5. Checking if palindrome or not 
print("Enter the string to check palindrome:")
str4 = input()
str_rev = reversed(str4)
if str4 == str_rev:
    print("Entered string is palindrome")
else:
    print("Entered string is not a palindrome")

#6. Taking two strings & giving longest common substring:
print("Enter first string:")
str5 = input()
print("Enter second string:")
str6 = input()
ans = 0
substr1 = []
substr2 = []
for i in range(len(str6)):
    for j in range(len(str5)):
        k = 0
        while ((i + k) < len(str6) and (j + k) < len(str5) and str6[i + k] == str5[j + k]):
            substr1.append(str5[k])
            k = k + 1
        ans = max(ans, k)
table = [[0 for _ in range(len(str5) + 1)] for _ in range(len(str6) + 1)]
for i in range(1, len(str6) + 1):
    for j in range(1, len(str5) + 1):
        if str6[i - 1] == str5[j - 1]:
            table[i][j] = table[i - 1][j - 1] + 1
        else:
            table[i][j] = max(table[i - 1][j], table[i][j - 1])      
print("length of a longest substring is: ",ans)
longest_common_substring = ""
i = len(str6)
j = len(str5)
while i > 0 and j > 0:
    if str6[i - 1] == str5[j - 1]:
        longest_common_substring = str6[i - 1] + longest_common_substring
        i -= 1
        j -= 1
    else:
        if table[i - 1][j] > table[i][j - 1]:
            i -= 1
        else:
            j -= 1

print("The longest common substring is:", longest_common_substring)

#7. Most frequent character in a string
print("Enter a string to find the most frequent character in a string:")
str7 = input()
from collections import Counter
more_freq = Counter(str7)

print(max(more_freq.most_common(1)))

print("Most frequent character, number of times: ",max(more_freq.most_common(1)))

# 8. Check if the given string is an anagram of other given string
print('Enter string 1: ')
string2 = input()
print('Enter string 2: ')
string3 = input()
if sorted(string2) == sorted(string3):
    print("Entered strings are anagrams")
else:
    print("Entered strings are NOT anagrams")

# 9.No.of words in given string
print('Enter a string to count no.of words: ')
string1 = input()
num_words = len(string1.split())
print("There are ",num_words," words in the given string")

