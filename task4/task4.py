import sys

def min_moves(numbers_file):

    with open(numbers_file, 'r') as file:
        nums = [int(line.strip()) for line in file]
    
    
    nums.sort()
    median = nums[len(nums) // 2] 
    total_moves = 0
    for num in nums:
        if num > median:
            total_moves += num - median
        else:
            total_moves += median - num
    return total_moves

score = min_moves(sys.argv[1])
print(score)

# Для использования: python task4.py numbers.txt