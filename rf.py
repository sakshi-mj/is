def rail_fence(text, rails, mode):
    fence = [''] * rails
    if mode == 'e':  # Encryption
        row, step = 0, 1
        for char in text:
            fence[row] += char
            row += step
            if row == 0 or row == rails - 1:
                step = -step
        return ''.join(fence)
    else:  # Decryption
        pattern = [['' for _ in range(len(text))] for _ in range(rails)]
        row, step, idx = 0, 1, 0
        for i in range(len(text)):
            pattern[row][i] = '*'
            row += step
            if row == 0 or row == rails - 1:
                step = -step
        for i in range(rails):
            for j in range(len(text)):
                if pattern[i][j] == '*':
                    pattern[i][j] = text[idx]
                    idx += 1
        result, row, step = '', 0, 1
        for i in range(len(text)):
            result += pattern[row][i]
            row += step
            if row == 0 or row == rails - 1:
                step = -step
        return result

text = input("Enter text: ")
rails = int(input("Enter number of rails: "))
mode = input("Encrypt (e) or Decrypt (d)? ").lower()

print("Result:", rail_fence(text, rails, mode))



















