#코뮤니티 모각코 3일차

lans=[215,513,712,803]

start = 1
end = max(lans)
target = 10

while(end-start>=0):
  cnt = 0
  mid = (start+end)//2

  for i in lans:
    cnt+=i//mid
  
  if target <= cnt:
    start = mid+1
  
  else: end = mid-1

print(end)