import string

def cipher(msg, k):
  p = 0
  key_list = list(k.keys())
  val_list = list(k.values())
  while p < len(msg):
    pos = val_list.index(msg[p])
    i = key_list[pos]
    pos = val_list.index(msg[p+1])
    j = key_list[pos]
    if (i % 5) == (j % 5):
      if (i + 5) > 24:
        a = k[i%5]
      else:
        a = k[i+5]
      if (j + 5) > 24:
        b = k[j%5]
      else:
        b = k[j+5]
    elif (i // 5) == (j // 5):
      c = i // 5
      if ((i + 1) // 5) != c:
        a = k[c*5]
      else:
        a = k[i+1]
      if ((j + 1) // 5) != c:
        b = k[c*5]
      else:
        b = k[j+1]
    else:
      y = ((i // 5) * 5) + (j % 5)
      z = ((j // 5) * 5) + (i % 5)
      a = k[y]
      b = k[z]
    msg = msg[:p] + a + msg[p+1:]
    msg = msg[:p+1] + b + msg[p+2:]
    p += 2

  m = ' '.join([msg[i:i+5] for i in range(0, len(msg), 5)])
  h = '\n'.join([m[i:i+60] for i in range(0, len(m), 60)])
  return h.lower()

def decipher(msg, k):
  p = 0
  key_list = list(k.keys())
  val_list = list(k.values())
  while p < len(msg):
    pos = val_list.index(msg[p])
    i = key_list[pos]
    pos = val_list.index(msg[p+1])
    j = key_list[pos]
    if (i % 5) == (j % 5):
      if (i - 5) < 0:
        a = k[20+(i%5)]
      else:
        a = k[i-5]
      if (j - 5) < 0:
        b = k[20+(j%5)]
      else:
        b = k[j-5]
    elif (i // 5) == (j // 5):
      c = i // 5
      if ((i - 1) // 5) != c:
        a = k[(c*5)+4]
      else:
        a = k[i-1]
      if ((j - 1) // 5) != c:
        b = k[(c*5)+4]
      else:
        b = k[j-1]
    else:
      y = ((i // 5) * 5) + (j % 5)
      z = ((j // 5) * 5) + (i % 5)
      a = k[y]
      b = k[z]
    msg = msg[:p] + a + msg[p+1:]
    msg = msg[:p+1] + b + msg[p+2:]
    p += 2
  return msg.lower()

print("1. PLAIN TO CIPHER")
print("2. CIPHER TO PLAIN")
print("0. EXIT")
print()
ch = eval(input("ENTER YOUR CHOICE : "))
print()

if ch == 1:
  f = open('PLAIN.txt', 'r')
  msg = f.read()
  f.close()
elif ch == 2:
  f = open('CIPHER.txt', 'r')
  msg = f.read()
  f.close()
elif ch == 0:
  exit(0)
else:
  print("INVALID CHOICE !!!")

k = {}

key = input("ENTER THE KEY  : ")
print()

msg = msg.lower()
key = key.lower()

msg = msg.replace('j', 'i')
key = key.replace('j', 'i')

m = ''.join(ch for ch in msg if ch.isalpha())

p = 0
while p < len(m):
  if ((p+1) < len(m)) and (m[p] == m[p+1]):
    if m[p] == 'x':
      m = m[:p+1] + 'q' + m[p+1:]
    else:
      m = m[:p+1] + 'x' + m[p+1:]
  p += 2

if len(m) % 2 != 0:
  m = m + 'z'

for i in key:
  if i not in k.values() and i.isalpha():
    k[len(k.keys())] = i

for i in string.ascii_lowercase:
  if i not in k.values() and (i != 'j'):
    k[len(k.keys())] = i

if ch == 1:
  x = cipher(m,k)
  print("PLAIN TEXT  : ")
  print(msg)
  print("CIPHER TEXT : ")
  print(x)
elif ch == 2:
  x = decipher(m,k)
  print("CIPHER TEXT : ")
  print(msg)
  print("PLAIN TEXT  : ")
  print(x)

print()
