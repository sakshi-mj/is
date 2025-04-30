def caesar(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift_val = shift if mode == 'e' else -shift
            result += chr((ord(char) - base + shift_val) % 26 + base)
        else:         
            result += char
    return result

text = input("Enter text: ")
shift = int(input("Enter shift: "))
mode = input("Encrypt (e) or Decrypt (d)? ").lower()

print("Result:", caesar(text, shift, mode))



