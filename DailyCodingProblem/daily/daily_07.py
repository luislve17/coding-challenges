"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded
message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it
could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For
example, '001' is not allowed.
"""
import string 

code_mapping = {
    str(letter_i+1): letter
    for letter_i, letter
    in enumerate(list(string.ascii_lowercase))
    }

def contains_out_of_bounds(list_of_str_integers):
    for coded_str in list_of_str_integers:
        if coded_str.isdigit() and int(coded_str) > 26:
            return True
    return False

def get_all_subsets(coded_msg:str):
    possible_messages = []
    for index_i in range(len(coded_msg)):
        for index_j in range(index_i+1, len(coded_msg)):
            pass_flag = False
            prefix_str = coded_msg[0:index_i]
            subset_str = coded_msg[index_i:index_j]
            sufix_str = coded_msg[index_j:]
            compiled_substr = [prefix_str,subset_str,sufix_str]
            
            if contains_out_of_bounds(compiled_substr): continue

            compiled_substr = [coded_str for coded_str in compiled_substr if coded_str]
            decrypted_str = ''.join([code_mapping.get(coded_str) for coded_str in compiled_substr])
            possible_messages.append(decrypted_str)

    return possible_messages

# Testing
print("-"*14, "\n", ".: Testing :.", "\n", "-"*14, sep='')
test_function = get_all_subsets

inputs = [
    {'coded_msg': '111'},
    {'coded_msg': '1234'}
]

for input_arg in inputs:
    print(f"in: {input_arg}\n|\n┖-> out: {test_function(**input_arg)}\n")

