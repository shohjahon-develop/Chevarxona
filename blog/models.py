from django.db import models

# Create your models here.

class Bezaklarcategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Matocategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Mahsulotcategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Bezaklar(models.Model):
    category = models.ForeignKey(Bezaklarcategory,on_delete=models.CASCADE)
    color = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    soni = models.IntegerField()
    umumiynarx = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Mato(models.Model):
    category = models.ForeignKey(Matocategory,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    long = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    umumiynarx = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Mahsulotlar(models.Model):
    category = models.ForeignKey(Mahsulotcategory,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
 
    def __str__(self):
        return self.name


class Bezakkirim(models.Model):
    bezak_id = models.ForeignKey(Bezaklar,on_delete=models.CASCADE)
    soni = models.IntegerField(default=0)
    narxi = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    umumiynarx = models.CharField(max_length=100)

    def __str__(self):
        return str(self.date)

class Bezakchiqm(models.Model):
    bezak_id = models.ForeignKey(Bezaklar,on_delete=models.CASCADE)
    mahsulot_id = models.ForeignKey(Mahsulotlar,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True),
    soni = models.IntegerField(default=0)

    def __str__(self):
        return str(self.date)

class Matokrim(models.Model):
    mato_id = models.ForeignKey(Mato,on_delete=models.CASCADE)
    soni = models.IntegerField(default=0)
    narxi = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    umumiynarx = models.CharField(max_length=100)

    def __str__(self):
        return str(self.date)

class Matochiqim(models.Model):
    mato_id = models.ForeignKey(Mato,on_delete=models.CASCADE)
    mahsulot_id = models.ForeignKey(Mahsulotlar,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    soni = models.IntegerField(default=0)

    def __str__(self):
        return str(self.date)

class Mahsulotkirm(models.Model):
    bezaklar_id = models.ForeignKey(Bezaklar,on_delete=models.CASCADE)
    mato_id = models.ForeignKey(Mato,on_delete=models.CASCADE)
    soni = models.IntegerField(default=0)
    mahsulot_id = models.ForeignKey(Mahsulotlar,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.mahsulot_id)

class   Sotuv(models.Model):
    mahsulot_id = models.ForeignKey(Mahsulotlar,on_delete=models.CASCADE)
    soni = models.IntegerField(default=0)
    narxi = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.date)





class Accaount(models.Model):
    username = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    login = models.CharField(max_length=300)
    phonenumber = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=300)

    def __str__(self):
        return self.username

























































































