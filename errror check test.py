def errorCheck(varName, type, question, error):
    x=0
    while x == 0:
        try:
            varName=type(varName)
            #tries to convert the variable into an integer/float
            x=1
            #stops the loop
        except error:
            varName = input(question)
            #if it is unable to convert the users input it asks the question again
    return varName

