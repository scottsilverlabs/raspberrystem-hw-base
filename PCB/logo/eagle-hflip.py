from bs4 import BeautifulSoup
import sys

try:
    prog, name = sys.argv
except:
    print "Usage: eagle-hflip.py <file> <scale_factor> "
    sys.exit()

with file(name) as f:
    soup = BeautifulSoup(f)

for tag in soup.plain.find_all(["vertex", "polygon", "wire"]):
    for attr in ["x", "x1", "x2", "curve"]:
        if attr in tag.attrs:
            tag[attr] = float(tag[attr]) * -1

with file(name, "w") as f:
    f.write(str(soup))

