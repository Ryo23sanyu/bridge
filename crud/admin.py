from django.contrib import admin
from .models import Product, Category
from django.utils.safestring import mark_safe

class ProductAdmin(admin.ModelAdmin):
     list_display = ('id', 'name', 'damage_name', 'picture_number', 'picture_comment', 'findings', 'image')
     search_fields = ('name','damage_name')
     list_filter = ('name', 'damage_name',)
     
     def image(self, obj):
      if obj.img:
        return mark_safe('<img src="{}" style="width:100px; height:auto;">'.format(obj.img.url))# mark_safe関数:管理画面にimgタグを出力するため
      else:
        return 'No Image'
     
class CategoryAdmin(admin.ModelAdmin):
     list_display = ('id', 'name')
     search_fields = ('name',)
     
admin.site.register(Product, ProductAdmin)# アプリケーションのproduct名
admin.site.register(Category, CategoryAdmin)

