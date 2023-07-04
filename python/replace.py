sentence = 'The!quick!brown!fox!jumps!over!the!lazy!dog!.'
# replace ! in sentence 
# #the blank quotes should have a space otherwise sentence omits and dont have space in between the words
print(sentence.replace('!',' '))
#store result of sentence.replace as a variable
cap_sentence= sentence.replace('!',' ')
#print cap sentence in upper case
print(cap_sentence.upper()) # results in cap sentence all in capitals
#find the length of sentence to work out index
print(len(cap_sentence))#index of cap_sentece is 0 to 44
#print cap_sentence in reverse by starting at 44 to 0 and reversing by -1
print(cap_sentence[44::-1])
#this prints 'god yzal eht revo spmuj xof nworb kciuq ehT

