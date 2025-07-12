marks = [20,2,3,6,45,85,96,74,10,25,85,32,30,25]
highest = marks[0]

for i in marks:
    print(i)
    if i > highest:
        highest = i


print("Current highest mark:", highest)

#printing was done like print stmt using the \n character
#user input ishtey ilaa untundhi, kindha unnattu
marks1 = [(input())]    #maname discover chesamu. input ilaaga ivvali ani

lowest = marks1[0]
for i in marks1:
    if i < lowest:
        lowest = i

print("Current lowest mark:", lowest)

#manaki max function kooda undhandoi!! simple ga aipothundhi dhaanitho aithey

m = [52,59,58,57,45,51,25,93,53,62]
print(max(m))


#manaki min function kooda undhandoi!! simple ga aipothundhi dhaanitho aithey
print(min(m))
