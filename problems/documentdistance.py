import math, sys

def read_file(filename):
    try:
        f = open(filename, 'r')
        return f.readlines()
    except IOError:
        print ("Error opening or reading input file: ",filename)
        sys.exit()
        
def word_frequencies_for_file(filename):
    line_list = read_file(filename)
    word_list = get_words_from_line_list(line_list)
    freq_mapping = count_frequency(word_list)
    merge_sort(freq_mapping) # Getting Different Distance with Insertion Sort
    return freq_mapping

def get_words_from_line_list(L):
    word_list = []
    for line in L:
        words_in_line = get_words_from_string(line)
        word_list.extend(words_in_line)
    return word_list

def get_words_from_string(line):
    word_list = []
    character_list = []
    for c in line:
        if c.isalnum():
            character_list.append(c)
        elif len(character_list) > 0:
            word = "".join(character_list)
            word = word.lower()
            word_list.append(word)
            character_list = []
    if len(character_list) > 0:
        word = "".join(character_list)
        word = word.lower()
        word_list.append(word)
    return word_list

# def count_frequency(word_list):
#     L = []
#     for new_word in word_list:
#         for entry in L:
#             if new_word == entry[0]:
#                 entry[1] = entry[1] + 1
#                 break
#         else:
#             L.append([new_word, 1])
#     return L

def count_frequency(word_list):
    D = {}
    for new_word in word_list:
        if new_word in D:
            D[new_word] += 1
        else:
            D[new_word] = 1
    W = []
    for key, value in D.items():
        temp = [key,value]
        W.append(temp)
    return W

def insertionsort(A):
    for i in range(len(A)):
        key = A[i]
        j = i - 1
        while j > -1 and A[j] > key:
            A[j+1] = A[j]
            j = j - 1
        A[j + 1] = key
    return A

def merge_sort(A):
    if len(A) == 1:
        return A
    elif len(A) == 2:
        if A[0] > A[1]:
            return [A[1], A[0]]
        else:
            return A

    p = len(A)//2
    m1 = merge_sort(A[:p])
    m2 = merge_sort(A[p:])

    ret = []

    while 1:
        if len(m1) > 0 and len(m2) > 0:
            if m1[0] <= m2[0]:
                ret.append(m1[0])
                m1 = m1[1:]
            else:
                ret.append(m2[0])
                m2 = m2[1:]
        elif len(m1) > 0:
            ret += m1
            m1 = []
        elif len(m2) > 0:
            ret += m2
            m2 = []
        else:
            break
    return ret


def vector_angle(L1, L2):
    numerator = inner_product(L1, L2)
    denominator = math.sqrt(inner_product(L1, L1) * inner_product(L2, L2))
    return math.acos(numerator / denominator)

def inner_product(L1, L2):
    sum = 0.0
    i = 0
    j = 0

    while i < len(L1) and j < len(L2):
        if L1[i][0] == L2[j][0]:
            sum += L1[i][1] * L2[j][1]
            i += 1
            j += 1
        elif L1[i][0] < L2[j][0]:
            i += 1
        else:
            j += 1
    return sum

def main():
    if len(sys.argv) != 3:
        print("Usage: documentdistance.py filename_1 filename_2")
    else:
        filename_1 = sys.argv[1]
        filename_2 = sys.argv[2]
        sorted_word_list_1 = word_frequencies_for_file(filename_1)
        sorted_word_list_2 = word_frequencies_for_file(filename_2)
        distance = vector_angle(sorted_word_list_1, sorted_word_list_2)
        print("The distance between the documents is: %0.6f (radians)" %distance)

if __name__ == "__main__":        
    import profile
    profile.run("main()")
    # main()