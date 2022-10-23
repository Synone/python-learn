result = open("result.txt")
scores = {} 
for line in result:
    (name,score) = line.split()
    scores[name] = score

for each_score in scores.keys():
    print('Surfer ' +each_score + ' scored ' + scores[each_score])


""" 
scores= {}
scores[8.45] = "Joseph"
scores[9.12] = 'Juan'
scores[7.21] = 'Zack'
scores[8.31] = "Aaron"
scores[8.05] = "Aideen"
scores[8.65] = "Johnny"
scores[7.81] = "Stacey"

for key in scores.keys():
    print(scores[key] + ' had a score of ' + str(key)) """