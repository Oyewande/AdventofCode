import re
pattern = re.compile(r'(\d+)(\1)')
 
def main():
    with open ("input-4.txt", "r") as file:
        line = file.readline().strip()
    ranges = line.split(",")
    results = []
    
    for range in ranges:
        left, right = range.split("-")
        start, stop = int(left)-1, int(right)
        
        current = start
    
        while(True):
            next_num = current
            # print(next_num)
            if pattern.fullmatch(str(next_num)):
                results.append(next_num) 
                
            if next_num >= stop:
                break
            
            current = next_num + 1
            
    print(sum(results))
        
            
if __name__ == "__main__":
    main()

# def next_repeating_number(number):
#     number_string = str(number)
#     digit_count = len(number_string)
#     if digit_count % 2 == 0:
#         L = digit_count // 2

#         S_str = number_string[:L]
#         S = int(S_str)

#         power_of_10_plus_1 = 10 ** L + 1
#         C = S * power_of_10_plus_1

#         if C > number:
#             return C

#         S_prime = S + 1
#         if len(str(S_prime)) == L:
#             C_prime = S_prime * power_of_10_plus_1
#             return C_prime

#     L_prime = (digit_count // 2) + 1
#     S_min = 10 ** (L_prime - 1)

#     power_of_10_plus_1_prime = 10 ** L_prime + 1
#     C_min = S_min * power_of_10_plus_1_prime

#     return C_min


# def main():
#     with open('input-4.txt', 'r') as file:
#         line = file.readline()
#     ranges = line.split(',')
#     results = []
#     for range in ranges:
#         left, right = range.split('-')
#         start,stop = int(left)-1,int(right)
#         current = start
#         while(True):
#             next_number = next_repeating_number(current)
#             if next_number <= stop:
#                 results.append(next_number)
#             else:
#                 break
#             current = next_number
#     print(sum(results))
    
# if __name__ == "__main__":
#     main()