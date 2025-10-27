#Write a program to fill in a letter given below with name and date
letter = ''' Dear <|Name|>, 
You are Selected !
<|Date|> '''

print(letter.replace("<|Name|>","Harry").replace("<|Date|>", "28 spetemeber 2025"))