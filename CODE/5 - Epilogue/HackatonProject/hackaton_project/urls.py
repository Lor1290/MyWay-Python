from django.urls import path, include

urlpatterns = [
    path('', include('hackaton_app.urls')), # -> only one path, we decide not to implement s
                                            #    user registration or a admin page
]