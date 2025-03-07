two=[]

while True:
 
  one=[]
  sch=input("school= ")
  for i in range(1,3):
   groupnum=i
   comp=input(f"What did group {i} particapate in?")
   place=input("What did they get? ")
   Details=(groupnum,sch,comp,place)
   one.append(Details)
  two.append(one)
  ans=input("Anymore schools to enter? (yes or no)")
  if ans=="no":
    break



for z in two:
  print(z)