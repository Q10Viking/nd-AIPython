import useful_functions as uf
scores = [88, 92, 79, 93, 85]

mean = uf.mean(scores)
curved = uf.add_five(scores)
mean_c = uf.mean(curved)

print("Scores: ",scores)
print("Original Mean: ",mean,"New Mean: ",mean_c)

print(__name__)
print(uf.__name__)

'''
Scores:  [88, 92, 79, 93, 85]
Original Mean:  87.4 New Mean:  92.4
__main__
useful_functions
'''