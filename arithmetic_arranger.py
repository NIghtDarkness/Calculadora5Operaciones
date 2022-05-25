def arithmetic_arranger(problems,solves=False):

    if len(problems) > 5:
        return "Error: Too many problems."

    else:
        arithmetic_array = ["","","",""]

        for i in problems:
            try:
                pieces = i.split()
                firstnum = int(pieces[0])
                operator = pieces[1]
                secondnum = int(pieces[2])
            except:
                return "Error: Numbers must only contain digits."

            line = ""
            space = ""
            space2 = ""

            if operator != "+" and operator != "-":
                return "Error: Operator must be '+' or '-'."
                break

            if len(pieces[0]) > 4 or len(pieces[2]) > 4:
                return "Error: Numbers cannot be more than four digits."
                break

            if problems.index(i) > 0:
                for x in range(4):
                    arithmetic_array[x] += "    "

            if operator == "+":
                output = str(firstnum + secondnum)
            elif operator == "-":
                output = str(firstnum - secondnum)
        

            if len(pieces[0]) > len(pieces[2]):
                dif = len(pieces[0]) - len(pieces[2])
                dif2 = len(pieces[0]) - len(output)

                for i in range(dif+1):
                    space = space + " "
                for i in range(len(pieces[0]) + 2):
                    line = line + "-"
                if dif2 > 0:
                    space2 = " "
                    for i in range(dif2):
                        space2 = space2 + " "
                elif dif2 < 0:
                    space2 = " "
                elif dif2 == 0:
                    space2 = "  "

                arithmetic_array[0] += "  " + pieces[0]
                arithmetic_array[1] += operator + space + pieces[2]
                arithmetic_array[2] += line
                arithmetic_array[3] += space2 + output

            elif len(pieces[0]) < len(pieces[2]):

                dif = len(pieces[2]) - len(pieces[0])
                dif2 = len(pieces[2]) - len(output)

                for i in range(dif+2):
                    space = space + " "
                for i in range(len(pieces[2]) + 2):
                    line = line + "-"
                if dif2 > 0:
                    space2 = " "
                    for i in range(dif2):
                        space2 = space2 + " "
                elif dif2 < 0:
                    space2 = " "
                elif dif2 == 0:
                    space2 = "  "

                arithmetic_array[0] += space + pieces[0]
                arithmetic_array[1] += operator + " " + pieces[2]
                arithmetic_array[2] += line
                arithmetic_array[3] += space2 + output

            else:
                
                dif = len(pieces[0]) - len(output)

                if dif > 0:
                    space = " "
                    for i in range(dif):
                        space = space + " "
                elif dif < 0:
                    space = " "
                elif dif == 0:
                    space = "  "

                for i in range(len(pieces[0]) + 2):
                    line = line + "-"

                arithmetic_array[0] += "  " + pieces[0]
                arithmetic_array[1] += operator + " " + pieces[2]
                arithmetic_array[2] += line
                arithmetic_array[3] += space + output

        if solves:
            solve = arithmetic_array[0] + "\n" + arithmetic_array[1] + "\n" + arithmetic_array[2] + "\n" + arithmetic_array[3]
        else:
            solve = arithmetic_array[0] + "\n" + arithmetic_array[1] + "\n" + arithmetic_array[2] 
    
    
        return solve