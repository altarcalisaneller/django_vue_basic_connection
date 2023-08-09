from django.db import models

# Create your models here.
class GameScore(models.Model):
    MATH = "MATH"
    ANAGRAM = "ANAGRAM"
    
    GAME_CHOICES = [
        (MATH, "Math Game"),
        (ANAGRAM, "Anagram Game")
    ]
    
    user_name = models.TextField()
    game = models.TextField(choices=GAME_CHOICES, default=MATH)
    score = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)


    """
    auto_now_add seçeneği, bir nesne (örneğin, bir veritabanı kaydı) oluşturulduğunda, belirtilen alanın o anki tarih ve saati ile doldurulmasını sağlar. Yani bu alanı sadece bir nesne oluşturulduğunda değiştirebilirsiniz. Bir nesne güncellendiğinde bu alan güncellenmez. Bu özellik, genellikle yaratılma tarihini veya başka bir zaman damgasını tutmak için kullanılır.
    
    auto_now seçeneği, bir nesne her kaydedildiğinde (oluşturulduğunda veya güncellendiğinde) belirtilen alanın o anki tarih ve saati ile doldurulmasını sağlar. Bu nedenle, bir nesne kaydedildiğinde bu alan her zaman güncellenir. Bu seçenek genellikle nesnenin son güncellenme tarihini tutmak için kullanılır.
    
    Özetle, auto_now_add sadece nesne yaratıldığında bir kez çalışırken (INSERT işlemi sırasında), auto_now her kaydetme işlemi (INSERT veya UPDATE) sırasında çalışır.
    
    """
    
   
    