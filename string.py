word = input("Enter word: ")
i = int(input("Enter index: "))
n = int(input("Enter step: "))

word = word[:i:n].capitalize()
print(word)

sym = input("Enter symbol: ")
print("At index: ", word.find(sym))

sym = input("Enter new symbol: ")
list = word.split(sym)
print("List: ", list)
