"""
Task:
    Compress the code from regex.py into just two lines. Here is a redacted 
    version as a hint....

    import re
    print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )
"""

import re
print( sum( [ int(x) for x in re.findall('[0-9]+',open("regex_sum_1628192.txt").read()) ] ) )
                                                  