# "i in 'aeiou'" how is this read? we are stating at the outset that the condition for summing the element i
# is that the element must be a vowel?
def get_count(sentence):
    print(sum(i in "aeiou" for i in sentence))


get_count("testing")
