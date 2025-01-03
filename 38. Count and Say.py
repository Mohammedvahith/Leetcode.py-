'''
Example 1:

Input: n = 4

Output: "1211"

Explanation:
countAndSay(1) = "1"
countAndSay(2) = RLE of "1" = "11"
countAndSay(3) = RLE of "11" = "21"
countAndSay(4) = RLE of "21" = "1211"

Example 2:

Input: n = 1

Output: "1"

Explanation:
This is the base case.
'''
def countAndSay(n: int) -> str:
    if n == 1:  # Base case
        return "1"

    prev = countAndSay(n-1)

    result = ""

    count = 1

    for i in range(len(prev)):
        if i+1 < len(prev) and prev[i] == prev[i+1]:
            count += 1
        else:
            result += str(count) + prev[i]
            count =1
            
    return result

n = 4
print(countAndSay(n))

    
