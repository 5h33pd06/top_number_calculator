#!/usr/bin/python3

# File with data
filename = input("Enter the filename: ")

# Top amount of numbers to retrieve
top_num = int(input("Enter the top amount of numbers to display: "))

# Open the data file, split by double line breaks to create strings representing a group of numbers
with open(filename) as f:
	groups = f.read().strip().split('\n\n')

# Create empty lists to start with
group_nums = []
total_group_nums = []

# Sort in descending order based on total calorie count, return list of top elves
for i, group in enumerate(groups):
	nums = list(map(int, group.split()))
	num_sum = sum(nums)
	group_nums.append((i+1, num_sum))
top_nums = sorted(group_nums, key=lambda x: x[1], reverse=True)[:top_num]

# Print the top elves and the total calories between them
print(f"\nTop {top_num} numbers:")
for group_num, total_num in top_nums:
	print(f"Group {group_num} total {total_num}")
	total_group_nums.append(total_num)
print(f"\nTotal for these groups: {sum(total_group_nums)}")