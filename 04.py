with open('04.in') as f:
    pairs = [[int(y) for y in x.replace(',','-').split('-')] for x in f.read().split('\n')]
    print(sum([a<=c<=d<=b or c<=a<=b<=d for a,b,c,d in pairs]))
    print(sum([a<=c<=b or a<=d<=b or c<=a<=d or c<=b<=d for a,b,c,d in pairs]))