# from django.urls import path
# from todo_app.views import home_page


# urlpatterns = [
#     path('', home_page, name="home"),
#     # path('data/', data_page, name="data")
#     # path("data/<int:id>",update ),
#     # path("data/<int:id>",delete),

# ]

from django.urls import path
from .views import home_page,create_todo, update_view, delete_view, show_view

urlpatterns = [
    path('', home_page, name="home"),
    path('create/', create_todo, name="create_todo"),
    path('update/<int:id>/', update_view, name='update_view'),
    path('delete/<int:id>/', delete_view, name='delete_view'),
    path('show/<int:id>/', show_view, name='show_view'),

]
