# Rep-Units-Calcultation
Python script that shows which method to find a Rep Digit number is the fastest.

## What is a rep-unit number ?
It is a number only composed by the same digit.

Samples:
- 99999
- 88
- 77777
- 1

## How to find them ?
There are multiple technics to spot a rep-unit number:
- Change number into list of digits, and check if the first digit is equal to the second and so on
- Change the number into a set, and check if the set is only 1 long

## Formula Method
$$9 \times x \over (\lfloor(\log_{10}(x) + 1)\rfloor)^{10} - 1)$$

If the above formula returns a whole number, thus, the entered digit is not rep-unit.
