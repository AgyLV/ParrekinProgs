import os
for file in os.listdir("C:\Users\agnese.veze\source\repos\ParrekinProgs"):
    if file.endswith(".txt"):
        print(os.path.join("C:\Users\agnese.veze\source\repos\ParrekinProgs", file))