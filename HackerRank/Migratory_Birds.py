def solution(arr):
    # Write your code here
    ans = 0
    highest = 0
    sightings = {}
    keys = []
    
    for i in range(1,6):
    	if arr.count(i) > 1:
    		sightings[i] = arr.count(i)
    
    sorted_by_values = dict(sorted(sightings.items(), key=lambda item: item[1], reverse=True))
    
    for key, value in sorted_by_values.items():
    	if value >= highest:
    		highest = value
    		keys.append(key)
    		ans = min(keys)
    		
    return ans
    
# -----------------------------

input = "1 4 4 4 5 3"

arr = [int(item) for item in input.split()]

solution = solution(arr)
print(f'--> {solution}')	
