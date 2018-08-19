def master_yoda(words):
    wordlist = words.split()
    reverse_word_list = wordlist[::-1]
    print ' '.join(reverse_word_list)

master_yoda('I am home')
