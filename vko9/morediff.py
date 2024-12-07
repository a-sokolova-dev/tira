# no itertools, just backtracking
def create(n):
    def is_valid(current_list):
        if len(current_list) < 2:
            return True
        
        # check if last added element is not adjacent to previous
        return abs(current_list[-1] - current_list[-2]) > 1

    def backtrack(current_list):
        if len(current_list) == n:
            return current_list
        
        for num in range(1, n + 1):
            if num not in current_list:
                current_list.append(num)
                
                if is_valid(current_list):
                    result = backtrack(current_list)
                    if result:
                        return result
                
                # backtrack if doesn't work
                current_list.pop()
        return None

    if n == 1:
        return [1]
    
    return backtrack([])

if __name__ == "__main__":
    print(create(1)) # [1]
    print(create(2)) # None
    print(create(4)) # [2, 4, 1, 3]
    print(create(7)) # [1, 3, 5, 2, 6, 4, 7]