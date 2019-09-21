
f = open('a.txt','w')
f.write("moge\n")
f.write("page\n")
f.close()

f = open('a.txt','r')
txt = f.read()
print(txt)
f.close()


with open("a.txt",encoding="utf-8") as f2:
	print (f2.read())

with open("a.txt","a",encoding="utf-8") as f3:
	f3.write("hoge\n")

with open("a.txt",encoding="utf-8") as f4:
	print(f4.read())




