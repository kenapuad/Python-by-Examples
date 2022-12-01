word = "banana"
x = word[0].lower()

if x =='a' or x =='e' or x =='i' or x =='o' or x =='u':
    new_word = (word+"way")
    print(new_word.lower())
else:
    new_word = (word[1:len(word)]+word[0] +"ay")
    print(new_word.lower())
