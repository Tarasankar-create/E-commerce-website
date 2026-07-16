from django.db import models

# Create your models here.
class Catagories(models.Model):
    name=models.CharField(primary_key=True,max_length=20)
    def __str__(self):
        return self.name
class homeSlider(models.Model):
    slide_url=models.ImageField(upload_to='images/',blank=True,null=True)
class homeContSlider1(models.Model):
    slide_url1=models.ImageField(upload_to='images/',blank=True,null=True)
class homeContSlider2(models.Model):
    name=models.ForeignKey(Catagories,on_delete=models.CASCADE)
    slide_url2=models.ImageField(upload_to='images/',blank=True,null=True)
    def __str__(self):
        return str(self.name)

class menSlider(models.Model):
    slide_url=models.ImageField(upload_to='images/',blank=True,null=True)
class menContent(models.Model):
    image_url=models.ImageField(upload_to='images/',blank=True,null=True)
    men_title=models.CharField(max_length=200)
    total=models.CharField(max_length=20)
    discount=models.IntegerField()
    dis_price=models.CharField(max_length=20)

class womenSlider(models.Model):
    slide_url=models.ImageField(upload_to='images/',blank=True,null=True)

class womenContent(models.Model):
    image_url=models.ImageField(upload_to='images/',blank=True,null=True)
    w_title=models.CharField(max_length=200)
    total=models.CharField(max_length=20)
    discount=models.IntegerField()
    dis_price=models.CharField(max_length=20)

class kidSlider(models.Model):
    slide_url=models.ImageField(upload_to='images/',blank=True,null=True)

class kidContent(models.Model):
    image_url=models.ImageField(upload_to='images/',blank=True,null=True)
    k_title=models.CharField(max_length=200)
    total=models.CharField(max_length=20)
    discount=models.IntegerField()
    dis_price=models.CharField(max_length=20)

class decorSlider(models.Model):
    slide_url=models.ImageField(upload_to='images/',blank=True,null=True)

class decorContent(models.Model):
    image_url=models.ImageField(upload_to='images/',blank=True,null=True)
    d_title=models.CharField(max_length=200)
    total=models.CharField(max_length=20)
    discount=models.IntegerField()
    dis_price=models.CharField(max_length=20)

class beautySlider(models.Model):
    slide_url=models.ImageField(upload_to='images/',blank=True,null=True)

class beautyContent(models.Model):
    image_url=models.ImageField(upload_to='images/',blank=True,null=True)
    b_title=models.CharField(max_length=200)
    total=models.CharField(max_length=20)
    discount=models.IntegerField()
    dis_price=models.CharField(max_length=20)

class electronicsSlider(models.Model):
    slide_url=models.ImageField(upload_to='images/',blank=True,null=True)
class electronicsContent(models.Model):
    image_url=models.ImageField(upload_to='images/',blank=True,null=True)
    e_title=models.CharField(max_length=200)
    total=models.CharField(max_length=20)
    discount=models.IntegerField()
    dis_price=models.CharField(max_length=20)

class mobileSlider(models.Model):
    slide_url=models.ImageField(upload_to='images/',blank=True,null=True)
class mobileContent(models.Model):
    image_url=models.ImageField(upload_to='images/',blank=True,null=True)
    m_title=models.CharField(max_length=200)
    total=models.CharField(max_length=20)
    discount=models.IntegerField()
    dis_price=models.CharField(max_length=20)

