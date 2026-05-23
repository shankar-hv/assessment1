#Palindrome check

def palindrome(s: str):
    copy = "".join(s.split()).lower()
    new_string = "".join(s.split()).lower()
    # print(new_string)
    return new_string==copy

def main()->None:
    inp = input('Enter the string: ')
    print(palindrome(inp))
    
if __name__ == '__main__':
    main()