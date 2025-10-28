# Your code here
# Read the input ratings as integers
a, b, c, d = map(int, input().split())

# Dictionary to map ratings back to user names
ratings = {
    a: "Anubhav",
    b: "Anuj",
    c: "Gaurav",
    d: "Ramandeep"
}

# Find the highest rating manually (without max)
highest = a
if b > highest:
    highest = b
if c > highest:
    highest = c
if d > highest:
    highest = d

# Find the second highest rating manually
second_highest = None

# Initialize second_highest with a value less than any rating
# since ratings are distinct and integers, pick the minimum of the four initially
lowest = a
if b < lowest:
    lowest = b
if c < lowest:
    lowest = c
if d < lowest:
    lowest = d

second_highest = lowest

for rating in [a, b, c, d]:
    if rating != highest and rating > second_highest:
        second_highest = rating

# Print the name corresponding to second highest rating
print(ratings[second_highest])
