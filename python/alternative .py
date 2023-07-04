phrase= 'hello world'
#use a loop code to do upper and lower phrase
mixed_phrase = ''

for i in range (len(phrase)):
    if not i%2:
        mixed_phrase = mixed_phrase + phrase[i].upper()
    else :
        mixed_phrase =mixed_phrase +phrase[i].lower()

print(f' The mixed cased phrase is : {mixed_phrase}')




sen = ' i am learning to code'

#for every alternative cased word first split then loop
words= sen.split()

mixed_words = [word.lower() if i % 2 != 0 else word.upper() for i, word in enumerate(words)]

#now join the mixed cased word to make a sentence

result = " ".join(mixed_words)

print(f'The new sentence with mixed cased words is : {result}')

