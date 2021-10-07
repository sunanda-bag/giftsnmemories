from django.urls import path
from .views import *

app_name='product'

urlpatterns = [
    path('detail/<slug:slug>', ProductView.as_view(),name="product-page"),
    # path('all-category/', AllCategoryView.as_view(),name="all-category"),
    # path('men/', MenCategoryView.as_view(), name='men-category'),
    # path('women/', WomenCategoryView.as_view(), name='women-category'),
    path('search/', SearchCategoryView.as_view(), name='search-category'),
    # path('filter/', FilterCategoryView.as_view(), name='filter-category'),
    # path('sort/', SortView.as_view(), name='sort-category'),
    path('size-product/', sizeProduct, name='size-product'),
    # path('color-product/', colorProduct, name='color-product'),
    # path('product/post-review/', postReview, name='post-review'),


    path('premade/', premade, name='premade'),
    path('build-a-box/', build_a_box, name='build-a-box'),


    # add items urls
    path('add-category/', AddCategoryView.as_view(), name='add-category'),
    # path('add-sub-category/', AddSubCategoryView.as_view(), name='add-sub-category'),
    # path('add-size/', AddSizeView.as_view(), name='add-size'),
    # path('add-color/', AddColorView.as_view(), name='add-color'),
    path('add-product/', AddProductView.as_view(), name='add-product'),
    path('add-product-variation/', AddProductVariationView.as_view(), name='add-product-variation'),
    

]