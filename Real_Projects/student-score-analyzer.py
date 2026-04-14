def get_average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)


def get_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num


def get_min(numbers):
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num


def count_passed(numbers):
    count = 0
    for num in numbers:
        if num >= 50:
            count += 1
    return count


scores = input("Enter scores: ")
nums = scores.split()

numbers = []
for n in nums:
    try:
        numbers.append(int(n))
    except ValueError:
        print(f"Invalid input: {n}")


print(f"Average: {get_average(numbers):.2f}")
print(f"Maximum: {get_max(numbers)}")
print(f"Minimum: {get_min(numbers)}")
print(f"Passed: {count_passed(numbers)}")
