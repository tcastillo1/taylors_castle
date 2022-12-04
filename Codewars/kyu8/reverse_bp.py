# how does this make sense....
# i believe the arguemtns for indexing are star:stop:step
# we leave start and stop blank meaning we start at the 1st item and end at the last.
# step is -1 meaning we work backwards
# why dont we start at the first letter and work backwards from there?
# why is it not wdlro
def solution(string):
    print(string[::-1])


solution("world")
