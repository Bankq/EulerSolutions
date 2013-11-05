def main():
    with open("67.input", "r") as f:
        lines = f.readlines()
        res = [int(x) for x in lines[0].split()]
        
        for line in lines[1:]:
            # read current line
            cur = [int(x) for x in line.split()]
            
            for i, v in enumerate(cur):
                if i == 0:
                    cur[i] = v + res[0]
                elif i == (len(cur) - 1):
                    cur[i] = v + res[-1]
                else:
                    cur[i] = v + max(res[i], res[i-1])
            res = cur
        return max(res)

print(main())
