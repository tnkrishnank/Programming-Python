import string

def cipher(msg, l, u):
  for i in range(len(msg)):
    c = ord(msg[i])
    if c >= 65 and c <= 90:
      if (c + (u[msg[i]] + 1) % 4) > 90:
        c = 64 + ((c + (u[msg[i]] + 1) % 4) - 90)
      else:
        c = c + (u[msg[i]] + 1) % 4
      u[msg[i]] = (u[msg[i]] + 1) % 4
      msg = msg[:i] + chr(c) + msg[i+1:]
    elif c >= 97 and c <= 122:
      if (c + (l[msg[i]] + 1) % 4) > 122:
        c = 96 + ((c + (l[msg[i]] + 1) % 4) - 122)
      else:
        c = c + (l[msg[i]] + 1) % 4
      l[msg[i]] = (l[msg[i]] + 1) % 4
      msg = msg[:i] + chr(c) + msg[i+1:]
  return msg

l = {}
u = {}

for i in string.ascii_lowercase:
  if i not in l.keys():
    l[i] = 0

for i in string.ascii_uppercase:
  if i not in u.keys():
    u[i] = 0

msg = input("ENTER THE TEXT : ")
print()

x = cipher(msg,l,u)
f = open('CIPHER.txt', 'w')
f.write(x)
f.close()
print("CIPHER TEXT EXPORTED TO FILE SUCCESSFULLY !!!")
print()
