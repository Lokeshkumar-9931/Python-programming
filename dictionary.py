dic={
    "lokesh":"Human being",
    "vasudev":"god",
    "krishna":"radha",
    "27":"lokesh",
    "28":"vashu",
    "29":"govind",
    "30":"kesaw"
}
print(dic)
print(dic["krishna"])
print(dic["lokesh"])
print(dic["vasudev"])
print(dic["27"])
print(dic["28"])
print(dic["29"])
print(dic.get('name'))
print(dic.keys())
print(dic.values())

for key in dic.keys():
    print(key)
print(dic.items())  
  
for key,values in dic.items():
    print(f"the key is {key} and it value is {values}")
    
#dictionary methods    
ep={122:45,123:89,69:567}
ep2={222:67,223:45}
ep.update(ep2)
print(ep)
ep2.clear()
print(ep2)
ep.pop(122)
print(ep)
ep.popitem()
print(ep)
ep3={122:34,123:45,34:67}

del ep3[122]
print(ep3)
