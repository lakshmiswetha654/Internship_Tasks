from solution import (
    frequency_count, character_frequency, non_repeating_character,
    is_anagram, first_repeating_character,zeros_shifting, second_highest,
    remove_duplicates, missing_value, add, near_zero,
    common_element,reverse, maximum_sum, add
)


print("Q1:", frequency_count("python is easy and python is powerful"))
print("Q1 additional:",frequency_count("hello hello world"))

print("Q2:", character_frequency("banana"))
print("Q2 additional:", character_frequency("apple"))

print("Q3:",non_repeating_character("swiss"))
print("Q3 additional:",non_repeating_character("aabb"))

print("Q4:", is_anagram("listen", "silent"))
print("Q4 additional:", is_anagram("hello", "world"))

print("Q5:", first_repeating_character("programming"))
print("Q5 additional:", first_repeating_character("abcde"))

print("Q6:",zeros_shifting([0, 3, 0, 1, 2, 0, 4]))
print("Q6 additional:",zeros_shifting([1, 0, 2]))

print("Q7:", second_highest([10, 20, 40, 30, 40, 20]))
print("Q7 additional:", second_highest([5, 5, 5]))

print("Q8:", remove_duplicates([4, 2, 4, 5, 2, 7, 5]))
print("Q8 additional:", remove_duplicates([1, 1, 2, 3, 2]))

print("Q9:", missing_value([1, 2, 4, 5, 6]))
print("Q9 additional:", missing_value([1, 3, 4]))

print("Q10:", add([2, 7, 11, 15]))
print("Q10 additional:", add([1, 2, 3]))

print("Q11:",near_zero([-8, -3, 2, 5, -2]))
print("Q11 additional:", near_zero([-4, 4, 6]))

print("Q12:", common_element([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
print("Q12 additional:", common_element([1, 1, 2], [2, 1]))

print("Q13:",reverse([1, 2, 3, 4, 5]))
print("Q13 additional:", reverse([1, 2, 3]))

print("Q14:", maximum_sum([4, 7, 2, 9, 5]))
print("Q14 additional:", maximum_sum([-5, -2, -7]))

print("Q15:", add([2, 4, 3, 5, 7, 8, 1]))
print("Q15 additional:", add([1, 2, 3]))
