import json
from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from dev_api.models import Status
from .serilalizer import StatusSerilizer

'''CRUD'''


def is_json(json_data):
    try:
        real_json = json.loads(json_data)
        is_vaild = True
    except ValueError:
        is_vaild = False
    return is_vaild

class StatusAPIView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerilizer


# '''
# query
# '''


    def get_queryset(self):
        request = self.request
        qs = Status.objects.all()
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(content_icontains=query)
        return qs


    def get_object(self):
        request = self.request
        passed_id = request.GET.get('id', None) or self.passed_id
        queryset = self.get_queryset()
        obj = None
        if passed_id is not None:
            obj = get_object_or_404(queryset, id=passed_id)

            self.check_object_permissions(request, dobj)
        return obj


    def perform_destroy(self, instance):
        if instance is not None:
            return instance.delete()
        return None


    """ get data """


    def get(self, request, *args, **kwargs):
        url_pass_id = request.GET.get('id', None)
        json_data = {}
        body_ = request.body
        if is_json(body_):
            json_data = json.loads(request.body)
        new_passed_id = json_data.get('id', None)

        passed_id = url_pass_id or new_passed_id or None
        self.passed_id = passed_id
        if passed_id is not None:
            return self.retrieve(request, *args, **kwargs)
        return super().get(request, *args, **kwargs)


    '''post data to database admin'''


    def post(self, request, *args, **kwargs):
        url_pass_id = request.GET.get('id', None)
        json_data = {}
        body_ = request.body
        if is_json(body_):
            json_data = json.loads(request.body)
        new_passed_id = json_data.get('id', None)

        passed_id = url_pass_id or new_passed_id or None
        self.passed_id = passed_id
        return self.create(request, *args, **kwargs)


    '''update data'''


    def put(self, request, *args, **kwargs):
        url_pass_id = request.GET.get('id', None)
        json_data = {}
        body_ = request.body
        if is_json(body_):
            json_data = json.loads(request.body)
        new_passed_id = json_data.get('id', None)

        passed_id = url_pass_id or new_passed_id or None
        self.passed_id = passed_id
        return self.update(request, *args, **kwargs)


    def patch(self, request, *args, **kwargs):
        url_pass_id = request.GET.get('id', None)
        json_data = {}
        body_ = request.body
        if is_json(body_):
            json_data = json.loads(request.body)
        new_passed_id = json_data.get('id', None)

        passed_id = url_pass_id or new_passed_id or None
        self.passed_id = passed_id
        return self.update(request, *args, **kwargs)


    #'''delete data'''


    def delete(self, request, *args, **kwargs):
        url_pass_id = request.GET.get('id', None)
        json_data = {}
        body_ = request.body
        if is_json(body_):
            json_data = json.loads(request.body)
        new_passed_id = json_data.get('id', None)

        passed_id = url_pass_id or new_passed_id or None
        self.passed_id = passed_id
        return self.destroy(request, *args, **kwargs)



# '''remove first # comment it work mixine  seprate for Creation and and Api view
#   update and delete
#
#   remove second # comment  all processes have seprate funtion
#   and we can  use seprate urls their
# '''

# class StatusListSearchAPIView(APIView):
#     permission_classes = []
#     authentication_classes = []
#
#     def get(self, request, format=None):
#         qs = Status.objects.all()
#         serializer = StatusSerilizer(qs, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None ):
#         qs = Status.objects.all()
#         serializer = StatusSerilizer(qs, many=True)
#         return Response(serializer.data)

# #createModel mixin -------->POST method
# #UpdateModel mixin --------->PUT method
# #DestoryModelmixin --------->DELETE method
#
# class StatusAPIView(mixins.CreateModelMixin, generics.ListAPIView): #create List
#     permission_classes = []
#     authentication_classes = []
#     serializer_class = StatusSerilizer
#
#     def get_queryset(self):
#         qs =Status.objects.all()
#         query = self.request.GET.get('q')
#         if query is not None:
#             qs = qs.filter(content_icontains =query)
#         return qs
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#     '''mixin use cheyumpo  StatusCreateAPIView avashyam ela
#     athu post also doing that process'''
#
# # class StatusCreateAPIView(generics.CreateAPIView):
# #     permission_classes = []
# #     authentication_classes = []
# #     queryset = Status.objects.all()
# #     serializer_class = StatusSerilizer
# #
# #     # def perform_create(self, serializer):
# #     #     serializer.save(user =self.request.user)
# #     #
# class StatusDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerilizer
#     #lookup_field = 'id'
#
#     # def get_object(self, *args, **kwargs):
#     #     kwargs =self.kwargs
#     #     kw_id = kwargs.get('id')
#     #     return Status.objects.get(id=kw_id)
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
#
# '''updates'''
#
# # class StatusUpdateAPIView(generics.UpdateAPIView):
# #     permission_classes = []
# #     authentication_classes = []
# #     queryset = Status.objects.all()
# #     serializer_class = StatusSerilizer
# #
# # class StatusDeleteAPIView(generics.DestroyAPIView):
# #     permission_classes = []
# #     authentication_classes = []
# #     queryset = Status.objects.all()
#     serializer_class = StatusSerilizer
