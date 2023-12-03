"""The client has an ip address of 192.168.1.200
10.3.45.25

172.15.65.0"""

"""The client has an ip address of #.#.#.#
#.#.#.#

#.#.#.#"""

#.#.#.#

import re

def convert_ip(s:str):

    return re.sub('(\d{1,3}\.){3}\d{1,3}', '#.#.#.#', s)



s = """The client has an ip address of 192.168.1.200
10.3.45.25

172.15.65.0"""
print(convert_ip(s))
