
"""def grtoounce(grams):
    ounce = 28.3495231 * grams
    print(ounce)
a = 150
ounces_from_a = grtoounce(a)"""

"""def temp(f):
    c = (5/9) * (f - 32)
    print(c)
a = 48
celsius = temp(a)"""

"""def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num/2) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if prime(num)]

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
prime_numbers = filter_prime(numbers_list)

print("Original list:", numbers_list)
print("Prime numbers:", prime_numbers)"""

def reverse_words(sentence):
    words = sentence.split()

    reversed_sentence = ' '.join(reversed(words))

    return reversed_sentence

user_input = input("Enter a sentence: ")
result = reverse_words(user_input)

print("Reversed words in the sentence:", result)
