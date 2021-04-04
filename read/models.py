from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length = 40, verbose_name = '课程名')
    about = models.CharField(max_length = 1000, default='', blank=True,
        null=True, verbose_name='课程描述')
    leibie = models.CharField(max_length = 40, verbose_name='课程类别')


    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Maker(models.Model):
    name = models.CharField(max_length = 40, verbose_name = '制作者')
    school = models.CharField(max_length = 40, default='', blank=True,
        null=True, verbose_name='所属学校')

    class Meta:
        verbose_name = '制作者'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Chapter(models.Model):
    name = models.CharField(max_length = 40, verbose_name = '章节名')
    about = models.CharField(max_length = 1000, default='', blank=True,
        null=True, verbose_name='章节描述')
    text = models.TextField(verbose_name='章节文本')
    link = models.TextField(default='', blank=True,
        null=True, verbose_name='章节链接')
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    maker = models.ForeignKey(Maker, on_delete = models.CASCADE)
    img = models.ImageField(upload_to='img', verbose_name='思维导图')
    img_name = models.CharField(max_length = 40,  default='', blank=True,
        null=True, verbose_name='导图名')

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Img(models.Model):
    img = models.ImageField(upload_to='img', verbose_name='图像')
    name = models.CharField(max_length = 40,  default='', blank=True,
        null=True, verbose_name='图像名')
   
    class Meta:
        verbose_name = '图像'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

