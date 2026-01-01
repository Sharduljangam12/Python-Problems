'''The included code stub will read an integer n from STDIN.

Without using any string methods, try to print the following
123...n'''
#It took me 36 minutes to solve this problem 
if __name__ == '__main__':
    n = int(input())
    
    for n in  range(1,n+1):
        print(n,end="") 
        