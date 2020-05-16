from collections import Counter 
  

dictionary = {'Steve' : [1, 4, 5, 6], 'Bat' : [1, 8, 9], 'Watson': [10, 22, 4], 'Sherlock': [5, 11, 22]} 
  

print("The original dictionary : " + str(dictionary)) 
  
cnt = Counter() 
for idx in dictionary.values(): 
    cnt.update(idx) 
res = {idx: [key for key in j if cnt[key] == 1]  
               for idx, j in dictionary.items()} 
   
print("Uncommon elements records : " + str(res))