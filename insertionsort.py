# insertion-sort function
def insertion_sort(A):
    for j in range(1, len(A)):

        key = A[j]
        i = j

        while i > 0 and A[i - 1] > key:
            A[i] = A[i - 1]
            i = i - 1

        A[i] = key
