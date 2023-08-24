# writing with a
fileEdit=open("Words.txt", "a")
fileEdit.write("temp of hello")
fileEdit.close()
#reading and printing what happened with "a"
fileEdit=open("Words.txt",'r')
List=[""]
for read in fileEdit:
    List.append(read)

print(List)
#writing with # w
fileEdit=open("Words.txt", "w")
fileEdit.write("temp of hello")
fileEdit.close()
#reading and printing what happened with "w"
fileEdit=open("Words.txt",'r')
List=[""]
for read in fileEdit:

    List=list(read)

print(List)
# they both write but "a" adds the word to the end of the file while "w" deletes everything and adds itself
