numbers = list(map(int, input("Enter numbers separated by space: ").split()))

smallest = min(numbers)
print("Smallest number is:", smallest)

sorted_nums = sorted(numbers)
second_greatest = sorted_nums[-2]
print("Second greatest number is:", second_greatest)

second_smallest = sorted_nums[1]
print("Second smallest number is:", second_smallest)
