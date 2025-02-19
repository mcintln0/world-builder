#Functions for text conversions or manipulations

def effIt(non_f_str: str):
    return eval(f'f"""{non_f_str}"""')
    #Is a security concern but as the program is intended for local use only. By authors is included
    #Other option would be to automaticaly add f""" to the beginninng of the text area  
    
#Splitting text only    
def splitParagraphs(textBlock):
    textArrays = textFile.split('\n\n')
    for i in textArrays:
        i+= f'\n\n'
    return textArrays

#Splitting text and formatting to f-string    
def fsplitParagraphs(textBlock):
    textArrays = effIt(textFile).split('\n\n')
    for i in textArrays:
        i+= f'\n\n'
    return textArrays