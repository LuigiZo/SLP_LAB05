from Lab5.lab05 import calculateAvgList1, calculateAvgNormInputList, calculateAvgList, calculateAvgFromList
#point1
print("Point1")
list_avg = calculateAvgList(5,4,7,6,5,8)
print(f"AVG: {list_avg}")

#point2
print(" ")
print("Point2")
calculateAvgNormInputList(0.5, 1, 3, 5, 8, 4, 7)
calculateAvgNormInputList(0.5, 1, 3, 5, 8, 4, 7, 5, 8)


#point 3.1
print(" ")
print("Point3.1")
list1_avg = calculateAvgList(5,4,7,5,5,8)
print(f"AVG: {list1_avg}")
#point 3.2
print(" ")
print("Point3.2")
print("DOUBLE STAR **")
lists_avgN = calculateAvgFromList(list1=5, list2=3, list3=4.5)
print(f"AVG: {lists_avgN}")
