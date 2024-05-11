#MIT License

#Copyright (c) 2023 Golovanov Grigoriy
#Contact e-mail: magentrum@gmail.com

# Библиотека расчета вероятностей
from scipy import stats

# Библиотека рисования графиков
import matplotlib.pyplot as plt

# Библиотека работы с файлами
import os

data=[]
# Загрузка файла с подсчетом количества аспектов
fileName = open("../probability/3.60.4_1000", 'r')
for l in fileName:
    l=int(l.rstrip())
    data.append(l)
    
# Установка параметров расчета вероятностей (матожидание (среднее знаение)=85.2, стандартное отклонение (сигма)=8.1)
calc_rp = stats.norm(loc=85.2, scale=8.1)
# Расчет вероятности события
calc_rp.pdf(105)
# Данные для графика
pdf = calc_rp.pdf(data)
# Параметры графика
plt.bar(data, pdf, color='darkblue')
# Подписи под осями
plt.ylabel('$f(x)$')
plt.xlabel('$x$')
# Рисуем пунктирную линию
plt.axvline(105, color='red', linestyle='--', lw=2); 
# Метка
plt.text(105, -0.003, '105', rotation=0, color='red') 
