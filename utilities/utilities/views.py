# VIEWS MADE BY ME

from django.shortcuts import render


def index(request):

    return render(request, 'index.html')


def uforia(request):
    txt = (request.post.get('text1', 'off'))
    yourname = request.post.get('yourname', 'off')

    if yourname == "on":
        for char in txt:
            txt = txt + char.uppercase()

        a = {'name': txt}
        return render(request, 'index.html', a)


def jio(request):
    djtext = (request.POST.get('text', 'off'))

    removepunc = (request.POST.get('removepunc', 'off'))

    capital = (request.POST.get('capital', 'off'))

    newlineremover = request.POST.get('newlineremover', 'off')

    esr = request.POST.get('esr', 'off')

    charcounter = request.POST.get('charcounter', 'off')

    analyzed = ""

    params = {}

    if removepunc == "on":
        a = '''!@#$^%)(*}{][:;+=-"',>`/_><&"?|'''
        analyzed = ""
        for char in djtext:
            if char not in a:
                analyzed = analyzed + char

        djtext = analyzed
        params = {'purpose': 'Your Edit Is Ready-->', 'analyzed_text': analyzed}

    if capital == "on":
        analyzed = ""
        for char1 in djtext:
            analyzed = analyzed + char1.upper()

        djtext = analyzed
        params = {'purpose': 'Your Edit Is Ready-->', 'analyzed_text': analyzed}

    if newlineremover == "on":
        analyzed = " "
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        djtext = analyzed
        params = {'purpose': 'Your Edit Is Ready-->', 'analyzed_text': analyzed}

    if esr == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] != " ":
                analyzed = analyzed + char

        djtext = analyzed
        params = {'purpose': 'Your Edit Is Ready-->', 'analyzed_text': analyzed}

    if charcounter == "on":
        s = 0
        for char in djtext:
            if char != " " and char != "\n":
                s += 1

        params = {'purpose': 'Your Edit Is Ready-->', 'analyzed_text': analyzed, 'char': s}

    return render(request, 'analized.html', params)
