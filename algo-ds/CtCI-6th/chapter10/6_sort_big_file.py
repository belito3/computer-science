"""
Big file (20GB), we can not load all data into memory -> external sort
Then, we devide big file into small chunk which has chunk size fit memory
Prequired: + merge sort: sort data in each chunk
            + merge k sorted array: merge 2 chunk file into one file

Input: input_file, chunk_size (can fit in RAM), num_chunk
    + Read input_file such that at most 'chunk_size',
    + Use merge sort then write data back to i'th file
    + Merge file:  we merge the chunks, one by one. At the end, we have a fully sorted file
--> This algorithm is known as external sort
"""
