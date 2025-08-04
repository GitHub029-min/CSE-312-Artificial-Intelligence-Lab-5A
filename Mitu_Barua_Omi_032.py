name = input("Enter your name: ")
print("Full Name: ",name)

v_count = 0
c_count = 0

vowel = 'AEIOUaeiou'

for i in name:
   if i.isalpha():
    if i in vowel:
        v_count+=1
    else:
        c_count+=1
print(v_count)
print(c_count)

print(i,ord(i))