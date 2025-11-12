
import secrets
import string

def generate(length, use_upper=True, use_digits=True, use_symbols=True):
    alphabet = string.ascii_lowercase
    if use_upper:
        alphabet += string.ascii_uppercase
    if use_digits:
        alphabet += string.digits
    if use_symbols:
        alphabet += "!@#$%^&*()-_=+[]{}|;:,.<>?/"
    if length <= 0:
        return ""
    return "".join(secrets.choice(alphabet) for _ in range(length))

def main():
    try:
        l = int(input("Desired password length (e.g. 12): ").strip())
    except:
        print("Invalid length.")
        return
    up = input("Include uppercase? (Y/n): ").strip().lower() != "n"
    dg = input("Include digits? (Y/n): ").strip().lower() != "n"
    sy = input("Include symbols? (Y/n): ").strip().lower() != "n"
    pwd = generate(l, up, dg, sy)
    print("\nGenerated password:\n", pwd)

if __name__ == "__main__":
    main()
