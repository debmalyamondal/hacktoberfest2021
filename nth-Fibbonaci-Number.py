#recursive approach
def fib_num(n):
   if n<=0:
      print("Fibonacci can't be computed")
   # First Fibonacci number
   elif n==1:
      return 0
   # Second Fibonacci number
   elif n==2:
      return 1
   else:
      return fib_num(n-1)+fib_num(n-2)

#input
n=int(input("Enter n: "))
print("{}th Fibonacci number is ".format(n),fib_num(n))
