from rest_framework.response import Response
from rest_framework.views import APIView

from store.models import User, Product, ProductCategory, Basket
from store.serializers import UserSerializer, ProductSerializer, ProductCategorySerializer, BasketSerializer


class UserListAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(data=serializer.data)


class UserAPIView(APIView):
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(data=serializer.data)

    def post(self, request):
        user = UserSerializer(data=request.data)
        if user.is_valid(raise_exception=True):
            user.save()
        return Response(status=201)

    def put(self, request, pk):
        try:
            instance = User.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = UserSerializer(data=request.data, instance=instance)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({"user": serializer.data})

    def delete(self, request, pk):
        try:
            User.objects.filter(pk=pk).delete()
        except:
            return Response({"error": "Object does not exists"})
        return Response(status=200)


class ProductCategoryListAPIView(APIView):
    def get(self, request):
        categories = ProductCategory.objects.all()
        serializer = ProductCategorySerializer(categories, many=True)
        return Response(data=serializer.data)


class ProductCategoryAPIView(APIView):
    def get(self, request, pk):
        category = ProductCategory.objects.get(pk=pk)
        serializer = ProductCategorySerializer(category)
        return Response(data=serializer.data)

    def post(self, request):
        category = ProductCategorySerializer(data=request.data)
        if category.is_valid(raise_exception=True):
            category.save()
        return Response(status=201)

    def put(self, request, pk):
        try:
            instance = ProductCategory.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})
        serializer = ProductCategorySerializer(data=request.data, instance=instance)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({"user": serializer.data})

    def delete(self, request, pk):
        try:
            ProductCategory.objects.filter(pk=pk).delete()
        except:
            return Response({"error": "Object does not exists"})
        return Response(status=200)


class ProductListAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(data=serializer.data)


class ProductAPIView(APIView):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        return Response(data=serializer.data)

    def post(self, request):
        product = ProductSerializer(data=request.data)
        if product.is_valid(raise_exception=True):
            product.save()
        return Response(status=201)

    def put(self, request, pk):
        try:
            instance = Product.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})
        serializer = ProductSerializer(data=request.data, instance=instance)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({"user": serializer.data})

    def delete(self, request, pk):
        try:
            Product.objects.filter(pk=pk).delete()
        except:
            return Response({"error": "Object does not exists"})
        return Response(status=200)


class BasketAPIView(APIView):
    def get(self, request, user):
        product = Basket.objects.filter(user=user)
        serializer = BasketSerializer(product, many=True)
        return Response(data=serializer.data)


class BasketItemAPIView(APIView):
    def get(self, request, pk):
        product = Basket.objects.filter(pk=pk)
        serializer = BasketSerializer(product)
        return Response(data=serializer.data)

    def post(self, request):
        basket = BasketSerializer(data=request.data)
        if basket.is_valid(raise_exception=True):
            basket.save()
        return Response(status=201)

    def put(self, request, pk):
        try:
            instance = Basket.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})
        serializer = BasketSerializer(data=request.data, instance=instance)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({"user": serializer.data})

    def delete(self, request, pk):
        try:
            Basket.objects.filter(pk=pk).delete()
        except:
            return Response({"error": "Object does not exists"})
        return Response(status=200)
