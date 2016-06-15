def Palindrome():
    words = input("Please enter a string: ")
    if words == words[::-1]:
        return True
    else:
        return False

print(Palindrome())