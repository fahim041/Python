def square_numbers(nums):
    for i in nums:
        yield i * i


sq_nums = square_numbers([2, 3, 4, 5])
for num in sq_nums:
    print(num)
