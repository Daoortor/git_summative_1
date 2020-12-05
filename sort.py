def maxplus(arr):
	ans = (0, ans[0])
	for i in range(len(arr)):
		if arr[i] > ans[1]:
			ans = (i, arr[i])
	return ans


def sort(arr):
	if len(arr) <= 1:
		return arr
	else:
		deleted = maxplus(arr)
		arr.pop(deleted[0])
		return sort(arr) + [deleted[1]]

