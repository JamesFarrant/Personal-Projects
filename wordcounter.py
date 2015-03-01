def count_words():
    count = 0
    sentence = input('Input a sentence! > ')
    new = sentence.split()

    for i in new:
        count += 1

    print('There are ' + str(count) + ' words in the sentence!')
    print('Your sentence was ' + '"' + sentence + '"')
count_words()

# i is unused but seems to still count the split words in new that add to the count.
