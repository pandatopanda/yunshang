from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
#Shop,Category,ProductsSPU,SPUspecType,SPUspecValue,SPUspec,ProductsImage,ProductsImage,ProductsSKU,Customer,Order,Order_list,Comment
# Create your models here.



class Category(models.Model):

    name=models.CharField(max_length=100,verbose_name='类目名',default='abc')
    detail = models.TextField()

    class Meta:
        verbose_name = '类目'
        verbose_name_plural = verbose_name
        

class ProductsSPU (models.Model):
   name=models.CharField(max_length=100)
   #  当我删除商品分类时时商品SPU的数据也随之删除
   category_id = models.ForeignKey(to=Category,on_delete=set)
   desc_detail = models.CharField(max_length=1000, verbose_name='详情',default='abc')

   class Meta:
       verbose_name = '商品SPU'
       verbose_name_plural = verbose_name

class SPUspecType(models.Model):
    name = models.CharField(default='abc',max_length=100, verbose_name='规格名')

    class Meta:
        verbose_name = 'SPU规格类型'
        verbose_name_plural = verbose_name

class SPUspecValue(models.Model):
     name = models.CharField(max_length=100, verbose_name='规格值',default='abc')

     class Meta:
         verbose_name = '商品SPU规格值'
         verbose_name_plural = verbose_name

class SPUspec(models.Model):
    spu_id = models.ForeignKey(to=ProductsSPU, on_delete=set)
    type_id = models.ForeignKey(SPUspecType, on_delete=set,verbose_name='规格名')
    value_id=models.ForeignKey(SPUspecValue, on_delete=set,verbose_name='规格值')

    class Meta:
        verbose_name = '规格'
        verbose_name_plural = verbose_name



# SKU图片表，id为主键，
class ProductsImage(models.Model):
    name = models.CharField(max_length=50, verbose_name='图片名',default='abc')
    picture = models.ImageField(upload_to='avatar/%Y/%m/%d/',verbose_name='图片源')
    class Meta:
        verbose_name = 'SKU图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.picture



# 产品SKU表，SPU通过获取规格的类型和值访问SKU表
class ProductsSKU(models.Model):
    name=models.CharField(max_length=50,verbose_name='SKU名',default='abc')
    is_launched = models.BooleanField(default=False)
    spu_id = models.ForeignKey(to=ProductsSPU, on_delete=set)
    code = models.CharField(max_length=50,verbose_name='sku编号',default='abc')
    price = models.DecimalField(max_digits=9,decimal_places=2)
    store = models.IntegerField( verbose_name='库存')
    img = models.ForeignKey(to=ProductsImage,on_delete=set,verbose_name='图片')
    class Meta:
        verbose_name = '商品SKU'
        verbose_name_plural = verbose_name

#
# class ShopProducts(models.Model):
#     produsts_id = models.ForeignKey(unique=(ProductsSKU.pk,Shop.pk),on_delete=set)

#


class Customer (models.Model):
    name = models.CharField(max_length=50, verbose_name='用户名',default='abc')
    password = models.CharField(max_length=20, verbose_name='密码',default='abc')
    phone = models.CharField(max_length=20, verbose_name='联系电话',default='abc')
    address = models.CharField(max_length=200, verbose_name='地址',default='abc')
    integral = models.IntegerField(verbose_name='积分')

    class Meta:  # 定义元数据
        verbose_name = '客户信息'
        verbose_name_plural = verbose_name  # 设置后台模块
        ordering = ['-id']  # id降序排列

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.ForeignKey(Customer, verbose_name='下单用户',on_delete=set)
    price = models.CharField(max_length=10, verbose_name='总价格',default='abc')
    order_state = models.CharField(max_length=10, choices=(('未发货', '未发货'), ('已发货', '已发货')), verbose_name='订单状态')
    express_id = models.CharField(max_length=50, verbose_name='快递单号',default='abc')
    order_date = models.DateField('订单时间', auto_now=True)

    class Meta:
        verbose_name = '订单信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order_state)






class Order_list(models.Model):
    name = models.CharField(max_length=50, verbose_name='商品名',default='abc')
    quantity = models.IntegerField(default=0, verbose_name='数量')
    order = models.ForeignKey(Order, verbose_name='所属订单',on_delete=set)
    remark = models.IntegerField(default=0, choices=((0, '未评价'), (1, '已评价')), verbose_name='是否评价')
    user_id = models.IntegerField(default=0,verbose_name='用户')
    list_date = models.DateField('订单时间', auto_now=True)

    class Meta:
        verbose_name = '订单条目信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.name)

#评论
class Comment(models.Model):
    comm= models.CharField(max_length=200,verbose_name='评论内容',default='abc')
    ProductsSKU_id = models.ForeignKey(to=ProductsSKU,on_delete=set,verbose_name='商品ID')
    user_id = models.ForeignKey(to=Customer, on_delete=set,default=1,verbose_name='用户ID')
    order_id = models.ForeignKey(to=Order,on_delete=set,verbose_name='订单ID')

    class Meta:
        verbose_name = '评价信息'
        verbose_name_plural = verbose_name
    def __str__(self):
        return str(self.comm)

class Caritem(models.Model):
    SKU_id = models.ForeignKey(ProductsSKU, verbose_name='购物车中产品条目',on_delete=set)
    quantity = models.IntegerField(default=0, verbose_name='数量')
    sum_price = models.FloatField(default=0.0, verbose_name='小计')

    class Meta:
        verbose_name = '购物车条目信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.id)


class Shop(models.Model):
    name = models.CharField(max_length=100, verbose_name='店铺名',default='abc')
    address= models.CharField(max_length=100, verbose_name='地址',default='abc')
    SKU_id= models.ForeignKey(to=ProductsSKU,on_delete=set,verbose_name='所属商品')
    class Meta:
        verbose_name = '店铺信息'
        verbose_name_plural = verbose_name

class Cart(models.Model ):
    def __str__(self):
        self.items = []
        self.total_price = 0.0

    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = verbose_name
    #  #定义加入购物车算法
    # def add(self, furniture):
    #     self.total_price += furniture.new_price  # 购物车总额增加
    #     for item in self.items:
    #         if item.furniture.id == furniture.id:  # 购物车已存在该商品
    #             item.quantity += 1  # 数量增一
    #             item.sum_price += furniture.new_price
    #             return
    #     else:
    #         self.items.append(Caritem(furniture=furniture, quantity=1, sum_price=furniture.new_price))







# 购物车
