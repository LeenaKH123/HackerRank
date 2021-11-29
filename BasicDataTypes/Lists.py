if __name__ == '__main__':
    N = int(input()) # take the number of commands from the user
    lst = [] # create empty list

    for i in range(N):
        cmd = input().split() # insert 10 5. ['insert', 10, 5]
        if cmd[0]=='insert':
            lst.insert(int(cmd[1]),int(cmd[2]))
        if cmd[0]=='print':
            print(cmd(1), cmd(2))
        
