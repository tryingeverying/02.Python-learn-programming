def printTable(tabledata):
    len_num_i=[]
    for i in tabledata:
        len_num=[]
        for j in i:
            len_num.append(len(j))
        len_num_i.append(max(len_num))
    for row_num in range(len(tabledata[0])):
        
        for list_num in range(len(tabledata)):
            
            temp_str=tabledata[list_num][row_num]
            print(temp_str.rjust(len_num_i[list_num]),end = " ")
        print(' ')


tableData=[['apple','orange','cherries','banana'],
            ['Alice','Bob','Carol','David'],
            ['dogs','cats','moose','goose']]
printTable(tableData)







# list_1=['apple','orange','cherries','banana']
# list_2=[]
# for i in list_1:
#     list_2.append(len(i))

# print(max(list_2))
