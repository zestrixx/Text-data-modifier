# this file is created by me-mayank
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    capfirst = request.POST.get('capfirst', 'off')
    extraspacerem = request.POST.get('extraspacerem', 'off')
    wordcount = request.POST.get('wordcount', 'off')

    if removepunc=='on':
        analyzedch = ""
        punc=''',:'".?/\!@#{}[]()*+-_;=<>|$%^&'''
        for char in djtext:
            if char not in punc:
                analyzedch+=char
        params = {'purpose': 'Removed Punctuations', 'analyzed': analyzedch}
        djtext=analyzedch

    if capfirst=='on':
        analyzedch = ''
        for char in djtext:
            analyzedch += char.upper()
        params = {'purpose': 'Changed To UpperCase', 'analyzed': analyzedch}
        djtext=analyzedch

    if extraspacerem=='on':
        analyzedch = ''
        for i, char in enumerate(djtext):
            if not(djtext[i]==' ' and djtext[i+1]==' '):
                analyzedch += char
        params = {'purpose': 'Removed Extra Spaces', 'analyzed': analyzedch}
        djtext=analyzedch

    if wordcount=='on':
        count = 0
        for word in djtext.split():
            count += 1
        params = {'purpose': 'Total Words', 'analyzed': count}
        djtext=count

    if (wordcount!='on' and removepunc!="on" and extraspacerem!="on" and capfirst!="on"):
        return HttpResponse('Error')
    
    return render(request, 'analyze.html', params)

def fet(request):
    return render(request, 'feature.html')

    
def othserv(request):
    return render(request, 'OtherServices.html')

