from django.contrib import admin
from YunShang.models import Shop,Category,ProductsSPU,SPUspecType,SPUspecValue,SPUspec,ProductsImage,ProductsSKU,Customer,Order,Order_list,Comment,Caritem,Cart
# Register your models here.

admin.site.register(Shop)
admin.site.register(SPUspecValue)
admin.site.register(SPUspecType)
admin.site.register(SPUspec)
admin.site.register(ProductsSKU)
admin.site.register(ProductsSPU)
admin.site.register(Customer)
admin.site.register(ProductsImage)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Order_list)
admin.site.register(Comment)
admin.site.register(Caritem)
admin.site.register(Cart)