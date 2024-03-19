Problem Statement:
You are given a list of integers representing the prices of a stock on consecutive days. You need to find the maximum profit that can be obtained by buying and selling the stock, but you are only allowed to complete at most two transactions (buy and sell one share of the stock multiple times).
For example, given the prices [3, 3, 5, 0, 0, 3, 1, 4], the maximum profit that can be achieved is 6, which is obtained by buying on day 4 (price = 0) and selling on day 6 (price = 3), then buying again on day 7 (price = 1) and selling on day 8 (price = 4).
Question:
Write a Python function to solve the problem efficiently. Your function should take a list of integers representing the stock prices as input and return the maximum profit achievable with at most two transactions.
def max_profit_two_transactions(prices):
  """
  This function finds the maximum profit achievable with at most two transactions.

  Args:
      prices: A list of integers representing stock prices on consecutive days.

  Returns:
      The maximum profit achievable.
  """
  first_buy = float('inf')
  first_profit = 0
  second_profit = 0
  
  for price in prices:
    first_buy = min(first_buy, price)
    first_profit = max(first_profit, price - first_buy)
    second_profit = max(second_profit, price - first_buy + first_profit)
  
  return second_profit

Can you use the DP approach ?

def max_profit_two_transactions(prices):
  """
  This function finds the maximum profit achievable with at most two transactions.

  Args:
      prices: A list of integers representing stock prices on consecutive days.

  Returns:
      The maximum profit achievable.
  """
  n = len(prices)
  # Initialize two arrays to store maximum profit for one and two transactions
  # ending on each day
  dp_one = [0] * n
  dp_two = [0] * n

  # Find the maximum profit possible by making at most one transaction ending on 
  # each day (buy before current day and sell on current day)
  min_price = float('inf')
  for i in range(n):
    min_price = min(min_price, prices[i])
    dp_one[i] = max(dp_one[i-1], prices[i] - min_price)

  # Reset minimum price for second transaction
  max_price = float('-inf')
  for i in range(n - 1, -1, -1):
    max_price = max(max_price, prices[i])
    # Find the maximum profit possible by making two transactions (considering profit
    # from previous transaction) ending on current day (sell on current day)
    dp_two[i] = max(dp_two[i-1], dp_one[i] + max_price - prices[i])

  return max(dp_two)

Explanation:
The function takes a list of prices as input.
It initializes two arrays dp_one and dp_two of size n to store the maximum profit achievable with at most one and two transactions, respectively, ending on each day.
We iterate through the prices to find the maximum profit possible by making at most one transaction. We keep track of the minimum price seen so far (min_price) and calculate the profit for each day as the difference between the current price and the minimum price encountered before. This is stored in dp_one.
We then iterate through the prices in reverse order to find the maximum profit possible by making two transactions. We keep track of the maximum price seen so far (max_price) and calculate the profit for each day by considering the profit from the previous transaction (stored in dp_one) and adding the difference between the maximum price encountered after the previous transaction and the current price. This is stored in dp_two.
Finally, the function returns the maximum value from dp_two, which represents the maximum profit achievable with at most two transactions.
This approach utilizes dynamic programming to efficiently solve the problem in O(n) time complexity and O(n) space complexity.
 Write 5 test cases

Sure, here are 5 test cases for the max_profit_two_transactions function using dynamic programming:
Test Case 1:
Python
prices = [3, 3, 5, 0, 0, 3, 1, 4]
expected_profit = 6

profit = max_profit_two_transactions(prices)
assert profit == expected_profit, f"Test failed. Expected profit: {expected_profit}, Actual profit: {profit}"

print(f"Test Case 1: Maximum profit with at most two transactions - {profit}")


Explanation:
Buy on day 4 (price = 0) and sell on day 6 (price = 3) for a profit of 3.
Buy again on day 7 (price = 1) and sell on day 8 (price = 4) for a profit of 3.
Total profit = 3 + 3 = 6.
Test Case 2:
Python
prices = [1, 2, 3, 4, 5]
expected_profit = 4

profit = max_profit_two_transactions(prices)
assert profit == expected_profit, f"Test failed. Expected profit: {expected_profit}, Actual profit: {profit}"

print(f"Test Case 2: Maximum profit with at most two transactions - {profit}")


Explanation:
Buy on day 1 (price = 1) and sell on day 5 (price = 5) for a profit of 4.
No need for a second transaction as the price keeps increasing.
Test Case 3:
Python
prices = [7, 6, 4, 3, 1]
expected_profit = 0

profit = max_profit_two_transactions(prices)
assert profit == expected_profit, f"Test failed. Expected profit: {expected_profit}, Actual profit: {profit}"

print(f"Test Case 3: Maximum profit with at most two transactions - {profit}")


Explanation:
Since the price keeps decreasing, no profitable transactions are possible.
Test Case 4:
Python
prices = [1]
expected_profit = 0

profit = max_profit_two_transactions(prices)
assert profit == expected_profit, f"Test failed. Expected profit: {expected_profit}, Actual profit: {profit}"

print(f"Test Case 4: Maximum profit with at most two transactions - {profit}")


Explanation:
Only one price is given, so no transactions are possible.
Test Case 5:
Python
prices = [1, 2, 4, 7, 5, 3, 1]
expected_profit = 6

profit = max_profit_two_transactions(prices)
assert profit == expected_profit, f"Test failed. Expected profit: {expected_profit}, Actual profit: {profit}"

print(f"Test Case 5: Maximum profit with at most two transactions - {profit}")


Explanation:
Buy on day 1 (price = 1) and sell on day 4 (price = 7) for a profit of 6.
No need for a second transaction as a higher profit has already been achieved.
These test cases cover various scenarios, including increasing, decreasing, and mixed price trends, with single or multiple profitable transactions. They validate the correctness of the max_profit_two_transactions function using dynamic programming.
