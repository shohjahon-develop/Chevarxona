from django.core.exceptions import ValidationError
from rest_framework import serializers

from blog.models import (Mato, Bezaklar, Bezaklarcategory, Bezakkirim,
                         Bezakchiqm, Matocategory, Matokrim, Matochiqim,
                         Mahsulotkirm, Mahsulotcategory, Mahsulotlar, Sotuv, Accaount)


class AccaountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accaount
        fields = "__all__"

    def validate(self,data):
        username = data.get('name',None)
        email = data.get('email',None)


        Kattaharf=False
        for x in username:
            code = ord(x)
            if (code >=65 and code <=90 or (code == 32)):
                Kattaharf=True
        if (Kattaharf):
            raise ValidationError({
                "status":False,
                "message":"Katta harif va bo'sh joy bo'lishi mumkin emas"
            })








        if Accaount.objects.filter(username=username,email=email).exists():
            raise ValidationError(
                {
                    'status': False,
                    "xabar": "Username va email qaytarilishi  mumkin emas"
                }
            )
        return data
class BezaklarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bezaklar
        fields = "__all__"

    def validate(self,data):
        name = data.get('name',None)
        code = data.get('code',None)
        umumiynarx = data.get('umumiynarx',None)

        if not (int(umumiynarx) > 0 and int(umumiynarx) < 5000000):
            raise ValidationError({
                "status":False,
                "natija":"Umumiynarx 0 dan katta 5 000 000 dan kichik bo'lishi kerak"
            })

        if not (name.isalpha() ):
            raise ValidationError({
                "status":False,
                "natija":"Name  da raqam qatnashmasligi kerak"
            })

        if not (code.isnumeric()):
            raise ValidationError({
                'status':False,
                'natija':"Code da faqat raqamalr qatnashishi kerak"
            })
        return data




class BezakkirimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bezakkirim
        fields = "__all__"

    def validate(self,data):
        soni = data.get('soni',None)

        if not (int(soni) > 0 and int(soni) <= 2000):
            raise ValidationError({
                "status":False,
                "natija":"Bezaklarni soni o dan ko'p 2000 tadan kam bo'lishi kerak"
            })
        return data


class BezakchiqmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bezakchiqm
        fields = "__all__"

    def validate(self, data):
        soni = data.get('soni', None)

        if not (int(soni) > 0 and int(soni) <= 2000):
            raise ValidationError({
                "status": False,
                "natija": "Bezaklarni soni o dan ko'p 2000 tadan kam bo'lishi kerak"
            })
        return data





class MatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mato
        fields = "__all__"

    def validate(self,data):
        name = data.get('name',None)
        code = data.get('code',None)
        long = data.get('long',None)

        if not (int(long) >= 0 and int(long) <= 1000):
            raise ValidationError({
                'status':False,
                "natija":"Mato uzunligi 0 dan katta va 1000 dan kichik bo'lishi kerak"
            })

        if not (name.isalpha() ):
            raise ValidationError({
                "status":False,
                "natija":"Name  da raqam qatnashmasligi kerak"
            })

        if not (code.isnumeric()):
            raise ValidationError({
                'status':False,
                'natija':"Code da faqat raqamalr qatnashishi kerak"
            })
        return data








class MatochiqimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matochiqim
        fields = "__all__"

    def validate(self,data):
        long = data.get('long',None)

        if not (int(long) > 0 and int(long) <=5):
            raise ValidationError({
                "status":False,
                "natija":"Mato uzunligi 0 metrdan katta 5 metrdan kichik bo'lishi kerak"
            })
        return data


class MatokrimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matokrim
        fields = "__all__"

    def validate(self,data):
        long = data.get('long',None)

        if not (int(long)>0 and int(long)<=1000):
            raise ValidationError({
                'status':False,
                "natija":"Mato 0 dan ko'p 1000 metrdan kichik bo'lishi kerak"
            })
        return data


class MahsulotlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahsulotlar
        fields = "__all__"

    def validate(self,data):
        name = data.get('name',None)
        code = data.get('code',None)

        if not (name.isalpha() ):
            raise ValidationError({
                "status":False,
                "natija":"Name  da raqam qatnashmasligi kerak"
            })

        if not (code.isnumeric()):
            raise ValidationError({
                'status':False,
                'natija':"Code da faqat raqamalr qatnashishi kerak"
            })
        return data

class MahsulotkirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahsulotkirm
        fields = "__all__"

    def validate(self,data):
        soni = data.get('soni',None)

        if not(int(soni) >=10):
            raise ValidationError({
                'status':False,
                "natija":"Mahsulotlar 10 tadan ko'p bo'lishi kerak"
            })
        return data



class SotuvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sotuv
        fields = "__all__"

    def validate(self,data):
        soni = data.get('soni',None)

        if not(int(soni) >= 100 and soni.isnumeric()):
            raise ValidationError({
                "status":False,
                'message':"Sotilgan mahsulotlar 100 tadan ko'p bo'lishi kerak"
            })
        return data


















































































































