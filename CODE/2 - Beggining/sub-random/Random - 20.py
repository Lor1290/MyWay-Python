class Exercise:
    def PrintMax(num_1: int, num_2: int):
        min_n = min(num_1, num_2)
        max_n = max(num_1, num_2)
        print("> ", end = "")
        for x in range(min_n, max_n):
            print(x, end = " ")
        print("\n> ", end = "")
        for x in range(max_n, min_n, -1):
            print(x, end = " ")
    def MediaAndSum():
        #Primo metodo
        print("Inserisci 5 numeri positivi, \n> ")
        List_n = list(map(int, input().split()))
