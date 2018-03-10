# 3. Longest Substring Without Repeating Characters#

# ==========First part: issue requirement============#
print "=======input the array========"
array = input("input the array:")
# print array[0]

# ==========Second part: issue solvement============#
list = {}
pist = {}
for i in range(len(array)):
    list[array[i]] = i
    pist[i] = array[i]
# print list

subarray = ''
presentlist = {}
start = maxlength = 0
for i in range(len(array)):
    if array[i] not in presentlist:
        maxlength = max(maxlength, i - start + 1)
        # print maxlength
    if array[i] in presentlist and start <= array[i]:
        start = presentlist[array[i]] + 1
        # print start
    presentlist[array[i]] = i
    # print i

print maxlength
