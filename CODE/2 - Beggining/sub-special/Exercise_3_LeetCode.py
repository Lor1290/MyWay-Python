class AlfabetoInglese:
    def __init__(number):
        self.num = number
        self.lis = []
    def translator(self):
        number{ 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
                11: "eleven", 12: "twelve", 13: "thirteen" 14: "fourteen" 15: "fifteen", 
                16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"
                20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90:  "ninty"}
        
        if self.num <= 20:
            self.num = number[self.num]
        else:
            
            for i in self.num[::-1]:
                self.lis.append(i)
            
            for 