from operator import truediv
import sys
#regex built-in
import re

numeric: set = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
operation: set = {"*", "/", "+"}

class Expression():
    _sign: bool
    _number: int = 0
    _with_x: bool
    _power: int = 0


# def main():
if len(sys.argv) != 2:
    print("error, wrong number of arguments")
    sys.exit()
all_expr : list = []
full_equation: str = sys.argv[1].split(" ")
print("all split", full_equation)
for num in full_equation:
    print("elements", num)
    if num not in operation or (num[0] == "-" and len(num) > 1) :
        exp = Expression()
        j : int = 0
        i : list = list(num)
        while len(i) > j:
            if i[j] == "-":
                exp._sign = False
                j += 1
            else:
                exp._sign = True
            if len(i) > j and i[j] in numeric:
                while len(i) > j and i[j] in numeric:
                    exp._number += int(i[j])
                    exp._number *= 10
                    j += 1
                exp._number /= 10
            else:
                exp._number = 1
            if len(i) > j and i[j] == "X":
                exp._with_x = True
                j += 1
            else:
                exp._with_x = False
            if len(i) > j and i[j] == "^":
                while len(i) > j and i[j].isnumeric():
                    exp._number += int(i[j])
                    exp._number *= 10
                    j += 1
                exp._number /= 10
            else:
                exp.power = 1
        all_expr.append(exp)
        print("exp", exp)
print(all_expr)
        

