import re
pattern = re.compile(r'(\d+)(\1)+')

def main():
    with open ("input-4.txt", "r") as file:
        line = file.readline().strip()
    ranges = line.split(",")
    results = []
    
    for range in ranges:
        left, right = range.split("-")
        start, stop = int(left), int(right)
        
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