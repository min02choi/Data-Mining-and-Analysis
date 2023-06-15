def student_info():
    print("[ Student ID: 2116309 ]")
    print("Name: 최민영\n")

def show_menu():
    print("1. K-means")
    print("2. Hierarchical Clustering")
    print("3. DBSCAN")
    print("4. Quit")

    num = int(input())
    return num

def k_means():
    n_clusters = int(input("n_clusters: " ))
    rand_state = int(input("random_state: "))

    print("<Clustering Result>")


n = 0
while(n != 4):
    student_info()
    n = show_menu()
