# Input the number of rows (N) and columns (M)
N, M = map(int, input().split())
# Input the rows of the spreadsheet
rows = [input() for _ in range(N)]
# Input the column index (K) to sort by
K = int(input())
# Sort rows based on the Kth column and print the result
for row in sorted(rows, key=lambda row: int(row.split()[K])):
   print(row)
