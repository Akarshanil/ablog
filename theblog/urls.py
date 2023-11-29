from django.urls import path
from .views import HomeView,ArticleDetailView,AddPostView,UpdatePostView,DeletePostView,AddCategoryView,CategoryView,CategoryListView,LikeView,AddcommentView

urlpatterns =[
    # path('home/',views.home,name="home")
    path('home/',HomeView.as_view(),name="home"),
    path('article/<int:pk>/',ArticleDetailView.as_view(),name="article-detail"),
    path('addpost/',AddPostView.as_view(),name="add_post"),
    path('article/edit/<int:pk>',UpdatePostView.as_view(),name="update_post"),
    path('article/Delete/<int:pk>', DeletePostView.as_view(), name="delete_post"),
    path('addcategory/', AddCategoryView.as_view(), name="addcategory"),
    path('category/<cats>', CategoryView, name="category"),
    path('category-list/', CategoryListView, name="category_list"),
    path('like/<int:pk>', LikeView, name="like_post"),
    path('article/<int:pk>/comment/', AddcommentView.as_view(), name="Add_comment"),

]