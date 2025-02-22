class Exercise:
    def Ex_1(num: int) -> int:
        count: int = 0
        for x in range(num):   
            count += x
            if count > num:
                return x-1

res_1: int = Exercise.Ex_1(9)
print(res_1)