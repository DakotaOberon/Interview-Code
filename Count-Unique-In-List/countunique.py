"""
Problem Statement:

Given a list of at least 1 integer in ascending order
Write a function that returns the count of unique values
"""

class CountUnique:
    def __init__(self):
        self.inputs = [
            [1],
            [1, 1, 1, 1, 1],
            [1, 2, 2, 3, 3, 3, 4, 4, 4, 4],
            [2, 3, 7]
        ]

    def func1(self, input):
        '''Using python built-in set (Used in interview)'''
        # Time O(1) | Space O(1)

        # Convert input into a set which removes duplicate values before returning length
        return len(set(input))

    def func2(self, input):
        '''Using an intermediary list with loop (Used in interview)'''
        # Time O(n) | Space O(n)

        # Create a list to hold unique values
        k = []

        for x in input:
            # Add integers not currently in the unique list to the list
            if x not in k:
                k.append(x)

        # Return the length of the unique list
        return len(k)

    def func3(self, input):
        '''Using an increment counter with loop (Used in interview)'''
        # Time O(n) | Space O(2)

        # Set defaults
        unique = 1
        prev = input[0]

        for i in range(1, len(input)):
            # If current value is larger than the previous
            if input[i] > prev:
                # Set prev to current value
                prev = input[i]

                # Increment the unique counter
                unique += 1

        return unique

def main():
    count = CountUnique()

    for inp in count.inputs:
        print('#######################')
        print('Running functions on list:', inp)
        print('Function1 Output:', count.func1(inp))
        print('Function2 Output:', count.func2(inp))
        print('Function3 Output:', count.func3(inp))

if __name__ == "__main__":
    main()
