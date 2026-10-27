def is_palindrome(text):
	"""Return whether text reads the same forward and backward, ignoring case and spaces."""
	#normalized = "".join(char.lower() for char in text).replace(" ", "")
	normalized = text.lower().replace(" ", "")
	stack = list(normalized)

	for char in normalized:
		if char != stack.pop():
			return False
	return True


if __name__ == "__main__":
	value = input("Enter text: ")
	print("Palindrome" if is_palindrome(value) else "Not a palindrome")

#  def is_palindrome(s):
#return s == s[::-1] 
