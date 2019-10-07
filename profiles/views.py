import profiles.models as profiles_models
import profiles.serializers as profiles_serializers

import time
from rest_framework.parsers import FileUploadParser
from django.db import connection, reset_queries
from rest_framework import viewsets
from core import permissions as core_permissions
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ( ListAPIView, 
    CreateAPIView, UpdateAPIView, RetrieveAPIView, ListCreateAPIView,
    RetrieveUpdateAPIView
)

User = get_user_model();

# To Check Number of Query Execution #
# print(len(connection.queries))
# reset_queries()

# class Client(ListAPIView):
#     queryset = client_models.Client.objects.all()
#     serializer_class = sud_serializers.ClientSerializer
#     permission_classes = [ IsAuthenticated, core_permissions.IsAdminUser]

#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())

#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)

#         serializer = self.get_serializer(queryset, many=True)
#         return Response({'data':serializer.data,'status':True})

# class ClientDetail(CreateAPIView, RetrieveUpdateAPIView):
#     lookup_field = 'id'
#     queryset = client_models.Client.objects.all()
#     serializer_class = sud_serializers.ClientSerializer
#     permission_classes = [ IsAuthenticated, core_permissions.IsAdminUser]

#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return Response({'data':serializer.data,'status':True})
    
#     def create(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         return Response({'message':'Client Created Succesfully', 'status':False}, status=status.HTTP_200_OK)

#     def update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)
#         return Response({'message':'Client Updated Succesfully', 'status':False}, status=status.HTTP_200_OK)

# class ListSubject(ListAPIView):
#     queryset = course_models.Subject.objects.filter(created_by_superuser=True)
#     serializer_class = sud_serializers.ListSubjectSerializer
#     permission_classes = [ IsAuthenticated, core_permissions.IsAdminUser]

#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())

#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)

#         serializer = self.get_serializer(queryset, many=True)
#         if(serializer.data):
#             return Response({'data':serializer.data,'status':True})
#         else:
#             return Response({'message':"No Subjects",'status':False})

# class SubjectDetail(CreateAPIView, RetrieveUpdateAPIView):
#     lookup_field = 'id'
#     queryset = course_models.Subject.objects.filter(created_by_superuser=True)
#     serializer_class = sud_serializers.ListSubjectSerializer
#     permission_classes = [ IsAuthenticated, core_permissions.IsAdminUser]

#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return Response({'data':serializer.data,'status':True})
    
#     def create(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         return Response({'message':'Subject Created Succesfully', 'status':False}, status=status.HTTP_200_OK)

#     def update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)
#         return Response({'message':'Subject Updated Succesfully', 'status':False}, status=status.HTTP_200_OK)

# class ListStandard(ListAPIView):
#     queryset = course_models.Standard.objects.filter(created_by_superuser=True)
#     serializer_class = sud_serializers.ListStandardSerializer
#     permission_classes = [ IsAuthenticated, core_permissions.IsAdminUser]

#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())

#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)

#         serializer = self.get_serializer(queryset, many=True)
#         if(serializer.data):
#             return Response({'data':serializer.data,'status':True})
#         else:
#             return Response({'message':"No Standards",'status':False})

# class StandardDetail(CreateAPIView, RetrieveUpdateAPIView):
#     lookup_field = 'id'
#     queryset = course_models.Standard.objects.filter(created_by_superuser=True)
#     serializer_class = sud_serializers.ListStandardSerializer
#     permission_classes = [ IsAuthenticated, core_permissions.IsAdminUser]

#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return Response({'data':serializer.data,'status':True})
    
#     def create(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         return Response({'message':'Standard Created Succesfully', 'status':False}, status=status.HTTP_200_OK)

#     def update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)
#         return Response({'message':'Standard Updated Succesfully', 'status':False}, status=status.HTTP_200_OK)

# class ListSubStd(ListAPIView):
#     serializer_class = sud_serializers.ListSubStdSerializer
#     permission_classes = [ IsAuthenticated, core_permissions.IsAdminUser]

