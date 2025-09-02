def even_odd(num):
    even = False
    if not (num == 0) and num % 2 == 0:
        return True
        
    else:
        return False
    
def get_avg(num_list:list):
    total = 0
    if isinstance(num_list, list):
        for i in num_list:
            total += i
            avg = total / len(num_list)
    return avg

def get_max(num_list):
    return max(num_list)

def get_min(num_list):
    return min(num_list)

