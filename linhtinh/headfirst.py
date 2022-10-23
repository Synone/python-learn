scores = {}
result = open("result.txt")
for line in result:
    (name,score) = line.split()
    scores[score] = name #scores là dict, scores[keys] = name => vậy name là value của keys, score là string
print(scores)
result.close()
print("The top score were: ")
print(scores.keys()) # lấy keys
for each_score in sorted(scores.keys(),reverse = True): # dùng sorted cho hash
    print("Surfer " + scores[each_score] +" scored "+ each_score) # scores[each_score]: lấy value, each_score là key

print(sorted(scores.keys(),reverse = True))
# sort xong reverse, need highest to lowest
#vì sort sẽ sort từ thấp đến cao, reverse đảo list
print(scores["8.65"])






