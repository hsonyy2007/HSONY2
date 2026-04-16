import itertools

data = ["Ali", "!", "Mustafa", "1980", "Messi","Ahmed", "Nissan", "Siri" , "_" , "#" , "@"]

data = list(set(data))  
limit = 100000
count = 0   
with open("password.txt", "w", encoding="utf-8") as file:
    for i in [3, 4, 5]:
        for j in itertools.permutations(data, i):
            file.write("".join(j) + "\n")
            count += 1
            if count >= limit:
                break
            if count >= limit:
                break
