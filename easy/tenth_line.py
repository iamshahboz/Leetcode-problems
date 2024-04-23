# with open('my_file', 'r') as reader:
#     lines = reader.readlines()[9]
#     print(lines)
'''
sed -n '10p' < 'file.txt'

-n option suppresses automatic printing of pattern space.
'10p' is a sed command where p is a command that prints the current pattern space (line) and 10 specifies that it should be applied to the 10th line.
< file.txt is input redirection, meaning it takes the content of file.txt as input for sed.

'''
