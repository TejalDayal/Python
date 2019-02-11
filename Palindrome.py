#Write a Python function that checks whether a passed string is palindrome or not.

def isPalindrome(string):
	left_pos = 0
	right_pos = len(string) - 1

	while right_pos >= left_pos:
		if not string[left_pos] == string[right_pos]:
			return False
	return True
a=input("Enter the string: ")
print(isPalindrome(a))
