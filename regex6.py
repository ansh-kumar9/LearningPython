# WAP to search the details that start with The, end with Spain

import re

txt = "The rain in Spain"

x = re.search("^The.*Spain$", txt)

print(x)