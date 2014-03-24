# coding: utf-8

fname = "py_task_2_3.txt"
word = "Django"
count_word, count_symb = 0, 0
problem_char = {'{': '{{', '}': '}}'}
f = open(fname)
fs = open("shablon_" + fname, "w")
fr = open("formatted_" + fname, "w")
for line in f.xreadlines():
    for i in problem_char:
        line = line.replace(i, problem_char[i])
    text = line.replace("Django", "{0}")
    text_f = text.format("Django 1.6")
    fs.write(text)
    fr.write(text_f)
    count_word += line.count(word)
    if line.rstrip().endswith(":"):
        count_symb += 1
f.close()
fs.close()
fr.close()
print word, "встречается", count_word, "раз(а). Символом ':' заканчиваются", count_symb, "строки."
