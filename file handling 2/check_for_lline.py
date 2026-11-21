def check_line_no():
    word="learning"
    data = True
    linenum=1
    with open('practice.txt', 'r') as f:
        data = f.readline()

        while data:
            
            if word in data:
                return linenum

            data =f.readline()
            linenum += 1
    return -1

print(check_line_no())