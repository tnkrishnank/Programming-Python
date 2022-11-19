def cipher(msg, a, b):
  for i in range(len(msg)):
    c = ord(msg[i])
    if c >= 65 and c <= 90:
      c = c - 65
      c = ((c * a) + b) % 26
      c = c + 97
      msg = msg[:i] + chr(c) + msg[i+1:]
    elif c >= 97 and c <= 122:
      c = c - 97
      c = ((c * a) + b) % 26
      c = c + 97
      msg = msg[:i] + chr(c) + msg[i+1:]
  return msg.upper()

def decipher(msg, a, b):
  for i in range(len(msg)):
    c = ord(msg[i])
    if c >= 65 and c <= 90:
      c = c - 65
      for j in range(26):
        d = ((j * a) + b) % 26
        if d == c:
          msg = msg[:i] + chr(j+97) + msg[i+1:]
          break
    elif c >= 97 and c <= 122:
      c = c - 97
      for j in range(26):
        d = ((j * a) + b) % 26
        if d == c:
          msg = msg[:i] + chr(j+97) + msg[i+1:]
          break
  return msg.upper()

msg = input("ENTER THE TEXT : ")
print()

print("1. PLAIN TO CIPHER")
print("2. CIPHER TO PLAIN")
print("0. EXIT")
print()
ch = eval(input("ENTER YOUR CHOICE : "))
print()

if ch == 1:
  x = cipher(msg,5,8)
  print("PLAIN TEXT  : ",msg)
  print("CIPHER TEXT : ",x)
elif ch == 2:
  x = decipher(msg,5,8)
  print("CIPHER TEXT : ",msg)
  print("PLAIN TEXT  : ",x)
elif ch == 0:
  exit(0)
else:
  print("INVALID CHOICE !!!")

print()
