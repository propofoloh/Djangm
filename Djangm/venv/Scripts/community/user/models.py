from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100, verbose_name='사용자명')
    useremail = models.EmailField(max_length=100, verbose_name='사용자이메일')
    password = models.CharField(max_length=100, verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

    def __str__(self): # 클래스가 문자열로 변환될 때 사용되는 내장함수
        return self.username


    class Meta:
        db_table = 'Community_user'
        verbose_name = '커뮤니티 사용자'
        verbose_name_plural = '커뮤니티 사용자' # 복수형 표현도 설정