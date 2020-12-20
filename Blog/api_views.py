from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.response import Response
from .seriallizer import Article, ArticleSeriallizer



@api_view(["POST", "GET"])

def create_api(request):
    if request.method == "POST": 
        create=ArticleSeriallizer(data=request.data)
        if create.is_valid(): 
            create.save()
            return Response(create.data)
        return Response(create.errors, status=404)
    row= Article.objects.all()
    all_data = ArticleSeriallizer(row, many=1)
    return Response(all_data.data)

@api_view(["GET","PUT", "DELETE"])
def detail_api(request, pk): 
    try:
         obj = Article.objects.get(pk=pk)
    except Exception as ec:
        return Response({'msg': "id not fout"}, status=404)
    if request.method == "DELETE": 
        obj.delete()
        return Response({'msg': 'sucess delete data'}, status=203)
    if request.method == 'PUT': 
        edit_data = ArticleSeriallizer(obj, data=request.data)
        if edit_data.is_valid(): 
            edit_data.save()
            return Response(edit_data.data)
        return Response(edit_data.errors, status=404)
    detail_data=ArticleSeriallizer(obj)
    return Response(detail_data.data)


@api_view(['GET'])
@permission_classes([])
def api_blog(request, slug):
     obj = Article.objects.filter(slug=slug).first()
     if not obj:
        return Response({'msg': "article not fout"}, status=404)
     serial = ArticleSeriallizer(obj)
     return Response(serial.data)
    


@api_view(['GET'])
@permission_classes([])
def api_allblog(request): 
    obj = Article.objects.all()
    serial = ArticleSeriallizer(obj, many=1)
    return Response(serial.data)







