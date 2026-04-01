def add_binary(a, b):
    
    new_a = a[2:]
    new_b = b[2:]
    
    i = len(new_a) - 1
    j = len(new_b) - 1
    
    leftover = 0
    result = ""
    
    while i >= 0 or j >= 0 or leftover:
        
        total = leftover
        
        if i >= 0:
            total += int(new_a[i])
            i -= 1
        
        if j >= 0:
            total += int(new_b[j])
            j -= 1
        
        result = str(total % 2) + result
        leftover = total // 2
    
    result = result.lstrip('0')
    
    if result == "":
        result = "0"
    
    return "0b" + result