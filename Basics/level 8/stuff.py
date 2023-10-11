# Write Number in Expanded Form
# You will be given a number and you will need to return it as a string in Expanded Form. For example:

# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'
# NOTE: All numbers will be whole numbers greater than 0.

def expanded_form(num):
    num = str(num) # you cant iterate over int, this converts to string which is iterable
    st = ''  # create an empty string to append later on
    for index, n in enumerate(num):  # enumrate assigns index to each item 'n' in the string num.
        if n != "0":
# append st with +=. space + {'n'}=n aka no 0 integer. from num {len(num[index+1:])*"0"}=number of 0s need to append
            st += " + {}{}".format(n, len(num[index+1:])*"0")  # .format allows to format using {}
    return st.strip(" +")