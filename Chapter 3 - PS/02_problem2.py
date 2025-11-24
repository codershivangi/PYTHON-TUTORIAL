# program to fill a letter template given below with name and date.

letter = ''' Dear <|Name|>,
You are selected!
<|Date|> '''

print(letter.replace("<|Name|>","Shivangi").replace("<|Date|>","21 August 2050"))