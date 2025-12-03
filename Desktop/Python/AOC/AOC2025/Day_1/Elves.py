def zero_hits_from_file(path):
    
    with open ("input-3.txt", "r") as file:
        lines = [line.rstrip("\n") for 
                 line in file]
    
    startpoint = 50
    count = 0
    
    for line in lines:
        if not line:
            continue
        direction = line[0].upper()
        distance = int(line[1:])
        
        if direction == 'L':
            startpoint = (startpoint - distance) % 100
        elif direction == 'R':
            startpoint = (startpoint + distance) % 100
            
        if startpoint == 0:
            count += 1
    return count 
   
print(zero_hits_from_file("input-3.txt"))
          