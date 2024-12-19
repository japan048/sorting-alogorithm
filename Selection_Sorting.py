# -*- coding: utf-8 -*-
"""
Created on Thu Sat 14 11:54:10 2024

@author: LENOVO
"""

import time

start_time = time.time()

with open("province.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

def SelectionSort(a_list):
    n = len(a_list)

    for i in range(0, n-1):
        iMax = i

        for j in range(i+1, n):
            
            if a_list[j] > a_list[iMax]:
                iMax = j

        # สลับตำแหน่ง
        temp = a_list[i]
        a_list[i] = a_list[iMax]
        a_list[iMax] = temp

    return a_list

# เรียงลำดับข้อมูล
sorted_lines = SelectionSort(lines)

end_time = time.time()
elapsed_time = end_time - start_time

# แสดงข้อมูลที่เรียงแล้ว
for line in sorted_lines:
    print(line.strip())  # ลบ \n ออกเมื่อแสดงผล

print(f"Sorting Time: {elapsed_time:.10f} Sec.")
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(f"เวลาที่ใช้ในการประมวลผล: {elapsed_time:.2f} วินาที")

# a = SelectionSort(lines)
# print (a)