"""
KSM1 IS A PYTHON MODULE THAT CONTAINS MANY CRYPTOGRAPHIC ALGORITHMS.
USE ksm.help() to get the list of crypto algos.

"""

import numpy as np
import math



def rail_fence_enc(plain,r):
  x=len(plain)
  if(x%2!=0):
    plain+=' '
    x+=1
  l1=list(range(2,x+1,2))
  l2=list(range(1,x,2))
  ciph1=""
  for x in l1:
    ciph1+=plain[x-1]
  ciph2=""
  ciph3=""

  for i in range(0,len(l2)):
    if i%2==0:
      ciph2+=plain[l2[i]-1]
    else:
      ciph3+=plain[l2[i]-1]

  res=ciph2+ciph1+ciph3
  return res



def rail_fence_dec(res,r):
  x=len(res)
  l1=list(range(2,x+1,2))
  l2=list(range(1,x,4))
  l3=list(range(3,x,4))
  x1=len(l2)
  x2=len(l3)
  x3=len(l1)
  plain=[None]*x

  for i in range(0,x):
    if i>=0 and i<x1:
      plain[l2[i]-1]=res[i]
    if i>=x1 and i<x1+x3:
      plain[l1[i-x1]-1]=res[i]
    if i>=x1+x3 and i<=x3+x2+x1:
      plain[l3[i-x1-x3]-1]=res[i]

  res1=''.join(plain)
  return res1


def single_column_transposition_enc(plain,key):
  x1=len(key)
  x2=len(plain)

  k=0
  if(x2%x1!=0):
    for i in range(0,x2-(x2%x1)):
      plain+=" "

  x2=len(plain)
  x3=int(x2/x1)
  #print(x2/x1)
  m1=np.full((x3,x1),fill_value="", dtype='<U1')
  for i in range(x3):
    for j in range(x1):
      m1[i,j]=plain[k]
      k+=1
  l1=[ord(x) for x in key]
  #print(m1)
  #print(l1)
  l2=sorted(l1)
  #print(l1)
  #print(l2)
  res=""
  for x in l2:
    y=l1.index(x)
    res+=''.join(list(m1[:,y]))
    #print(res)
  return res


def single_column_transposition_dec(ciph,key):
  x1=len(key)
  x2=len(ciph)
  m1=np.full((int(x2/x1),x1),fill_value="", dtype='<U1')
  k=0
  l1=[ord(x) for x in key]
  l2=sorted(l1)
  l3=[]
  for i in range(0,x2,int(x2/x1)):
    l3.append(ciph[i:i+int(x2/x1)])

  #print(l3)

  res=""
  for x in l1:
    y1=l2.index(x)
    y2=l1.index(x)
    m1[:,y2]=np.array(list(l3[y1]))

  #print(m1)
  for i in range(0,int(x2/x1)):
    res+=''.join(list(m1[i,:]))

  return res


def check_prime_naive(a):

  if a==1:
    print("1 is neither prime nor composite")

  elif a%2==0:
    print("Not prime, divisible by 2")

  else:
    for i in range(3,int(math.sqrt(a))+1,2):
      if(a%i==0):
        print("Not prime")
        print("Number "+str(a)+" is divisible by "+str(i))
        return

    print(str(a)+" is a prime number")


def caesar_cipher_encrpyt(a):
  k=int(input("Enter the key:- "))
  s2=""
  for x in a:
    l=ord(x)
    if (l>=65 and l<=90):
      l-=64
      s2+=chr(((l+(k%26))%26)+64)
    elif (l>=97 and l<=122):
      l-=96
      s2+=chr(((l+(k%26))%26)+96)

  return s2


def caesar_cipher_decrpyt(a):
  k=int(input("Enter the key:- "))
  s2=""
  for x in a:
    l=ord(x)
    if (l>=65 and l<=90):
      l-=64
      s2+=chr(((l-(k%26))%26)+64)
    elif (l>=97 and l<=122):
      l-=96
      s2+=chr(((l-(k%26))%26)+96)

  return s2

def find_letter_index(cmatrix, letter):
  for i, row in enumerate(cmatrix):
    if letter in row:
      return i, row.index(letter)
  return None


