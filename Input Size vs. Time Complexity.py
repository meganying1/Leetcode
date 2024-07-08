# constraints for problems can be indicative of the upper bound for the time complexity of the solution:
#     n <= 10: time complexity is expected to be a factorial or exponential with a base greater than 2
#         possible solutions include backtracking and brute-force recursion
#     10 < n <= 20: time complexity is expected to be O(2^n)
#         possible solutions include backtracking and recursion
#     20 < n <= 100: upper bound for time complexity is O(n^3)
#         think of brute force solutions with nested loops, and improve on slow steps with tools like hash maps and heaps
#     100 < n <= 1000: time complexity is expected to be O(n^2)
#         consider using nested loops
#     1000 < n <= 1e5: slowest acceptable time complexity is O(nlogn), but goal is O(n)
#         ask if sorting or using heaps is helpful -> if not, aim for O(n) algorithm
#         possible solutions might use hash maps, two pointers implementations, monotonic stacks, binary search, heaps, etc.
#     1e5 < n <= 1e6: rare constraint, will likely require O(n) solution; O(nlogn) solution is possible if there is a small constant factor
#         likely need to use hash maps
#     1e6 < n: most common acceptable time complexity is O(logn) or O(1)
#         may need to reduce search space each iteration (such as by using binary search) or use tools to determine info in constant time (such as with math or use of hash maps)
