#！ /usr/bin/python
MyList = ["a", "b", "a", "c", "c", "a", "c"]
lst2 = ['7','8','1','3','6','2','9']
lst2.sort(reverse= False)
print(lst2)

my_dict = {i:MyList.count(i) for i in MyList}


def compressBad(string):
    res = ""
    count = 1
    #Add in first character
    res += string[0]
    #Iterate through loop, skipping last one
    for i in range(len(string)-1):
        if(string[i] == string[i+1]):
            count+=1
        else:
            if(count > 1):
                #Ignore if no repeats
                res += str(count)
            res += string[i+1]
            count = 1
    #print last one
    if(count >= 1):
        res += str(count)
    return res

print('my_dict2: ' + compressBad('aaaabbbbccs'))

time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

def first_non_repeating_character(str1):
    char_order = []
    ctr = {}
    for c in str1:
        if c in ctr:
            ctr[c] += 1
        else:
            ctr[c] = 1 
            char_order.append(c)
    a = []
    for c in char_order:
        if ctr[c] == 1:
            a.append(c)
    return a


def twoSumNaive(num_arr, pair_sum):
    for i in range(len(num_arr) - 1):
        for j in range(i + 1, len(num_arr)):
            if num_arr[i] + num_arr[j] == pair_sum:
                print("Pair with sum", pair_sum,"is: (", num_arr[i],",",num_arr[j],")")

      

# Driver Code
num_arr = [3, 5, 2, -4, 8, 11]
pair_sum = 7

# Function call inside print
twoSumNaive(num_arr, pair_sum) 
# numbers = [1,2,3,4,5,1,4,5] 
  
# # start parameter is not provided 
# Sum = sum(numbers) 
# print(Sum) # result is 25

# reverse = 'hello world'[::-1]
# print(reverse)

# test = set(x for x in numbers if numbers.count(x) > 1)
# print(test)

# print('yes'[::-1])

for fizzbuzz in range(51):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)



def first_non_repeating_character(str1):
    char_order = []
    ctr = {}
    for c in str1:
        if c in ctr:
            ctr[c] += 1
        else:
            ctr[c] = 1 
            char_order.append(c)
    a = []
    for c in char_order:
        if ctr[c] == 1:
            a.append(c)
    return a

def remove(str1, Nondup):
    str2 = ''
    for i in Nondup:
        str2 = str1.replace(i, '')
    return str2


foo = 'asddds'
foo1=''.join(sorted(set(foo), key=foo.index))
print(foo1)



# print(first_non_repeating_character('abcdef'))
# print(first_non_repeating_character('abcabcdef'))
# print(first_non_repeating_character('aabbcc'))
# print(remove('aabbccf', first_non_repeating_character('aabbccf')))
print(remove('aabbcc', first_non_repeating_character('aabbcc')))
def non_repeat(str1):
    lst = []
    dic1 = {}
    for n in str1:
        if n in dic1:
            dic1[n] += 1
        else:
            dic1[n] = 1
            lst.append(n)
    for n in lst:
        if dic1[n] == 1:
            return n
    return False
    


def first_non_repeating_character(str1):
  char_order = []
  ctr = {}
  for c in str1:
    if c in ctr:
      ctr[c] += 1
    else:
      ctr[c] = 1 
      char_order.append(c)
  for c in char_order:
    if ctr[c] == 1:
        return c
  return None

def Fibonacci(n):
   
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")
 
    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0
 
    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
 
# Driver Program
print('Fibonacci: {}'.format(Fibonacci(8)))



foo = 'asddds'
foo1=''.join(sorted(set(foo), key=foo.index))
print(foo1)



class Solution:
    def Fibonacci(self, n):
        if n < 0:
            return False
        elif n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            return self.Fibonacci(n-2) + self.Fibonacci(n-1)




class Solution2:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        left = 0
        right = len(A) - 1
        
        result = [-1, -1]
        
        while left <= right:
            mid = (left + right) / 2
            
            if A[mid] > target:
                right = mid - 1
            elif A[mid] < target:
                left = mid + 1
            else:
                result[0] = mid
                result[1] = mid
                
                i = mid - 1
                while i >= 0 and A[i] == target:
                    result[0] = i
                    i -= 1
                
                i = mid + 1
                while i < len(A) and A[i] == target:
                    result[1] = i
                    i += 1
                    
                break
                
        return result


class Solution_3:
    def gcd(self , a , b ):
        n = 2
        for n in range(2, 10**9, 1):
            if a % n == 0 and b % n == 0: 
                return n

    def ReverseList(self, pHead):
		# write code here
        if not pHead or not pHead.next:
            return pHead
        
        last =None
        
        while pHead:
            tmp = pHead.next#将下一步的地址指向给tmp
            pHead.next=last#将一个新的链表指向给旧链表pHead，这个时候就把pHead截断了，只剩下前面的链表值
            last=pHead#将旧链表的地址指向给新链表
            pHead=tmp#将旧链表原来的下一步只指向给pHead
        return last



def findPeakElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    N = len(nums)
    output = []
    for i in range(len(nums)):
        if i==0 or i==N-1:
            continue
        else:
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                return i
    if nums[0]<=nums[N-1]:
        return N-1
    else:
        return 0

if __name__ == "__main__":
    print(Solution_3().gcd(3,6))
    print(findPeakElement([1,3,4,6,7,1,3]))

    result = 0
    n = 5
    for i in range(1, n + 1):
        print(i)
        result += i
        # this ^^ is the shorthand for
        # result = result + i
    print(result)
    #print(Solution_3().ReverseList(1,2,3))
    # print(Solution().Fibonacci(9))
    # print(Solution().Fibonacci(8))
    # for n in range(10):
    #     print(Solution().Fibonacci(n))
    # def foo1():
    #     print("starting...")
    #     while True:
    #         res = yield 4
    #         print("res:",res)
    # g = foo1()
    # print(next(g))
    # print("*"*20)
    # print(next(g))

    # def foo(num):
    #     print("starting...")
    #     while num<10:
    #         num=num+1
    #         yield num
    # for n in foo(0):
    #     print(n)