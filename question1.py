def is_balanced(expression):
    pile = list()
    #map closing brackets to opening brackets in a dict
    char_dict = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in char_dict.keys():
            #check whether the corresponding bracket is at the top of the pile
            if not pile or pile.pop() != char_dict[char]:
                # falsy if pile is empty or its last character matches the value in the dict
                return False
        
        elif char in char_dict.values():
            #add character to pile
            pile.append(char)
        
        else:
            # skip other characters that are not in char_dict
            pass      
    return not pile
#Test case
print(is_balanced("({}[])")) #expected output >>> True