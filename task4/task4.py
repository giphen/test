import sys

def min_moves(numbers_file):

    with open(numbers_file, 'r') as file:
        nums = [int(line.strip()) for line in file if line.strip()]
    
    
    nums.sort()
    median = nums[len(nums)//2] 
    return sum(abs(num - median) for num in nums)

if __name__ == "__main__":

    moves = min_moves(sys.argv[1])
    print(moves)

# Для использования: python task4.py numbers.txt