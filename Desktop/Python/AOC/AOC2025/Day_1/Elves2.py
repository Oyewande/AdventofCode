def count_zero_hits(start, moves):
    pos = start % 100
    total = 0

    for direction, k in moves:
        dir_val = -1 if direction == 'L' else 1

        t0 = (-dir_val * pos) % 100
        if t0 == 0:
            t0 = 100

        if k >= t0:
            total += 1 + (k - t0) // 100

        pos = (pos + dir_val * k) % 100

    return total


def load_moves(filename):
    moves = []
    with open("input-3.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            direction = line[0].upper()
            steps = int(line[1:])
            moves.append((direction, steps))
    return moves


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python dial.py <start_position> <moves_file>")
        sys.exit(1)

    start_position = int(sys.argv[1])
    moves_file = sys.argv[2]

    moves = load_moves(moves_file)
    result = count_zero_hits(start_position, moves)

    print("Total zero hits:", result)