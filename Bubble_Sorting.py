# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 08:59:31 2024

@author: LENOVO
"""

import time

start_time = time.time()

with open("province.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    
def BubbleSort(a_list):
    n = len(a_list)
    for k in range(1,n):
        flag = 0
        for i in range(0,n-k):
            if a_list[i] < a_list[i+1]:
                tmp = a_list[i]
                a_list[i] = a_list[i+1]
                a_list[i+1] = tmp
                flag = 1
        if flag == 0:
            break
    return a_list

sorted_lines = BubbleSort(lines)

end_time = time.time()
elapsed_time = end_time - start_time

for line in sorted_lines:
    print(line.strip())  # ลบ \n ออกเมื่อแสดงผล

print(f"Sorting Time: {elapsed_time:.5f} Sec.")
