""" 1. After flipping a coin 10 times you got this result,
    ```
    result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
    ```
    Using for loop figure out how many times you got heads  """

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count = 0
for i in result:
   if i == "heads":
      count = count+1

print(f"we got heads {count} times")      