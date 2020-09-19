from django.urls import path
from .views import (
    #StatusListSearchAPIView,
                      StatusAPIView,
                     # StatusCreateAPIView,
                     #StatusDetailAPIView,
                    #StatusUpdateAPIView,
                   # StatusDeleteAPIView
                    )
urlpatterns = [
       # path('', StatusListSearchAPIView.as_view()),
        path('', StatusAPIView.as_view()),
        # path('create/', StatusCreateAPIView.as_view()),
        #path('<int:pk>/', StatusDetailAPIView.as_view()),
        # path('<int:pk>/update/', StatusUpdateAPIView.as_view()),
        # path('<int:pk>/delete/', StatusDeleteAPIView.as_view())
]

# start with

# /api/status/ ---> List View
# /api/status/create --->Create
# /api/status/12/ --->Detail
# /api/status/12/update ----> update
# /api/status/12/delete ----> delete


# End with

# /api/status/ -->list
# /api/status/1/ --> Details -->CrUd