#     def get_queryset(self, **kwargs):
#         data = kwargs['request'].query_params
#         data_keys = list(data.keys())
#         filter_data = { key : data.getlist(key)[0] for key in data_keys }
#         queryset = course_models.SubStd.objects.filter(created_by_superuser=True, **filter_data)
#         return(queryset)

#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset(request=request))

#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)

#         serializer = self.get_serializer(queryset, many=True)
#         if(serializer.data):
#             return Response({'data':serializer.data,'status':True})
#         else:
#             return Response({'message':"No SubStd",'status':False})

# class SubStdDetail(CreateAPIView, RetrieveUpdateAPIView):
#     lookup_field = 'id'
#     queryset = course_models.SubStd.objects.filter(created_by_superuser=True)
#     serializer_class = sud_serializers.ListSubStdSerializer
#     permission_classes = [ IsAuthenticated, core_permissions.IsAdminUser]

#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return Response({'data':serializer.data,'status':True})
    
#     def create(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         return Response({'message':'SubStd Created Succesfully', 'status':False}, status=status.HTTP_200_OK)

#     def update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)
#         return Response({'message':'SubStd Updated Succesfully', 'status':False}, status=status.HTTP_200_OK)

# class ListChapter(ListAPIView):
#     serializer_class = sud_serializers.ListChapterSerializer
#     permission_classes = [ IsAuthenticated, core_permissions.IsAdminUser]

#     def get_queryset(self, **kwargs):
#         data = kwargs['request'].query_params
#         data_keys = list(data.keys())
#         filter_data = { key : data.getlist(key)[0] for key in data_keys }
#         queryset = course_models.Chapter.objects.filter(created_by_superuser=True, **filter_data)
#         return(queryset)

#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset(request=request))

#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)

#         serializer = self.get_serializer(queryset, many=True)
#         if(serializer.data):
#             return Response({'data':serializer.data,'status':True})
#         else:
#             return Response({'message':"No Chapter",'status':False})

# class ChapterDetail(CreateAPIView, RetrieveUpdateAPIView):
#     lookup_field = 'id'
#     queryset = course_models.Chapter.objects.filter(created_by_superuser=True)
#     serializer_class = sud_serializers.ListChapterSerializer
#     permission_classes = [ IsAuthenticated, core_permissions.IsAdminUser]

#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return Response({'data':serializer.data,'status':True})
    
#     def create(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         ch_obj = course_models.Chapter.objects.filter(substd_id=serializer.validated_data['substd'], chapter_order=serializer.validated_data['chapter_order'])
#         if(ch_obj):
#             return Response({'errors':'Chapter Order Already Exist.', 'status':False}, status=status.HTTP_200_OK)    
#         self.perform_create(serializer)
#         return Response({'message':'Chapter Created Succesfully', 'status':False}, status=status.HTTP_200_OK)

#     def update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         ch_obj = course_models.Chapter.objects.filter(substd_id=serializer.validated_data['substd'], chapter_order=serializer.validated_data['chapter_order'])
#         if(ch_obj and (ch_obj.first() != instance)):
#             return Response({'errors':'Chapter Order Already Exist.', 'status':False}, status=status.HTTP_200_OK)    
#         self.perform_update(serializer)
#         return Response({'message':'Chapter Updated Succesfully', 'status':False}, status=status.HTTP_200_OK)

# class ListTopic(ListAPIView):
#     serializer_class = sud_serializers.ListTopicSerializer
#     permission_classes = [ IsAuthenticated, core_permissions.IsAdminUser]

#     def get_queryset(self, **kwargs):
#         data = kwargs['request'].query_params
#         data_keys = list(data.keys())
#         filter_data = { key : data.getlist(key)[0] for key in data_keys }
#         queryset = course_models.Topic.objects.filter(created_by_superuser=True, **filter_data)
#         return(queryset)

#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset(request=request))

#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)

#         serializer = self.get_serializer(queryset, many=True)
#         if(serializer.data):
#             return Response({'data':serializer.data,'status':True})
#         else:
#             return Response({'message':"No Topic",'status':False})

# class TopicDetail(CreateAPIView, RetrieveUpdateAPIView):
#     lookup_field = 'id'
#     queryset = course_models.Topic.objects.filter(created_by_superuser=True)
#     serializer_class = sud_serializers.ListTopicSerializer
#     permission_classes = [ IsAuthenticated, core_permissions.IsAdminUser]

