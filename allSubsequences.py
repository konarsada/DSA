def ps(ip, op):
    if(len(ip) == 0):
        print(op, end = ", ")
        return
    ps(ip[1:], op + ip[0])
    ps(ip[1:], op)

ps("abca", "")