 ##############################################################################################################################
 +# Method 1
  # Ideas: 
  # Time Complexity: O(n)
  # Space Complexity: O(n)
  ##############################################################################################################################
  
 -def Reverse(s):
 +def Reverse1(s):
  	return s[::-1]
  
  ##############################################################################################################################
 +# Method 2
 +# Ideas: 
 +# Time Complexity: O(n)
 +# Space Complexity: O(n)
 +##############################################################################################################################
 +
 +def Reverse2(s):
 +	result = ""
 +	for i in range(len(s)):
 +		print i
 +		result += s[len(s)-i-1]
 +	return result
 +
 +##############################################################################################################################
  
  def main():
  	s = "Hello, World!"
 -	result = Reverse(s)
 -	print "Before: ", s
 -	print "After: ", result
 +	result1 = Reverse1(s)
 +	result2 = Reverse2(s)
 +	print "Input: ", s
 +	print "Result 1: ", result1
 +	print "Result 1: ", result2
  
  if __name__ == '__main__':
  	main() 
View  
35  CTCI/Python/Chapter1-3.py
@@ -1,6 +1,7 @@
  ##############################################################################################################################
 +# Method 1
  # Ideas: For both of the them, for example, we can sort them with MergeSort, and then compare them.
 -# Time Complexity: O(nlogn)
 +# Time Complexity: O(nlogn) based on the sorting algorithm
  # Space Complexity: O(1)
  ##############################################################################################################################
  
 @@ -31,7 +32,7 @@ def MergeSort(L):
  
  # end define merge sort
  
 -def isPermutation(s1, s2):
 +def IsPermutation1(s1, s2):
  	if len(s1) != len(s2):
  		return False
  	else:
 @@ -44,12 +45,40 @@ def isPermutation(s1, s2):
  			return False
  
  ##############################################################################################################################
 +# Method 2
 +# Ideas: First create a flag array of 256 ZERO, since there are only 256 different ASCII characters.
 +#        Then, for each of the char in string_1 map to the array, flag++
 +#        And, for each of the char in string_2 map to the array, flag--
 +#        If all elements in the array still 0, then string_2 is the permutation of string_1
 +# Time Complexity: O(n) 
 +# Space Complexity: O(1)
 +##############################################################################################################################
 +
 +def IsPermutation2(s1, s2):
 +	if len(s1) != len(s2):
 +		return False
 +	else:
 +		Flag = [0 for i in range(256)]
 +		for x in s1:
 +			Flag[ord(x)] +=1
 +
 +		for x in s2:
 +			Flag[ord(x)] -=1
 +
 +	for f in Flag:
 +		if f != 0:
 +			return False
 +
 +	return True
 +
 +##############################################################################################################################
  
  def main():
  	string1 = "Hello,World!"
  	string2 = "oHell,!Wordl"
  	print "Is \"{}\" a permutation of \"{}\"".format(string2, string1)
 -	print "Result is: ", isPermutation(string1, string2)
 +	print "Result 1: ", IsPermutation1(string1, string2)
 +	print "Result 2: ", IsPermutation2(string1, string2)
  
  if __name__ == '__main__':
  	main()
