from django.http import HttpResponse
from django.shortcuts import render, redirect
from apps import models
from apps.forms import *

def main(request):
    return render(request, 'main.html')

def survey(request):
    if request.method == 'POST': #페이지에 POST방식으로 요청할 때(=survey.html에서 form양식을 작성하고 submit했을 때)
        form = UsedCarForm(request.POST) # survey.html에서 form양식을 작성한 값들
        if form.is_valid(): #form양식을 작성한 값들이 형식(models.py에서 정한 형식. e.g., CharField(max_length))에 맞는지 check
            obj = UsedCar(accident_history = form.data['accident_history'], repair_history = form.data['repair_history'],manufacturer = form.data['manufacturer'])
            #obj이라는 변수에 form양식에 작성한 값들을 넣습니다.
            obj.save() #그리고 save합니다.
            return redirect('http://127.0.0.1:8000/') #데이터들은 DB에 저장이되고 화면은 메인페이지로 돌아갑니다.
        return HttpResponse('Failed. Try again.<br>' + 'Go back to the survey -> <a href = "survey">SURVEY</a>')
        #form값이 양식에 맞지 않으면 HttpResponse값이 화면에 출력됩니다.

    elif request.method == 'GET':
    #페이지에 GET방식으로 요청할 때(=메인 페이지의 survey를 눌렸을 때)는 그냥 survey.html템플릿을 return해줍니다.
        form = UsedCarForm()
        return render(request, 'survey.html')
    else:
        pass
