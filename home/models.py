from django.db import models

# Create your models here.
class menSlider(models.Model):
    id=models.IntegerField(primary_key=True,default=None)
    slide_url=models.URLField(max_length=2000)
class menContent(models.Model):
    id=models.IntegerField(primary_key=True,default=None)
    main_url=models.URLField(max_length=2000)
    image_url=models.URLField(max_length=1000)
    men_title=models.CharField(max_length=200)
    total=models.CharField(max_length=20)
    discount=models.IntegerField()
    dis_price=models.CharField(max_length=20)

class womenSlider(models.Model):
    id=models.IntegerField(primary_key=True,default=None)
    slide_url=models.URLField(max_length=2000)

class womenContent(models.Model):
    id=models.IntegerField(primary_key=True,default=None)
    main_url=models.URLField(max_length=2000)
    image_url=models.URLField(max_length=1000)
    w_title=models.CharField(max_length=200)
    total=models.CharField(max_length=20)
    discount=models.IntegerField()
    dis_price=models.CharField(max_length=20)

class kidSlider(models.Model):
    id=models.IntegerField(primary_key=True,default=None)
    slide_url=models.URLField(max_length=2000)

class kidContent(models.Model):
    id=models.IntegerField(primary_key=True,default=None)
    main_url=models.URLField(max_length=2000)
    image_url=models.URLField(max_length=1000)
    k_title=models.CharField(max_length=200)
    total=models.CharField(max_length=20)
    discount=models.IntegerField()
    dis_price=models.CharField(max_length=20)

class decorSlider(models.Model):
    id=models.IntegerField(primary_key=True,default=None)
    slide_url=models.URLField(max_length=2000)

class decorContent(models.Model):
    id=models.IntegerField(primary_key=True,default=None)
    main_url=models.URLField(max_length=2000)
    image_url=models.URLField(max_length=1000)
    d_title=models.CharField(max_length=200)
    total=models.CharField(max_length=20)
    discount=models.IntegerField()
    dis_price=models.CharField(max_length=20)

class beautySlider(models.Model):
    id=models.IntegerField(primary_key=True,default=None)
    slide_url=models.URLField(max_length=2000)

class beautyContent(models.Model):
    id=models.IntegerField(primary_key=True,default=None)
    main_url=models.URLField(max_length=2000)
    image_url=models.URLField(max_length=1000)
    b_title=models.CharField(max_length=200)
    total=models.CharField(max_length=20)
    discount=models.IntegerField()
    dis_price=models.CharField(max_length=20)

class electronicsSlider(models.Model):
    id=models.IntegerField(primary_key=True,default=None)
    slide_url=models.URLField(max_length=2000)
class electronicsContent(models.Model):
    id=models.IntegerField(primary_key=True,default=None)
    main_url=models.URLField(max_length=2000)
    image_url=models.URLField(max_length=1000)
    e_title=models.CharField(max_length=200)
    total=models.CharField(max_length=20)
    discount=models.IntegerField()
    dis_price=models.CharField(max_length=20)

class mobileSlider(models.Model):
    id=models.IntegerField(primary_key=True,default=None)
    slide_url=models.URLField(max_length=2000)

class mobileContent(models.Model):
    id=models.IntegerField(primary_key=True,default=None)
    main_url=models.URLField(max_length=2000)
    image_url=models.URLField(max_length=1000)
    m_title=models.CharField(max_length=200)
    total=models.CharField(max_length=20)
    discount=models.IntegerField()
    dis_price=models.CharField(max_length=20)

