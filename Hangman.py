print ('Welcome to Hangman \n Your favourite public hanging hanging game')
secret_phrase=open('secret_phrase.txt').read()

shown_phrase=[]
wrong=[]
tries=10
while tries>0:
    out=''
    for letter in secret_phrase:
        if letter in shown_phrase:
            out=out+letter
        else:
            out =out+' _ '
    if out==secret_phrase:
        print ('You got it !','The secret word is ', secret_phrase)
        break
    print ('Guess the right letter: ', out)

    guess=input()

    if guess in shown_phrase or guess in wrong:
        print ('You already said that dum dum', guess)
    elif guess in secret_phrase:
        print('Right Right Right!! ')
        shown_phrase.append(guess)
    else:
        print ('Wrong kiddo ! You have', tries-1, 'attempts left')
        tries=tries-1
        wrong.append(guess)
else:
    print('You lose booohooo')
    print('Time to hang sinner')
