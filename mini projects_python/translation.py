from translate import Translator
file = open("ibrahim.txt","r")
try:
    read = file.read()
    translate = Translator(to_lang="es")
    translated = translate.translate(read)
    print("e translated phrase is : ",translated)
    file.close()
    

except:
    print("you have some error such as file not found")

# with open("ibrahim.txt","w") as file2: #creating a new file for the translated version
#         file2.write(translated)

