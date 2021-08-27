A = int(input())
L = int(input())
P = int(input())
H = int(input())
x = (A + L + (abs(A - L)))/2
y = (x + P + (abs(x - P)))/2
M = int(y*H)
print(M)