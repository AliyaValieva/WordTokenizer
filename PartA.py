import argparse
from collections import defaultdict

def tokenize(txtfile:str):
    ''' The below evaluation is based on ICS 33's content material(from Professor Pattis notes).
    Based on each analyzed time complexity, we perform the following algebraic procedures:
    O(N) + O(N)*O(1) + O(N) * O(1) + O(1) + O(1) + O(N) * O(1)+O(1) + O(N^3)+O(N)+O(1)  =
    O(N) + O(N) + O(N) + O(1) + O(1) + O(N) + O(1) + O(N^3) + O(N) =
    since we always drop the lower complexity added term result is O(N^3)
    As the input size grows, its time to execute triples; according to ICS 33 notes.
    '''
    listoftokens = [] # O(N) list creation
    for line in open(txtfile,'r'): #O(N) for loop
        line = line.lower().rstrip().split(" ") # O(1) because of reassignment

        for l in line: # O(N)
            if l.isalnum(): # O(1)
                listoftokens.append(l) # O(1)
            else:
                new = "" # O(1) since binding a value to any is O(1)
                for c in l: # O(N)
                    new += ' ' if c in "!@#$%^&*(){}[]:';,./\<>?~`-+=|" or c.startswith('"') else c # O(1)
                listoftokens.append(new) # O(1)

    # there are three for loops: O(N^3) + O(N) (split method creating list) + O(1) because of isalpha method
    return [n1 for n in [l.split(" ") for l in listoftokens] for n1 in n if n1.isalpha()]

def computeWordFrequencies(lst):
    ''' The below evaluation is based on ICS 33's content material(from Professor Pattis notes).
    Based on each analyzed time complexity, we perform the following algebraic procedures:
    O(len(...))+ O(N)*O(1)+O(NLogN)*O(1)+O(1) = O(N) based on priority of class complexities.
    Hence, for large sizes the algorithm will run faster and time grows linearly to the size input.
    '''
    fd = defaultdict(int) # O(len(...))
    for l in lst: # It's a loop -  O(N)
        fd[l] += 1 # O(1)
    for k,v in sorted(fd.items(), key=(lambda x: -x[1])): # here sorted is O(NLogN)+O(N) = O(N)
        print(k + "\t", v) #O(1)
    return k,v # O(1)

if __name__== '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file", nargs='*')
    computeWordFrequencies(tokenize(parser.parse_args().file[0]))





