def find_peak(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    def find_peak_rec(start_row, end_row, column):
        # Find the maximum element in the middle column
        mid_row = (start_row + end_row) // 2
        mid_max = matrix[mid_row][column]

        max_neighbor = float("-inf")
        max_neighbor_row = -1

        # Find the maximum neighbor in the same column
        if mid_row > 0 and matrix[mid_row - 1][column] > max_neighbor:
            max_neighbor = matrix[mid_row - 1][column]
            max_neighbor_row = mid_row - 1
        if mid_row < rows - 1 and matrix[mid_row + 1][column] > max_neighbor:
            max_neighbor = matrix[mid_row + 1][column]
            max_neighbor_row = mid_row + 1

        # Check if the middle element is a peak
        if mid_max >= max_neighbor:
            return (mid_row, column)

        # Recursively search in the subarray where the maximum neighbor was found
        if max_neighbor_row < mid_row:
            return find_peak_rec(start_row, mid_row - 1, column)
        else:
            return find_peak_rec(mid_row + 1, end_row, column)

    # Start the search in the middle column
    return find_peak_rec(0, rows - 1, columns // 2)

                        
        
            











matrix = [[9,8,3,11],[22,12,6,5],[12,7,6,9],[90,34,78,11]]

print(find_peak(matrix))