for row in range(6):
    for column in range(12):
        if (column ==0 or column==4 or column == 6 or column==10) and row !=0:
            print("*", end =' ')
        elif (column == 1 or column == 2 or column == 3 or column == 7 or column == 8 or column == 9) and (row == 0 or row == 3):
            print("*", end =' ')


        else:
            print(end= '  ')
    print()
