def adjacency_list_to_matrix(dictionary):
    #counting number of items in dictionary
    n = len(dictionary)

    #intializing matrix with zeros

    matrix = [[0 for _ in range(n)] for _ in range(n)]

    #replacing edges with 1
    for key,value in dictionary.items():

        #accessing specific edges

        for i in range(len(value)):
            matrix[key][value[i]] = 1 #reassignment
        print(matrix[key])

    return matrix