name = input("Name: ")
vowel = 'AEIOUaeiou'
v_count = 0
c_count = 0
rev=''
for i in name:
   if i.isalpha():
    if i in vowel:
        v_count+=1
    else:
        c_count+=1

print("Full Name:",name)
print("Vowels:",v_count)
print("Consonants:",c_count)
ascii_values = [ord(i) for i in name]
print(f"Ascii values: {ascii_values}")

print("Reversed Name:",name [::-1])

for i in name:
    rev = i + rev
if name == rev:
    print("Is Palindrome: True")
else:
    print("Is Palindrome: False")

name = name.replace(" ", '')
unique_letters = list(set(name))
unique_letters.sort()
print("Unique letters (sorted):", unique_letters)

for i in range(len(name)):
    if name.count(name[i]) == 1:
        print("First non-repeating character:", name[i])
        break
else:
    print("No non-repeating character found.")
