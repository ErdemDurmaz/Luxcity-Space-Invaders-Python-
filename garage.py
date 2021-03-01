#
# Implement function four_letters
#
names = "Trorr Gvigris Deriana Nori"
def four_letters(names):
    count = 0
    separated = names.split(" ")
    for letter in separated:
        if len(letter) == 4:
            count +=1
    print(count)
four_letters(names)