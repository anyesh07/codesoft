
def calculate(a, b, op):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        return a / b
    raise ValueError("Unknown operator")

def main():
    try:
        a = float(input("Enter first number: ").strip())
        b = float(input("Enter second number: ").strip())
    except:
        print("Invalid number input.")
        return
    op = input("Enter operator (+ - * /): ").strip()
    try:
        res = calculate(a, b, op)
    except Exception as e:
        print("Error:", e)
    else:
        if isinstance(res, float) and res.is_integer():
            res = int(res)
        print("Result:", res)

if __name__ == "__main__":
    main()
