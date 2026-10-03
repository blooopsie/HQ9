'''
HQ9+ interpreter in Python
'''
n = input()
acc = 0
for x in n:
    if x == "H":
        print("Hello, World!")
    elif x == "Q":
        print(n)
    elif x == "9":
        t = []
        for i in range(3, 100):
            t.append(i)
        for i in t[::-1]:
            print(f"{i} bottles of beer on the wall\n{i} bottles of beer\nTake one down, pass it around\n{i - 1} bottles of beer on the wall\n")
        print("2 bottles of beer on the wall\n2 bottles of beer\nTake one down, pass it around\n1 bottle of beer on the wall\n\n1 bottles of beer on the wall\n1 bottles of beer\nTake one down, pass it around\nNo bottles of beer on the wall\n\nNo bottles of beer on the wall\nNo bottles of beer\nGo to the store, buy some more\n99 bottles of beer on the wall")
    elif x == "+":
        acc += 1
    else:
        pass
