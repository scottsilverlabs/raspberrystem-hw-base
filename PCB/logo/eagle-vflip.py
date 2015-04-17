from bs4 import BeautifulSoup
import sys

try:
    prog, name = sys.argv
except:
    print "Usage: eagle-vflip.py <file> <scale_factor> "
    sys.exit()

with file(name) as f:
    soup = BeautifulSoup(f)

for tag in soup.plain.find_all(["vertex", "polygon", "wire"]):
    for attr in ["y", "y1", "y2", "curve"]:
        if attr in tag.attrs:
            tag[attr] = float(tag[attr]) * -1

with file(name, "w") as f:
    f.write(str(soup))

