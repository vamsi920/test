# def solution(queryType, query):
# # query type = ["insert","insert", "addToKey", "addToValue", "get"]
# # query = [[1,2], [2,3], [2], [3], [1]]
#     d = {}
#     allGetQueries = 0

#     for i in range(len(query)):
#         if(queryType[i] == "insert"):
#             d[query[i][0]] = query[i][1]
#         elif(queryType[i] == "addToKey"):
#             d2 = {}
#             for key in d:
#                 d2[key+query[i][0]] = d[key]
#             d = d2
#         elif(queryType[i] == "addToValue"):
#             for key in d:
#                 d[key] += query[i][0]
#         elif(queryType[i] == "get"):
#             # print( d[query[i][0]])
#             allGetQueries += d[query[i][0]]
#     return allGetQueries
    
# def is_valid_sudoku_solution(grid):
#     # Check rows
#     for row in grid:
#         if set(row) != set(range(1, 10)):
#             return False
    
#     # Check columns
#     for col in zip(*grid):
#         if set(col) != set(range(1, 10)):
#             return False
    
#     # Check sub-grids
#     for i in range(0, 9, 3):
#         for j in range(0, 9, 3):
#             subgrid = [grid[r][c] for r in range(i, i+3) for c in range(j, j+3)]
#             if set(subgrid) != set(range(1, 10)):
#                 return False
    
#     return True
# def solution(queryType, query):
#     s1 = []
#     s2 = []
#     sum = 0
#     for i in range(len(queryType)):
#         if(queryType[i] == "insert"):
#             if(query[i][0] in s1):
#                 for j in range(len(s1)):
#                     if(s1[j] == query[i][0]):
#                         s2[j] = query[i][1]
#             else:
#                 s1.append(query[i][0])
#                 s2.append(query[i][1])
#             # s1.append(query[i][0])
#             # s2.append(query[i][1])
#         elif(queryType[i] == "addToKey"):
#             for j in range(len(s1)):
#                 s1[j] += query[i][0]
#         elif(queryType[i] == "addToValue"):
#             for j in range(len(s2)):
#                 s2[j] += query[i][0]
#         elif(queryType[i] == "get"):
#             for j in range(len(s1)):
#                 if(s1[j] == query[i][0]):
#                     sum += s2[j]

#     return sum


# queryType = ["insert","insert", "addToValue","addToKey", "get"]
# queryType = ["insert", "addToValue", "get", "insert", "addToKey", "addToValue", "get"]
# queryType = ["insert", "insert", "addToValue", "addToKey", "get"]
# query = [[1,2], [2,3], [2], [1], [3]]
# query = [[1,2], [2,3], [2], [1], [3]]
# query = [[1,2], [2], [1], [2,3], [1], [-1], [3]]
# print(solution(queryType, query))

