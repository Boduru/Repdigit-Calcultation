# Repeated Digits Calcultation
Python script that shows which method to find a Repeated Digit number is the fastest.

## What is a repdigit ?
It is a number only composed by the same digits.

Samples:
- 99999
- 88
- 77777
- 1

## How to find them ?
There are multiple technics to identify a repdigit number:
- Change number into a list of digits, and check if the first digit is equal to the second and so on
- Change the number into a set, and check if the set is only 1 long

## Formula Method
$$9 \times x \over (\lfloor(\log_{10}(x) + 1)\rfloor)^{10} - 1)$$

If the above formula returns a whole number, thus, the entered number is a repdigit.
