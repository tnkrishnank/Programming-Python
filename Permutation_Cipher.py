def cipher(msg, a, b):
  x = ""
  p = 0
  while p != m:
    v = p
    while v < len(msg):
      x += msg[v]
      v += m
    p += 1
  return x

def decipher(msg, a, b):
  x = ""
  p = 0
  while p != n:
    v = p
    while v < len(msg):
      x += msg[v]
      v += n
    p += 1
  return x

msg = input("ENTER THE TEXT : ")
m = eval(input("ENTER M : "))
n = eval(input("ENTER N : "))
print()

print("1. PLAIN TO CIPHER")
print("2. CIPHER TO PLAIN")
print("0. EXIT")
print()
ch = eval(input("ENTER YOUR CHOICE : "))
print()

if ch == 1:
  x = cipher(msg,m,n)
  print("PLAIN TEXT  : ",msg)
  print("CIPHER TEXT : ",x)
elif ch == 2:
  x = decipher(msg,m,n)
  print("CIPHER TEXT : ",msg)
  print("PLAIN TEXT  : ",x)
elif ch == 0:
  exit(0)
else:
  print("INVALID CHOICE !!!")

print()
