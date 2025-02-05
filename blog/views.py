from django.http import Http404
from django.shortcuts import render
from rest_framework.response import  Response

# Create your views here.
from .serializers import (BezakchiqmSerializer,BezakkirimSerializer,
                          BezaklarSerializer,MahsulotkirmSerializer,
                          MahsulotlarSerializer,MatochiqimSerializer,
                          MatokrimSerializer,MatoSerializer,SotuvSerializer)

from .models import (Bezaklar,Bezakkirim,Bezakchiqm,
                     Matokrim,Matochiqim,Mahsulotkirm,
                     Mahsulotlar,Mato,Sotuv)
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication




class BezakRoyxatView(APIView):

    def get(self, request):

        bezak = Bezaklar.objects.all()
        bezak = BezaklarSerializer(bezak, many=True).data
        return Response(bezak)

    def post(self, request):
            bezak = BezaklarSerializer(data=request.data)
            if bezak.is_valid():
                bezak.save()
                return Response(bezak.data, status=status.HTTP_201_CREATED)
            return Response(bezak.errors, status=status.HTTP_400_BAD_REQUEST)



class BezaklarDetailAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    def get_object(self, pk):
        try:
            return Bezaklar.objects.get(pk=pk)
        except Bezaklar.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        bezak = self.get_object(pk)
        serializer = BezaklarSerializer(bezak).data
        data = {
            "natija": serializer
        }

        return Response(data)

    def put(self,request,pk):
        bezak = self.get_object(pk)
        serializer = BezaklarSerializer(bezak,data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "status":f"{bezak.name} o'zgartirildi",
                "result":serializer.data
            }
            return Response(data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk):
        bezak = self.get_object(pk)

        data = {
                "xabar":f"{bezak.name}ning malumotlari o'chirildi."
        }
        bezak.delete()
        return Response(data)

# ////////////////////////////////////////////////////////////////////////////////////////

class MatoRoyxatView(APIView):

    def get(self, request):

        mato = Mato.objects.all()
        mato = MatoSerializer(mato, many=True).data
        return Response(mato)

    def post(self, request):
            mato = MatoSerializer(data=request.data)
            if mato.is_valid():
                mato.save()
                return Response(mato.data, status=status.HTTP_201_CREATED)
            return Response(mato.errors, status=status.HTTP_400_BAD_REQUEST)



class MatoDetailAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    def get_object(self, pk):
        try:
            return Mato.objects.get(pk=pk)
        except Mato.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        mato = self.get_object(pk)
        serializer = MatoSerializer(mato).data
        data = {
            "natija": serializer
        }

        return Response(data)

    def put(self,request,pk):
        mato = self.get_object(pk)
        serializer = MatoSerializer(mato,data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "status":f"{mato.name} o'zgartirildi",
                "result":serializer.data
            }
            return Response(data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk):
        mato = self.get_object(pk)

        data = {
                "xabar":f"{mato.name}ning malumotlari o'chirildi."
        }
        mato.delete()
        return Response(data)


# ////////////////////////////////////////////////////////////////////////////////////////////////

class MahsulotlarRoyxatView(APIView):

    def get(self, request):

        mahsulot = Mahsulotlar.objects.all()
        mahsulot = MahsulotlarSerializer(mahsulot, many=True).data
        return Response(mahsulot)

    def post(self, request):
            mahsulot = MahsulotlarSerializer(data=request.data)
            if mahsulot.is_valid():
                mahsulot.save()
                return Response(mahsulot.data, status=status.HTTP_201_CREATED)
            return Response(mahsulot.errors, status=status.HTTP_400_BAD_REQUEST)



class MahsulotlarDetailAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    def get_object(self, pk):
        try:
            return Mahsulotlar.objects.get(pk=pk)
        except Mahsulotlar.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        mahsulot = self.get_object(pk)
        serializer = MahsulotlarSerializer(mahsulot).data
        data = {
            "natija": serializer
        }

        return Response(data)

    def put(self,request,pk):
        mahsulot = self.get_object(pk)
        serializer = MahsulotlarSerializer(mahsulot,data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "status":f"{mahsulot.name} o'zgartirildi",
                "result":serializer.data
            }
            return Response(data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk):
        mahsulot = self.get_object(pk)

        data = {
                "xabar":f"{mahsulot.name}ning malumotlari o'chirildi."
        }
        mahsulot.delete()
        return Response(data)


