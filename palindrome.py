def is_palindrome(string: str) -> bool:
    string = string.replace(' ', '').lower()
    return string == string[::-1]
    #Ana

def run():
    print(is_palindrome(3454))

if __name__ == '__main__':
    run()