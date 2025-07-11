from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse
from .forms import UploadFileForm
from .models import Page
import random


# Create your views here.
class IndexView(View):
    def get(self, request):
        return render(request, "main/index.html")


class RegistrationQuiz(View):
    def get(self, request):
        registration = UploadFileForm()
        return render(
            request, "main/registration_quiz.html", {"registration": registration}
        )

    def post(self, request):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("quiz_app:index")
        return render(request, "main/registration_quiz.html", {"form": form})


class QuizList(View):
    def get(self, request):
        page_list = Page.objects.all()
        return render(request, "main/quiz_list.html", {"page_list": page_list})


class QuizDetail(View):
    def get(self, request, id):
        quiz = get_object_or_404(Page, id=id)
        return render(request, "main/quiz_detail.html", {"quiz": quiz})


class Quiz(View):
    def get(self, request):
        # 初めてのアクセス時、セッション内に'displayed_data'キーが存在しない場合は空のリストを作成
        if "displayed_data" not in request.session:
            request.session["displayed_data"] = []

        # URLのクエリパラメータに'change_data'が含まれているかをチェック
        if 'change_data' in request.GET:
            # セッションのランダムデータをリセット
            if 'random_data' in request.session:
                del request.session['random_data']
            # セッションに'change_data'フラグを設定
            request.session['change_data_flag'] = True
            # クエリパラメータをとり沿いたURLにリダイレクト
            return redirect(reverse('quiz_app:quiz'))
        
        # 'change_data_flag'がセッション内に存在する場合、新しいデータをDBから取得
        if 'change_data_flag' in request.session:
            del request.session['change_data_flag']
            # 引き出すデータは、既に表示したデータID以外を取得
            all_data = list(
                Page.objects.exclude(id__in=request.session["displayed_data"])
            )
            # all_data = []
            if all_data:
                random_data = random.choice(all_data)
                request.session["displayed_data"].append(str(random_data.id))
                request.session["random_data"] = {
                    "source": random_data.source,
                    "source_text": random_data.source_text,
                    "quiz_text": random_data.quiz_text,
                    "correct": random_data.correct,
                    "incorrect_1": random_data.incorrect_1,
                    "incorrect_2": random_data.incorrect_2,
                }
            else:
                return redirect(reverse('quiz_app:quiz_result'))
        else:
            # セッション内に'random_data'が存在しない場合、新しいデータを取得
            if "random_data" not in request.session:
                all_data = list(
                    Page.objects.exclude(id__in=request.session["displayed_data"])
                )
                if all_data:
                    random_data = random.choice(all_data)
                    request.session["displayed_data"].append(str(random_data.id))
                    request.session["random_data"] = {
                        "source": random_data.source,
                        "source_text": random_data.source_text,
                        "quiz_text": random_data.quiz_text,
                        "correct": random_data.correct,
                        "incorrect_1": random_data.incorrect_1,
                        "incorrect_2": random_data.incorrect_2,
                    }
                else:
                    return redirect(reverse('quiz_app:result'))
            else:
                # セッションからデータを取得
                random_data = request.session["random_data"]

        return render(request, "main/quiz01.html", {"data": random_data})
    
class QuizResult(View):
    def get(self, request):
        return render(request, 'main/quiz_result.html')


class QuizUpdate(View):
    def get(self, request, id):
        page = get_object_or_404(Page, id=id)
        form = UploadFileForm(instance=page)
        return render(request, "main/quiz_update.html", {"form": form})

    def post(self, request, id):
        page = get_object_or_404(Page, id=id)
        form = UploadFileForm(request.POST, request.FILES, instance=page)
        if form.is_valid():
            form.save()
            return redirect("quiz_app:quiz_detail", id=id)
        return render(request, "main/quiz_detail.html", {"form": form})


index = IndexView.as_view()
registration = RegistrationQuiz.as_view()
page_list = QuizList.as_view()
quiz_detail = QuizDetail.as_view()
quiz = Quiz.as_view()
quiz_result  = QuizResult.as_view()
quiz_update = QuizUpdate.as_view()