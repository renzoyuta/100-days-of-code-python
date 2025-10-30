# Instructions
- Read this code
    ```bash
    def is_leap(year):
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 4000 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
- Spot the problems 🐞.
- Modify the code to fix the program.

## Leap Year
- on every year that is divisible by 4 with no remainder.
- except every year that is evenly divisible by 100 with no remainder.
- unless the year is also divisible by 400 with no remainder.