def playfair_cipher(input1,keyword,mode):
  keyword1=keyword
  #keyword="playfir"
  for i in range(97,123):
    if chr(i) not in keyword:
      keyword+=chr(i)

  keyword=keyword.replace("j","")
  #print(keyword)
  #print(len(keyword))
  #print(keyword1)

  matrix=[]
  l=[]
  i=0
  for x in keyword:
    if i==5:
      matrix.append(l[:])
      i=0
      l=[]
    l.append(x)
    i+=1
  matrix.append(l[:])
  #print(matrix)

  in2=[*input1]
  #print(in2)
  #print()

  no_of_chars=len(in2)
  if no_of_chars%2!=0:
    in2.append('a')

  in3=[]

  if mode=='e':
    for i in range(0,len(in2)-1,2):
      if in2[i]!=in2[i+1]:
        x=in2[i]+in2[i+1]
        in3.append(x)

      else:
        x1=in2[i]+'a'
        x2=in2[i+1]+'a'
        in3.append(x1)
        in3.append(x2)

  elif mode=='d':
    for i in range(0,len(in2)-1,2):
      x=in2[i]+in2[i+1]
      in3.append(x)

  print(in3)
  in4=[]
  cmatrix=[]
  for i in range(0,len(matrix)):
    cmatrix.append([row[i] for row in matrix])
  res=""
  for x in in3:
    s=0
    #print("row search")
    for i in range(0,5):
      if x[0] in matrix[i] and x[1] in matrix[i] and mode=='e':
        #print(x)
        #print(i)
        res+=matrix[i][(matrix[i].index(x[0])+1)%5]
        res+=matrix[i][(matrix[i].index(x[1])+1)%5]
        in4.append(matrix[i][(matrix[i].index(x[0])+1)%5]+matrix[i][(matrix[i].index(x[1])+1)%5])
        s=1
        break

      if x[0] in matrix[i] and x[1] in matrix[i] and mode=='d':
        #print(x)
        #print(i)
        res+=matrix[i][(matrix[i].index(x[0])-1)%5]
        res+=matrix[i][(matrix[i].index(x[1])-1)%5]
        in4.append(matrix[i][(matrix[i].index(x[0])-1)%5]+matrix[i][(matrix[i].index(x[1])-1)%5])
        s=1
        break

    #print("column search")
    for i in range(0,5):
     #print(x)
     #print(cmatrix[i])
     #print(x[0] in cmatrix[i] and x[1] in cmatrix[i])
     if x[0] in cmatrix[i] and x[1] in cmatrix[i] and mode=='e':
      #print(x)
      #print(i)
      res+=cmatrix[i][(cmatrix[i].index(x[0])+1)%5]
      res+=cmatrix[i][(cmatrix[i].index(x[1])+1)%5]
      in4.append(cmatrix[i][(cmatrix[i].index(x[0])+1)%5]+cmatrix[i][(cmatrix[i].index(x[1])+1)%5])
      s=1
      break

     if x[0] in cmatrix[i] and x[1] in cmatrix[i] and mode=='d':
      #print(x)
      #print(i)
      res+=cmatrix[i][(cmatrix[i].index(x[0])-1)%5]
      res+=cmatrix[i][(cmatrix[i].index(x[1])-1)%5]
      in4.append(cmatrix[i][(cmatrix[i].index(x[0])-1)%5]+cmatrix[i][(cmatrix[i].index(x[1])-1)%5])
      s=1
      break


    #print("random search")
    for i in range(0,5):
      if (not((x[0] in cmatrix[i]) and (x[1] in cmatrix[i])) and not( (x[0] in matrix[i]) and (x[1]  in matrix[i]))) and s!=1 and mode=='e':
        #print(x)
        #print(i)
        x0i=find_letter_index(matrix,x[0])
        x1i=find_letter_index(matrix,x[1])
        #print(x1i[0])
        y0i=matrix[x1i[0]][x0i[1]]
        y1i=matrix[x0i[0]][x1i[1]]
        y11=y0i+y1i
        res+=y11
        in4.append(y11)
        break

      if (not((x[0] in cmatrix[i]) and (x[1] in cmatrix[i])) and not( (x[0] in matrix[i]) and (x[1]  in matrix[i]))) and s!=1 and mode=='d':
        #print(x)
        #print(i)
        x0i=find_letter_index(matrix,x[0])
        x1i=find_letter_index(matrix,x[1])
        #print(x1i[0])
        y0i=matrix[x1i[0]][x0i[1]]
        y1i=matrix[x0i[0]][x1i[1]]
        y11=y0i+y1i
        res+=y11
        in4.append(y11)
        break

  print(in4)
  return res


