from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home_page.html')


def count(request):
    fulltext = request.GET['fulltext']
    word_list = fulltext.split()
    word_count = len(word_list)
    word_repeat = {}

    for word in word_list:
        if word in word_repeat:
            word_repeat[word] += 1
        else:
            word_repeat[word] = 1
    for i, j in word_repeat.items():
        if j == (max(word_repeat.values())):
            max_repeat = i
    return render(request, 'count_page.html', {'fulltext': fulltext, 'word_count': word_count,
                                               'word_repeat': word_repeat, 'max_repeat': max_repeat})
def about(request):
    return render(request, 'about_page.html')

