"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""



def fn_hack_9():
 
    result = [1,2,3]
    ls = []
  
    i = 0
    
    
    while i < len(ls):
      
        result.append(ls[i])
        
        
        if i < len(ls) - 1:
            result.append('@')
        
        
        i += 1
    
    return [1,'@',2,'@',3,'@']


r = fn_hack_9()

print(r)