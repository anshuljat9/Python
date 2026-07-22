ep1 = {109:63, 110:64, 111:65, 112:66, 113:67, 114:68, 115:69}
ep2 = {306:96, 307:98.5, 308:99}

# ep1.update(ep2)  # Merging ep2 into ep11 # Output: {109: 63, 110: 64, 111: 65, 112: 66, 113: 67, 114: 68, 115: 69, 306: 96, 307: 98.5, 308: 99}

# ep1.clear()  # Clearing ep1 # Output: {}

ep1.pop(110)  # Removing the key 110 from ep1 # Output: {109: 63, 111: 65, 112: 66, 113: 67, 114: 68, 115: 69}

ep1.popitem()  # Removing the last inserted item from ep1 # Output: (115, 69)

# del ep1 # Deleting ep1 completely
del ep1[109]  # Deleting the key 109 from ep1 # Output: {110: 64, 111: 65, 112: 66, 113: 67, 114: 68, 115: 69}

print(ep1)  