# ////////////////////////////////////////////////////////////////////////////////////////////


class BezakchqimRoyxatView(APIView):

    def get(self, request):

        bezakchiqm = Bezakchiqm.objects.all()
        bezakchiqm = BezakchiqmSerializer(bezakchiqm, many=True).data
        return Response(bezakchiqm)

    def post(self, request):
            bezakchiqm = BezakchiqmSerializer(data=request.data)
            if bezakchiqm.is_valid():
                bezakchiqm.save()
                return Response(bezakchiqm.data, status=status.HTTP_201_CREATED)
            return Response(bezakchiqm.errors, status=status.HTTP_400_BAD_REQUEST)



class BezakchiqmDetailAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    def get_object(self, pk):
        try:
            return Bezakchiqm.objects.get(pk=pk)
        except Bezakchiqm.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        bezakchiqm = self.get_object(pk)
        serializer = BezakchiqmSerializer(bezakchiqm).data
        data = {
            "natija": serializer
        }

        return Response(data)

    def put(self,request,pk):
        bezakchiqm = self.get_object(pk)
        serializer = BezakchiqmSerializer(bezakchiqm,data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "status":f"{bezakchiqm.name} o'zgartirildi",
                "result":serializer.data
            }
            return Response(data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk):
        bezakchiqm = self.get_object(pk)

        data = {
                "xabar":f"{bezakchiqm.bezak_id} malumotlari o'chirildi."
        }
        bezakchiqm.delete()
        return Response(data)


# ///////////////////////////////////////////////////////////////////////////////////////////


class BezakkirimRoyxatView(APIView):

    def get(self, request):

        bezakkirm = Bezakkirim.objects.all()
        bezakkirm = BezakkirimSerializer(bezakkirm, many=True).data
        return Response(bezakkirm)

    def post(self, request):
            bezakkirm = BezakkirimSerializer(data=request.data)
            if bezakkirm.is_valid():
                bezakkirm.save()
                return Response(bezakkirm.data, status=status.HTTP_201_CREATED)
            return Response(bezakkirm.errors, status=status.HTTP_400_BAD_REQUEST)



class BezakkirmDetailAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    def get_object(self, pk):
        try:
            return Bezakkirim.objects.get(pk=pk)
        except Bezakkirim.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        bezakkirm = self.get_object(pk)
        serializer = BezakkirimSerializer(bezakkirm).data
        data = {
            "natija": serializer
        }

        return Response(data)

    def put(self,request,pk):
        bezakkirm = self.get_object(pk)
        serializer = BezakkirimSerializer(bezakkirm,data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "status":f"{bezakkirm.name} o'zgartirildi",
                "result":serializer.data
            }
            return Response(data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk):
        bezakkirm = self.get_object(pk)

        data = {
                "xabar":f"{bezakkirm.bezak_id} malumotlari o'chirildi."
        }
        bezakkirm.delete()
        return Response(data)

# /////////////////////////////////////////////////////////////////////////////////////
class MatokirimRoyxatView(APIView):

    def get(self, request):

        matokrim = Matokrim.objects.all()
        matokrim = MatokrimSerializer(matokrim, many=True).data
        return Response(matokrim)

    def post(self, request):
            matokrim = MatokrimSerializer(data=request.data)
            if matokrim.is_valid():
                matokrim.save()
                return Response(matokrim.data, status=status.HTTP_201_CREATED)
            return Response(matokrim.errors, status=status.HTTP_400_BAD_REQUEST)



class MatokrimDetailAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    def get_object(self, pk):
        try:
            return Matokrim.objects.get(pk=pk)
        except Matokrim.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        matokrim = self.get_object(pk)
        serializer = MatokrimSerializer(matokrim).data
        data = {
            "natija": serializer
        }

        return Response(data)

    def put(self,request,pk):
        matokrim = self.get_object(pk)
        serializer = MatokrimSerializer(matokrim,data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "status":f"{matokrim.name} o'zgartirildi",
                "result":serializer.data
            }
            return Response(data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk):
        matokrim = self.get_object(pk)

        data = {
                "xabar":f"{matokrim.name}ning malumotlari o'chirildi."
        }
        matokrim.delete()
        return Response(data)


# /////////////////////////////////////////////////////////////////////////////////////////////


