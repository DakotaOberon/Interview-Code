"""
Problem Statement:

Given a list representing a number ([1, 2, 3] = 123)
Write a function that returns the list after adding 1 to it
"""

class PlusOne:
    def __init__(self):
        self.inputs = [
            [1],
            [9],
            [1, 2, 9],
            [2, 0, 1, 0],
        ]
    
    def func1(self, input):
        '''Convert to string, increment, then convert to list (After-thought)'''
        # Time O(2n) | Space O(n)

        # Returns a new list
        output = list(int(x) for x in str(int(''.join([str(x) for x in input])) + 1))
        return output

    def func2(self, input):
        '''Same as function 1 but broken up into readable lines (After-thought)'''
        # Time O(2n) | Space O(n + 3)

        # Convert list of integers to a string by first converting to a list of strings
        number_string = ''.join([str(x) for x in input])

        # Convert number string in an integer and add 1
        new_number = int(number_string) + 1

        # Convert new number back into a string
        new_string = str(new_number)

        # Convert each character to an integer before adding back into input list
        output = [int(x) for x in new_string]

        # Returns a new list
        return output

    def func3(self, input):
        '''Use a loop and decrement the index (Used in interview)'''
        # Time best: O(1) worst: O(n) | Space O(2)

        # Start index at the last value (ones place)
        i = len(input) - 1

        # Set the val variable to the current number
        val = input[i]

        # Loop as long as the value is 9 (edge case)
        while val == 9:

            # Set value to 0
            input[i] = 0

            if i == 0:
                # Insert a 0 at the beginning of input list
                input.insert(0, 0)
                break
            
            # Decrement index
            i -= 1

            # Get new value
            val = input[i]
        
        # Increment the current value of the current index by 1
        input[i] += 1

        return input

def main():
    count = PlusOne()

    for inp in count.inputs:
        print('#######################')
        print('Running functions on list:', inp)
        print('Function1 Output:', count.func1(inp))
        print('Function2 Output:', count.func2(inp))
        print('Function3 Output:', count.func3(inp))

if __name__ == "__main__":
    main()
