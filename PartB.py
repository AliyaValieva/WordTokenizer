import argparse

def tokenize(txtfile:str):
    ''' The below evaluation is based on ICS 33's content material(from Professor Pattis notes).
        Based on each analyzed time complexity, we perform the following algebraic procedures:
        O(N) + O(N)*O(1) + O(N) * O(1) + O(1) + O(1) + O(N) * O(1)+O(1) + O(N^3)+O(N)+O(1)  =
        O(N) + O(N^2) + O(N) + O(1) + O(1) + O(N) + O(1) + O(N^3) + O(N) =
        since we always drop the lower complexity added term result is O(N^3)
        As the input size grows, its time to execute triples; according to ICS 33 notes - the algorithm runs faster on
        smaller inputs as the complexity class is high
        '''
    listoftokens = []  # O(N) list creation
    for line in open(txtfile, 'r'):  # O(N) for loop
        line = line.lower().rstrip().split(" ")  # O(1) because of reassignment

        for l in line:  # O(N)
            if l.isalnum():  # O(1)
                listoftokens.append(l)  # O(1)
            else:
                new = ""  # O(1) since binding a value to any is O(1)
                for c in l:  # O(N)
                    new += ' ' if c in "!@#$%^&*(){}[]:';,./\<>?~`-+=|" or c.startswith('"') else c  # O(1)
                listoftokens.append(new)  # O(1)
    # there are three for loops: O(N^3) + O(N) (split method creating list) + O(1) because of isalpha method
    return [n1 for n in [l.split(" ") for l in listoftokens] for n1 in n if n1.isalpha()]
def tokenize2(txtfile2):
    '''This function is of same complexity as tokenize : O(N^3)'''
    return tokenize(txtfile2)

def compare(lst1,lst2):
    ''' The below evaluation is based on ICS 33's content material(from Professor Pattis notes).
    Based on each analyzed time complexity, we perform the following algebraic procedures:
    O(N) due to foor loop + O(len(lst1)) + O(len(lst2)) + O(len(created new list)) + O(1) counting len =
    dropping lower complexity terms we get O(N)
    As input grows bigger, time to execute the function is linear to the size of input.
    '''
    return len(list({k for k in lst1}.intersection(lst2)))



if __name__== '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file",nargs='*')
    file1lst = tokenize(parser.parse_args().file[0])
    file2lst = tokenize(parser.parse_args().file[1])
    print(compare(file1lst,file2lst))

