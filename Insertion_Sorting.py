# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 08:14:34 2024

@author: LENOVO
"""

import time

start_time = time.time()

with open("province.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()  # อ่านไฟล์ทีละบรรทัดแล้วเก็บในลิสต์
    
def InsertionSort(a_list):
    n = len(a_list)
    
    for i in range(1,n):
        
        temp = a_list[i]
        hole = i
        
        while hole>0 and a_list[hole-1]<temp:
            a_list[hole] = a_list[hole-1]
            hole = hole-1
            
        a_list[hole] = temp
        
    return a_list

sorted_lines = InsertionSort(lines)

end_time = time.time()
elapsed_time = end_time - start_time

for line in sorted_lines:
    print(line.strip())  # ลบ \n ออกเมื่อแสดงผล

print(f"Sorting Time: {elapsed_time:.5f} Sec.")