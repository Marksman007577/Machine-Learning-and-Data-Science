# TASK: Create a numpy array called myarray which consists of 101 evenly linearly
# spaced points between 0 and 10.
import numpy as np

myarray = np.linspace(0, 10, 101)
print(myarray)

# TASK: Use numpy to check how many rolls were greater than 2.
# For example if dice_rolls=[1,2,3] then the answer is 1.
# NOTE: Many different ways to do this! Your final answer should be an integer.
dice_rolls = np.array([3, 1, 5, 2, 5, 1, 1, 5, 1, 4, 2, 1, 4, 5, 3, 4, 5, 2, 4, 2, 6, 6, 3, 6, 2, 3, 5, 6, 5])

total_rolls_over_two = dice_rolls[dice_rolls > 2]
num_arr = np.count_nonzero(total_rolls_over_two)
print(total_rolls_over_two)
print(num_arr)

# TASK: Use numpy to check the total remaining in the account after the series of transactions.
# NOTE: Many different ways to do this!
account_transactions = np.array([100,-200,300,-400,100,100,-230,450,500,2000])

account_total = account_transactions.sum()
print(account_total)