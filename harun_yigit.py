def CTcalculator(list1):
    sum = 0
    mean=0
    mode=0
    for value in list1:
        sum += value
    mean = sum / len(list1)
    if len(list1) % 2 == 0:
        median = (list1[len(list1) // 2 - 1] + list1[
            (len(list1) // 2)]) / 2
    else:
        median = list1[((len(list1) + 1) // 2) - 1]
    max_count = 0
    for value2 in list1:
        count = list1.count(value2)
        if count > max_count:
            max_count = count
            mode = value2

    print("armean:",mean )
    print("median:",median)
    print("mode:" ,mode)


def file_to_list(file_name, list1):
    with open(file_name, "r") as file:
        for line in file:
            for word in line.split():
                try:
                    float_number = float(word)

                    list1.append(float_number)

                except:
                    pass


def list_to_file(file_name, list1):
    with open(file_name, "w") as file:
        for item in list1:
            file.write(str(item) + " ")


def summary():
    bilgiler = {"ad": "Harun", "soyad": "Yiğit", "numara": 211220029,
                "not": "Asla yanlış yapmamış insan, yeni hiç birşey denememiştir."}

    for key, value in bilgiler.items():
        print(key + ":", value)


summary()
