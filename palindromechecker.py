def is_palindrome():
    word = input('Enter a word to be checked > ')
    if word == word[::-1]:
        print('Palindrome!')
    else:
        print('Not a palindrome!')
is_palindrome()
