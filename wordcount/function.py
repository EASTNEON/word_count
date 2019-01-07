# from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def count(request):
    user_text = request.GET['text']
    total_count = len(request.GET['text'])

    word_dict = {}

    for word in user_text:  # 遍历 统计每个字符出现的次数
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    sorted_dict =\
        sorted(word_dict.items(), key=lambda w: w[1], reverse=True)
        # 可迭代对象
        # 排序 选取第一个参数作为排序的标准 如(a,b)则选择b
        # True降序 False 升序     

    # 通过字典（{}中内容）传递信息
    return render(request, 'count.html',
                  {'count': total_count, 'text': user_text, 
                  'worddict': word_dict, 'sorted': sorted_dict})
