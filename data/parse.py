import yaml
import numpy as np

with open("publications.yml", "r") as file:
    data = yaml.safe_load(file)

numPubs = len(data)

years = []
for iPub in range(numPubs):
    years.append(data[iPub]["year"])

sortYears = np.flip(np.argsort(years))



# read in header for publications.html file and begin writing out
with open("header.html", "r") as src, open("snippet.html", "w") as dst:
    dst.write(src.read())


# write a snippet of html that conveys this data 
fileOut = open("snippet.html", "a")
count = 0 
for iPub in sortYears:
    count += 1
    dataBuf = data[iPub]
    # start writing
    fileOut.write("<p>\n %s." % count)
    # first do authors 
    fileOut.write(" %s " % dataBuf["authors"]) 
    fileOut.write('"%s."' % dataBuf["title"])
    fileOut.write(' <i>%s</i>, ' % dataBuf["journal"])
    if "volume" in dataBuf:
        fileOut.write('<b>%s</b>, ' % dataBuf["volume"])
    if "number" in dataBuf:
        fileOut.write('%s ,' % dataBuf["number"])
    if "pages" in dataBuf:
        fileOut.write("%s ," % dataBuf["pages"])
    fileOut.write(" %s. " % dataBuf["year"])
    if "doi" in dataBuf:
        fileOut.write('<a href="%s">🔗 DOI</a>' % dataBuf["doi"])
    if "arxiv" in dataBuf:
        fileOut.write('<a href="%s">📄 arXiv</a>' % dataBuf["arxiv"])

    fileOut.write("\n</p>\n\n")

# add footer 
with open("footer.html", "r") as src:
    fileOut.write(src.read())

fileOut.close()

