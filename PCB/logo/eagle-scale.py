#
# Simple scaleable BRD file script.
#
# Reads in Eagle BRD file given as arg, and scales attributes in the <plain> section by the given
# factor.  
#
# Original file is overwritten - beware!
#
# See also hflip/vflip scripts.
#
# Example:
#
#   cp Logo.brd new.brd && python eagle-scale.py new.brd 1.8 open new.brd 
#
# The above scales Logo.brd by 1.8x, and opens the scaled file in Eagle.  In
# Eagle, you can then:
#    - group the file, 
#    - copy the group (then hit ESC), 
#    - open the board file you want to paste it into, 
#    - use the paste command to paste it.
#
from bs4 import BeautifulSoup
import sys

try:
    prog, name, scale_factor = sys.argv
except:
    print "Usage: eagle-scale.py <file> <scale_factor> "
    sys.exit()

with file(name) as f:
    soup = BeautifulSoup(f)

for tag in soup.plain.find_all(["vertex", "polygon", "wire"]):
    for attr in ["width", "x", "y", "x1", "y1", "x2", "y2"]:
        if attr in tag.attrs:
            tag[attr] = float(tag[attr]) * float(scale_factor)

with file(name, "w") as f:
    f.write(str(soup))

