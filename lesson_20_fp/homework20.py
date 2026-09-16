salary = [30000, 45000, 28000, 60000, 52000, 33000]
new_salary = sum([n*1.1 for n in salary if (n * 1.1)  > 35000])
print(new_salary)


def unic_word(text):
    result = []
    text1 = text.lower().split()
    for i in text1:
        if len(i)>4:
            result.append(i) 
    new_text = sorted(result)
    return new_text
text = "Python це потужна мова програмування яка підходить для різних задач"
print(unic_word(text))           

