def new_joltage(line):
    N = len(line)
    line = list(map(int, list(line)))

    result = []
    current = line
    for i in reversed(range(12)):
        if len(current) <= i+1:
            result.append(''.join(map(str,current)))
            break

        num = max(current[:-i]) if i > 0 else max(current)
        result.append(str(num))
        index = current.index(num)
        current = current[index+1:]

    return int(''.join(result))

def main():
    with open('input-5.txt', 'r') as file:
        lines = file.readlines()
        
    result = 0
    
    for line in lines:
        number = new_joltage(line.strip())
        result += number
    print(result)

if __name__ == '__main__':
    main()