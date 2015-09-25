#!/usr/bin/env python
'''
Problem Title:Counting Inversions  
Rosalind Armory ID: inv
URL: http://rosalind.info/problems/inv/
'''
import sys

def fr(fn):
    with open(fn) as f:
        n = int(f.readline().strip())
        lst = map(int, f.readline().strip().split(" "))
        assert len(lst) == n
    return lst

# other method that divied and conque
def merge_sorted_arrays_counting_inversions(A, B):
    '''Merges two sorted arrays A and B into a sorted array C and counts the nmber of inversions.'''
    # Initialize variables.
    i, j = 0, 0
    count = 0
    C = []
    # Add the smallest item from A or B until one of the arrays runs out of items.
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            count += len(A) - i
            j += 1
    # Add on the additional items from the remaining array. (Only one will be nonempty)
    C += A[i:] + B[j:]
    return C, count

def merge_sort_inversion_count(A):
    '''Uses the merge sort algorithm to sort an array A and count inversions.'''
    # Trivially sorted if the length is <= 1.
    # Also, this is used in the process of breaking down the array before rebuilding it sorted.
    if len(A) <= 1:
        return A, 0
    # Get the midpoint of A.
    midpoint = len(A) / 2
    # Use merge sort to sort the lower and upper halves of A.
    lower, lower_inv = merge_sort_inversion_count(A[:midpoint])
    upper, upper_inv = merge_sort_inversion_count(A[midpoint:])
    # Combine the sorted lower and upper halves.
    combined, combined_inv = merge_sorted_arrays_counting_inversions(lower, upper)
    return combined, lower_inv + upper_inv + combined_inv

def main():
    sys.stdout = open("inv.out", "w")
    print merge_sort_inversion_count(fr("inv"))[1]
                
if __name__ == '__main__':
    main()
