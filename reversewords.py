'''Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps" '''

def reverse_words(text):

  #go for it

    r = ""
    for word in text.split():
        r += "{} ".format(word[::-1])

    print(r)

reverse_words("This is an example!")
reverse_words("double  spaces")