#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return Response({'data':serializer.data,'status':True})
    
#     def create(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         topic_obj = course_models.Topic.objects.filter(chapter_id=serializer.validated_data['chapter'], topic_order=serializer.validated_data['topic_order'])
#         if(topic_obj):
#             return Response({'errors':'Topic Order Already Exist.', 'status':False}, status=status.HTTP_200_OK)    
#         self.perform_create(serializer)
#         return Response({'message':'Topic Created Succesfully', 'status':False}, status=status.HTTP_200_OK)

#     def update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         topic_obj = course_models.Topic.objects.filter(chapter_id=serializer.validated_data['chapter'], topic_order=serializer.validated_data['topic_order'])
#         if(topic_obj and (topic_obj.first() != instance)):
#             return Response({'errors':'Topic Order Already Exist.', 'status':False}, status=status.HTTP_200_OK)    
#         self.perform_update(serializer)
#         return Response({'message':'Topic Updated Succesfully', 'status':False}, status=status.HTTP_200_OK)

# class ListQuestion(ListAPIView):
#     serializer_class = sud_serializers.QuestionSerializer
#     permission_classes = [ IsAuthenticated, core_permissions.IsAdminUser]

#     def get_queryset(self, **kwargs):
#         data = kwargs['request'].query_params
#         data_keys = list(data.keys())
#         filter_data = { key : data.getlist(key)[0] for key in data_keys }
#         queryset = quiz_models.Question.objects.filter(**filter_data)
#         return(queryset)

#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset(request=request))

#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)

#         serializer = self.get_serializer(queryset, many=True)
#         if(serializer.data):
#             return Response({'data':serializer.data,'status':True})
#         else:
#             return Response({'message':"No Questions",'status':False})

# class QuestionDetail(CreateAPIView, RetrieveUpdateAPIView):
#     lookup_field = 'id'
#     queryset = quiz_models.Question.objects.all().prefetch_related('mcqtestcase_set', 'stringtestcase_set', 'solution_set')
#     serializer_class = sud_serializers.QuestionSerializer
#     permission_classes = [ IsAuthenticated, core_permissions.IsAdminUser]
#     parser_class = (FileUploadParser)

#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return Response({'data':serializer.data,'status':True})
    
#     def create(self, request, *args, **kwargs):
#         data = request.data.copy() # Making a Copy because request.data is immutable.
#         data['timestamp'] = int(round(time.time() * 1000))
#         serializer = self.serializer_class(data=data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         return Response({'message':'Question Created Succesfully', 'status':False}, status=status.HTTP_200_OK)

#     def update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=True, context={'request':request})
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)
#         return Response({'message':'Question Updated Succesfully', 'status':False}, status=status.HTTP_200_OK)

# class BulkUploadQuestion(CreateAPIView):
#     queryset = quiz_models.Question.objects.all()
#     serializer_class = sud_serializers.QuestionSerializer
#     permission_classes = [ IsAuthenticated, core_permissions.IsAdminUser]
#     parser_class = (FileUploadParser)
    
#     def create(self, request, *args, **kwargs):
#         csv_file = request.FILES['csv_file']
#         zip_file = request.FILES['zip_file'] if('zip_file' in request.FILES) else None

#         # If error = True then mssg is a List of error strings.
#         # If error = False then mssg is a List of Question ids.
#         mssg, no_error = quiz_utils.bulkuploadquestioncsv(csv_file=csv_file, zip_file=zip_file)

#         if(no_error):
#             question_data = quiz_models.Question.objects.filter(id__in=mssg).prefetch_related(
#                         'mcqtestcase_set', 'stringtestcase_set', 'solution_set'
#                     )
#             serializer = self.serializer_class(question_data, many=True)
#             return Response({'data':serializer.data, 'status':True, 'uploaded':no_error}, status=status.HTTP_200_OK)
#         else:
#             return Response({'errors':mssg, 'status':False, 'uploaded':no_error}, status=status.HTTP_200_OK)