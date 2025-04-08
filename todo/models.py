#Data Base 관련 설정 class는 필드 설정
#migrations.py 실행을 하면 python -> SQL 문으로 변경
#cmd: python mange.py makemigrations / add
#cmd: python mange.py migrate / DB에 생성
#admin.py로 이동 -> Rauting

from django.db import models

class Todo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    complete = models.BooleanField(default=False)
    exp = models.PositiveIntegerField(default=0)
    complete_at = models.DateTimeField(null=True, blank= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self): # 매서드는 __str__ 필요
        return self.name