class MatochqimRoyxatView(APIView):

    def get(self, request):

        matochqim = Matochiqim.objects.all()
        matochqim = MatochiqimSerializer(matochqim, many=True).data
        return Response(matochqim)

    def post(self, request):
            matochqim = MatochiqimSerializer(data=request.data)
            if matochqim.is_valid():
                matochqim.save()
                return Response(matochqim.data, status=status.HTTP_201_CREATED)
            return Response(matochqim.errors, status=status.HTTP_400_BAD_REQUEST)



class MatochqimDetailAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    def get_object(self, pk):
        try:
            return Matochiqim.objects.get(pk=pk)
        except Matochiqim.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        matochqim = self.get_object(pk)
        serializer = MatochiqimSerializer(matochqim).data
        data = {
            "natija": serializer
        }

        return Response(data)

    def put(self,request,pk):
        matochqim = self.get_object(pk)
        serializer = MatochiqimSerializer(matochqim,data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "status":f"{matochqim.name} o'zgartirildi",
                "result":serializer.data
            }
            return Response(data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk):
        matochqim = self.get_object(pk)

        data = {
                "xabar":f"{matochqim.name}ning malumotlari o'chirildi."
        }
        matochqim.delete()
        return Response(data)


# //////////////////////////////////////////////////////////////////////////


class MahsulotkrimRoyxatView(APIView):

    def get(self, request):

        mahsulotkrim = Mahsulotkirm.objects.all()
        mahsulotkrim = MatochiqimSerializer(mahsulotkrim, many=True).data
        return Response(mahsulotkrim)

    def post(self, request):
            mahsulotkrim = MahsulotkirmSerializer(data=request.data)
            if mahsulotkrim.is_valid():
                mahsulotkrim.save()
                return Response(mahsulotkrim.data, status=status.HTTP_201_CREATED)
            return Response(mahsulotkrim.errors, status=status.HTTP_400_BAD_REQUEST)



class MahsulotkrimDetailAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    def get_object(self, pk):
        try:
            return Mahsulotkirm.objects.get(pk=pk)
        except Mahsulotkirm.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        mahsulotkrim = self.get_object(pk)
        serializer = MahsulotkirmSerializer(mahsulotkrim).data
        data = {
            "natija": serializer
        }

        return Response(data)

    def put(self,request,pk):
        mahsulotkrim = self.get_object(pk)
        serializer = MahsulotkirmSerializer(mahsulotkrim,data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "status":f"{mahsulotkrim.name} o'zgartirildi",
                "result":serializer.data
            }
            return Response(data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk):
        mahsulotkrim = self.get_object(pk)

        data = {
                "xabar":f"{mahsulotkrim.name}ning malumotlari o'chirildi."
        }
        mahsulotkrim.delete()
        return Response(data)

# //////////////////////////////////////////////////////////


class SotuvRoyxatView(APIView):

    def get(self, request):

        sotuv = Sotuv.objects.all()
        sotuv = SotuvSerializer(sotuv, many=True).data
        return Response(sotuv)

    def post(self, request):
            sotuv = SotuvSerializer(data=request.data)
            if sotuv.is_valid():
                sotuv.save()
                return Response(sotuv.data, status=status.HTTP_201_CREATED)
            return Response(sotuv.errors, status=status.HTTP_400_BAD_REQUEST)



class SotuvDetailAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    def get_object(self, pk):
        try:
            return Sotuv.objects.get(pk=pk)
        except Sotuv.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        sotuv = self.get_object(pk)
        serializer = SotuvSerializer(sotuv).data

        data = {
            "natija": serializer
        }

        return Response(data)

    def put(self,request,pk):
        sotuv = self.get_object(pk)
        serializer = SotuvSerializer(sotuv,data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "status":f"{sotuv.name} o'zgartirildi",
                "result":serializer.data
            }
            return Response(data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk):
        sotuv = self.get_object(pk)

        data = {
                "xabar":f"{sotuv.name}ning malumotlari o'chirildi."
        }
        sotuv.delete()
        return Response(data)





class MatoNewApi(APIView):
    def get_object(self, pk):
        try:
            return Mato.objects.get(pk=pk)
        except Mato.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        mato = self.get_object(pk)
        serializer = MatoSerializer(mato).data
        data = {
            "natija": serializer

        }
        return Response(data)























































































































































































