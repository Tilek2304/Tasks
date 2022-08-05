"""
Дан список, содержащий в себе строки из нескольких слов. Нужно найти самое длинное слово из всех переданных строк

Например:
    in: [‘я любуюсь миром’, ‘лежу на боку’]
    out: ‘любуюсь’
"""
max_num = 0
dict_ = {}
list_ = ["я любуюсь миром", "лежу на боку"]
num_list = []
for i in list_:
    words = i.split()
    for word in words:
        if len(word)>max_num:
            dict_.clear()
            max_num = len(word)
            dict_[word] = max_num
print(dict_)

        
        

