brown_fox = "The!quick!brown!fox!jumps!over!the!lazy!dog"
#35 characters 8 blank spaces in the sentece: important for indexing

brown_fox = brown_fox.replace("!", " ")
#Replaces "!" with a " " (blank space)
print(brown_fox) 

brown_fox = brown_fox.upper()
#Changes every character in the string (sentence) to uppercase
print(brown_fox) 

brown_fox = "The quick brown fox jumps over the lazy dog"
#THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
print(brown_fox[-3:] + " " + brown_fox[-8:-4] + " " + brown_fox[-12:-9] + " " + brown_fox[-17:-13] + " " + brown_fox[-23:-18] + " " + brown_fox[-27:-24] + " " + brown_fox[-33:-28] + " " + brown_fox[-39:-34] + " " + brown_fox[-43:-40])
#Through the use of backwards indexing I'am able to print the sentence backwards
