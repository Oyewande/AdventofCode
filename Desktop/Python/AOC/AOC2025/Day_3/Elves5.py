def joltage(line):
    N = len(line)
    line = list(map(int, list(line)))
    candidate_i = N-2
    for i in reversed(range(N-2)):
        if line[i] >= line[candidate_i]:
            candidate_i = i
    return (line[candidate_i] * 10) + max(line[candidate_i+1:])

def main():
    with open('input-5.txt', 'r') as file:
        lines = file.readlines()
    result = 0
    for line in lines:
        number = joltage(line.strip())
        result += number
    print(result)

if __name__ == '__main__':
    main()