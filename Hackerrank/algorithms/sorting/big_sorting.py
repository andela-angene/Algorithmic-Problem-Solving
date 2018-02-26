unsorted = ['31415926535897932384626433832795', '1', '3', '10', '3', '5']

# unsorted.sort()
unsorted = sorted(unsorted, key=lambda item: int(item))
# or: unsorted = sorted(unsorted, key=int)
print(unsorted)
