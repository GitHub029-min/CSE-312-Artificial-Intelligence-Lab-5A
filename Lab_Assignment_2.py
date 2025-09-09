# Represent friendships as a graph
graph = {"A": ["B", "C"], "B": ["D"], "C": ["E"], "D": [], "E": []}

# Implement DFS (using recursion)
def dfs(graph, start, visited=None):
    if visited is None:
        visited = []

    # Visited student
    visited.append(start)
    print(start, end=" ")

    # Recursively visit each unvisited friend
    for friend in graph[start]:
        if friend not in visited:
            dfs(graph, friend, visited)

# Starting from student A
print("DFS starting from student A:")
dfs(graph, "A")
print("\n")

# Bonus: Allowing the user to input any student's name and print all friends reachable from that student
start_student = input("Enter the student name : ").strip()
if start_student in graph:
    print(f"DFS starting from student {start_student}:")
    dfs(graph, start_student)
else:
    print("Student not found in the graph.")