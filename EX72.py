subjects = ["Math","Science","GMRC","English","Filipino","History"]
print(subjects)
dislike = input("What is the subject you don't like in this list? ")
getrid = subjects.index(dislike)
del subjects[getrid]
print(subjects)