# -*- coding:utf-8 -*-
import random
import profile

def InsertionSort(list):
	for i in range(1,len(list)):
		index = i
		for j in range(i)[::-1]:
			if list[j+1] < list[j]:
				temp = list[j]
				list[j] = list[j + 1]
				list[j + 1] = temp
	return list

def BubbleSort(list):
	for i in range(len(list))[::-1]:
		for j in range(i):
			if list[j] > list[j + 1]:
				temp = list[j + 1]
				list[j + 1] = list[j]
				list[j] = temp
	return list

def SelectionSort(list):
	for i in range(len(list))[::-1]:
		index = i
		for j in range(i):
			if list[index] < list[j]:
				index = j
		temp = list[index]
		list[index] = list[i]
		list[i] = temp
	return list;

def _sort(list, start, middle, end,buf):
	i=start
	j=middle
	k=start

	while i<middle and j<end:
		if list[i]<list[j]:
			buf[k] = list[i]
			i += 1
		else:
			buf[k] = list[j]
			j += 1
		k +=1

	if i == middle:
		for x in range(j,end):
			buf[k] = list[x]
			k += 1
	else:
		for x in range(i, middle):
			buf[k] = list[x]
			k += 1

	for x in range(start, end):
		list[x] = buf[x]

def _merge(list,start,end,buf):
	if end - start > 1:
		middle = int((start + end)/2)
		_merge(list, start, middle,buf)
		_merge(list, middle, end,buf)
		_sort(list,start,middle,end,buf)

def MergeSort(list):
	copy = list[::]
	_merge(list,0, len(list), copy)
	return list

def _QuickSort(list,start,end):
	i = start;
	j = end - 1;

	if i < j:
		split = list[i]

		while i < j:
			while list[j] >= split and i < j:
				j -= 1;

			while list[i] <= split and i < j:
				i += 1

			if i < j:
				temp = list[i]
				list[i] = list[j]
				list[j] = temp

		list[start] = list[i]
		list[i] = split

		_QuickSort(list, start, i)
		_QuickSort(list, i + 1, end)

def QuickSort(list):
	_QuickSort(list, 0, len(list))
	return list

def test():
	data = []
	for i in range(10000):
		data.append(random.randint(0,1000))

	a = data[::]
	SelectionSort(a)
	a = data[::]
	InsertionSort(a)
	a = data[::]
	BubbleSort(a)
	a = data[::]
	MergeSort(a)
	a = data[::]
	QuickSort(a)

if __name__ == "__main__":
	profile.run("test()")
