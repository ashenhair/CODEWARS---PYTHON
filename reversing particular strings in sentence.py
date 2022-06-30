def spin_words(sentence):
    split_sentence = sentence.split(" ")
    new_sentence = ""
    for i in split_sentence:
        if len(i) >= 5:
            new_sentence += (i[::-1])
        else:
            new_sentence += i
        if split_sentence.index(i) + 1 < len(split_sentence):
            new_sentence += " "
    return new_sentence

print(spin_words("Hey fellow warriors "))
