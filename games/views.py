from django.shortcuts import render
from django.views.generic import TemplateView
import json
from django.http import JsonResponse

from games.models import GameScore
# Create your views here.

class HomeView(TemplateView):
    template_name = "home.html"


class MathGameView(TemplateView):
    template_name = "math-game.html"


class AnagramGameView(TemplateView):
    template_name = "anagram-game.html"


def record_score(request):
    data = json.loads(request.body)
    
    user_name = data["user-name"]
    game = data["game"]
    score = data["score"]
    
    new_score = GameScore(user_name = user_name, game = game, score = score)
    new_score.save()
    
    response = {
        "success": True
    }
    
    return JsonResponse(response)


class GameScoresView(TemplateView):
    template_name = "game-scores.html"
    
    def get_context_data(self, **kwargs):
        context = super(GameScoresView, self).get_context_data(**kwargs)
        context['anagram_scores'] = GameScore.objects.filter(game__exact='ANAGRAM').order_by('-score')
        context['math_scores'] = GameScore.objects.filter(game__exact='MATH').order_by('-score')
        return context

    """
    def get_context_data(self, **kwargs):
    Bu satır, get_context_data adlı bir metodu tanımlar. Bu metod, HTML şablonunun içeriğini oluşturmak için gereken bağlam (context) verilerini döndürmelidir.

    context = super(GameScoresView, self).get_context_data(**kwargs)
    Bu satır, üst sınıf olan TemplateView'ın get_context_data metodunu çağırarak temel bağlam verilerini alır.

    context['anagram_scores'] = GameScore.objects.filter(game__exact='ANAGRAM').order_by('-score')
    Bu satır, GameScore modelindeki 'ANAGRAM' oyununa ait skorları alır ve skorları puan sırasına göre büyükten küçüğe sıralar. Bu skorlar anagram_scores anahtarına bağlanarak bağlam verisine eklenir.

    context['math_scores'] = GameScore.objects.filter(game__exact='MATH').order_by('-score')
    Benzer şekilde, bu satır da 'MATH' oyununa ait skorları alır ve skorları puan sırasına göre büyükten küçüğe sıralar. Bu skorlar da math_scores anahtarına bağlanarak bağlam verisine eklenir.

    return context
    Bu satır, tüm bu bağlam verilerini içeren context sözlüğünü geri döndürür. Bu bağlam verileri, ilgili HTML şablonunun içinde kullanılabilir ve görüntülenen sayfanın içeriğini oluşturmak için kullanılır.
    """
