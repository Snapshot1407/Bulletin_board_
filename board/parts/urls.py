from django.urls import path
from .views import AdsSearch, AdsDetail, AdsCreate, AdsUpdate, AdsDelete

urlpatterns = [
   path('', AdsSearch.as_view(), name='ads_lisr'),
   path('<int:pk>', AdsDetail.as_view(), name='post_detail'),
   path('create/', AdsCreate.as_view(), name='ad_create'),
   path('<int:pk>/edit/', AdsUpdate.as_view(), name='ad_edit'),
   path('<int:pk>/delete/', AdsDelete.as_view(), name='ad_delete'),
]