#assert 2 == 3, "error"

s = 'My Name is Julia'

if 'Name' in s:
    print('Substring found')

index = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}')

def test_substring(full_string, substring):
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"
    #assert full_string.find(substring) != -1, f"expected '{substring}' to be substring of '{full_string}'"

def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"

print(__name__)
if __name__ == "assert":
    test_abs1()
    print("All tests passed!")