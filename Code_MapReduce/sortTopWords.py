def read(input,topten):
    inp = open(input, "r");
    for line in inp.readlines():
        line = line.split()
        word = line[0]
        word = word[0:len(word)]
        value = int(line[1])
        result = (word,value)
	topten.append(result)
    inp.close()
		


topten = []
read("NewsSocialMedia.txt",topten)
out = open("TopNewsSocialMedia.txt", "w");
final = sorted(topten,key=lambda a:a[1])
final.reverse()
i = 0
for term in final:
	print(term)
        out.write(str(term))
        out.write("\n")
        i+=1
        if (i ==31):
	   break
out.close()