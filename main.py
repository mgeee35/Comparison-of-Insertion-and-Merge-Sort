"""
Ege University ICI Fundamental Algorithmic Techniques Assignment
Comparison of Insertion and Merge Sort
Mustafa Guclu
April 2020 - GNU GPL v3 Licensed
"""

import insertionsort
import mergesort
import randomnumber
import duration


# calculation function of merge-sort duration
def calc_duration_merge_sort():
    p = 0
    r = len(A) - 1
    t1 = duration.start_time()
    mergesort.merge_sort(A, p, r)
    t2 = duration.stop_time()
    # print("By merge sort, sorted array is: ", end="\n")
    # print(A)
    print("Merge sorting time(sec): ", duration.calc_duration(t1, t2))
    print(end="\n")


# calculation function of insertion-sort duration
def calc_duration_insert_sort():
    t1 = duration.start_time()
    insertionsort.insertion_sort(B)
    t2 = duration.stop_time()
    # print("By insertion sort, sorted array is: ", end="\n")
    # print(B)
    print("Insertion sorting time(sec): ", duration.calc_duration(t1, t2))
    print(end="\n")


# driver code to test the above code
if __name__ == '__main__':

    """
    A = randomnumber.trial_array.copy()
    print("For array including", len(A), "elements", end="\n")
    # print("Array including", len(A), "elements is", end="\n")
    # print(A)
    calc_duration_merge_sort()
    B = randomnumber.trial_array.copy()
    print("For array including", len(B), "elements", end="\n")
    # print("Array including", len(B), "elements is", end="\n")
    # print(B)
    calc_duration_insert_sort()
    """

    A = randomnumber.array1.copy()
    print("For array including", len(A), "elements", end="\n")
    # print("Array including", len(A), "elements is", end="\n")
    # print(A)
    calc_duration_merge_sort()
    B = randomnumber.array1.copy()
    print("For array including", len(B), "elements", end="\n")
    # print("Array including", len(B), "elements is", end="\n")
    # print(B)
    calc_duration_insert_sort()

    A = randomnumber.array2.copy()
    print("For array including", len(A), "elements", end="\n")
    # print("Array including", len(A), "elements is", end="\n")
    # print(A)
    calc_duration_merge_sort()
    A = randomnumber.array2.copy()
    print("For array including", len(B), "elements", end="\n")
    # print("Array including", len(B), "elements is", end="\n")
    # print(B)
    calc_duration_insert_sort()

    A = randomnumber.array3.copy()
    print("For array including", len(A), "elements", end="\n")
    # print("Array including", len(A), "elements is", end="\n")
    # print(A)
    calc_duration_merge_sort()
    A = randomnumber.array3.copy()
    print("For array including", len(B), "elements", end="\n")
    # print("Array including", len(B), "elements is", end="\n")
    # print(B)
    calc_duration_insert_sort()

    A = randomnumber.array4.copy()
    print("For array including", len(A), "elements", end="\n")
    # print("Array including", len(A), "elements is", end="\n")
    # print(A)
    calc_duration_merge_sort()
    A = randomnumber.array4.copy()
    print("For array including", len(B), "elements", end="\n")
    # print("Array including", len(B), "elements is", end="\n")
    # print(B)
    calc_duration_insert_sort()
