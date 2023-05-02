# If two strings/inputs are anagrams 

def is_anagram(x,y):
    x_lower,y_lower = x.lower(),y.lower()
    return sorted(x_lower) == sorted(y_lower)
  
 
  
  
