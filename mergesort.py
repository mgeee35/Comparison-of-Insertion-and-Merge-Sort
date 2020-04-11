import math


# merge-sort function
def merge_sort(A, p, r):
    if p < r:
        m = (p + r) // 2
        merge_sort(A, p, m)
        merge_sort(A, m + 1, r)
        merge(A, p, m, r)


# merge function
def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)

    for i in range(0, n1):
        L[i] = A[p + i]

    for j in range(0, n2):
        R[j] = A[q + 1 + j]

    L[n1] = math.inf
    R[n2] = math.inf

    i = 0
    j = 0

    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
