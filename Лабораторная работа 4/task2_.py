def get_count_char(str_):
    str_ = str_.lower()
    dict_ = {}
    for char in str_:
        if char.isalpha():
            dict_.setdefault(char, str_.count(char))
    return dict_

def get_procent_count_char(dict_):
    procent_dict = {}
    for char, value in dict_.items():
        procent_dict.setdefault(char, round(value / sum(dict_.values()) * 100, 2))
    return procent_dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
dict_2 = get_count_char(main_str)

print(dict_2)

