from django.db import models

# Create your models here.
class menSlider(models.Model):
    slide_url=models.URLField(primary_key=True,max_length=2000)
class menContent(models.Model):
    main_url=models.URLField(max_length=2000)
    image_url=models.URLField(primary_key=True,max_length=1000)
    men_title=models.CharField(max_length=60)
    total=models.IntegerField()
    discount=models.IntegerField()
    dis_price=models.IntegerField()

class womenSlider(models.Model):
    slide_url=models.URLField(primary_key=True,max_length=2000)

class womenContent(models.Model):
    main_url=models.URLField(max_length=2000)
    image_url=models.URLField(primary_key=True,max_length=1000)
    w_title=models.CharField(max_length=60)
    total=models.IntegerField()
    discount=models.IntegerField()
    dis_price=models.IntegerField()

class kidSlider(models.Model):
    slide_url=models.URLField(primary_key=True,max_length=2000)

class kidContent(models.Model):
    main_url=models.URLField(max_length=2000)
    image_url=models.URLField(primary_key=True,max_length=1000)
    k_title=models.CharField(max_length=60)
    total=models.IntegerField()
    discount=models.IntegerField()
    dis_price=models.IntegerField()

class decorSlider(models.Model):
    slide_url=models.URLField(primary_key=True,max_length=2000)

class decorContent(models.Model):
    main_url=models.URLField(max_length=2000)
    image_url=models.URLField(primary_key=True,max_length=1000)
    d_title=models.CharField(max_length=60)
    total=models.IntegerField()
    discount=models.IntegerField()
    dis_price=models.IntegerField()

class beautySlider(models.Model):
    slide_url=models.URLField(primary_key=True,max_length=2000)

class beautyContent(models.Model):
    main_url=models.URLField(max_length=2000)
    image_url=models.URLField(primary_key=True,max_length=1000)
    b_title=models.CharField(max_length=60)
    total=models.IntegerField()
    discount=models.IntegerField()
    dis_price=models.IntegerField()

class electronicsSlider(models.Model):
    slide_url=models.URLField(primary_key=True,max_length=2000)

class electronicsContent(models.Model):
    main_url=models.URLField(max_length=2000)
    image_url=models.URLField(primary_key=True,max_length=1000)
    e_title=models.CharField(max_length=60)
    total=models.IntegerField()
    discount=models.IntegerField()
    dis_price=models.IntegerField()

class mobileSlider(models.Model):
    slide_url=models.URLField(primary_key=True,max_length=2000)

class mobileContent(models.Model):
    main_url=models.URLField(max_length=2000)
    image_url=models.URLField(primary_key=True,max_length=1000)
    m_title=models.CharField(max_length=60)
    total=models.IntegerField()
    discount=models.IntegerField()
    dis_price=models.IntegerField()

