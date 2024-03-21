#This is a simple and easy question in which an array is give to you named "arr"  and you are required to find the largest element of the array 
#There can be a lot of ways to find the largest element in an array 
#link to the below question : "https://www.codingninjas.com/studio/problems/largest-element-in-the-array-largest-element-in-the-array_5026279"
"""Problem Statement :-Given an array 'arr' of size 'n' find the largest element in the array.
Example:

Input: 'n' = 5, 'arr' = [1, 2, 3, 4, 5]

Output: 5

Explanation: From the array {1, 2, 3, 4, 5}, the largest element is 5.
Detailed explanation ( Input/output format, Notes, Images )
Sample input 1:
6
4 7 8 6 7 6 
Sample output 1:
8
Explanation of sample input 1:
The answer is 8.
From {4 7 8 6 7 6}, 8 is the largest element.
Sample input 2:
8
5 9 3 4 8 4 3 10 
Sample output 2:
10
Expected Time Complexity:
O(n), Where 'n' is the size of an input array 'arr'.
Constraints :
1 <= 'n' <= 10^5
1 <= 'arr[i]' <= 10^9

Time Limit: 1 sec"""
#Method 1: using a variable name mac_element and iterate through the array using a loop and compare all the values with the value of max_element
def max_ele(arr):
    max_ele=arr[0]
    for i in range(len(arr)):
        max_ele=max(max_ele,arr[i])
    return max_ele
#Method2 : using max function in Python
def Max_ele(arr):
    return max(arr)
#Method3 : sort the given array in ascending order using sort function and return the element at last position in the sorted array 
def Max_Ele(arr):
    arr.sort()
    return arr[-1]
def main():
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(int(input()))
    max_Ele=max_ele(arr)
    print("Largest number in the given array arr using method 1 is ",max_Ele)
    max_Ele=Max_ele(arr)
    print("Largest number in the given array arrusing method 2 is ",max_Ele)
    max_Ele=Max_Ele(arr)
    print("Largest number in the given array arrusing method 3 is ",max_Ele)
    return 
print(main())


