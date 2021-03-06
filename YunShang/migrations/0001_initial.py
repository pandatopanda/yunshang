# Generated by Django 2.1.7 on 2019-04-29 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caritem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0, verbose_name='数量')),
                ('sum_price', models.FloatField(default=0.0, verbose_name='小计')),
            ],
            options={
                'verbose_name': '购物车条目信息',
                'verbose_name_plural': '购物车条目信息',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': '购物车',
                'verbose_name_plural': '购物车',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='abc', max_length=100, verbose_name='类目名')),
            ],
            options={
                'verbose_name': '类目',
                'verbose_name_plural': '类目',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comm', models.CharField(default='abc', max_length=200, verbose_name='评论内容')),
            ],
            options={
                'verbose_name': '评价信息',
                'verbose_name_plural': '评价信息',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='abc', max_length=50, verbose_name='用户名')),
                ('password', models.CharField(default='abc', max_length=20, verbose_name='密码')),
                ('phone', models.CharField(default='abc', max_length=20, verbose_name='联系电话')),
                ('address', models.CharField(default='abc', max_length=200, verbose_name='地址')),
                ('integral', models.IntegerField(verbose_name='积分')),
            ],
            options={
                'verbose_name': '客户信息',
                'verbose_name_plural': '客户信息',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(default='abc', max_length=10, verbose_name='总价格')),
                ('order_state', models.CharField(choices=[('未发货', '未发货'), ('已发货', '已发货')], max_length=10, verbose_name='订单状态')),
                ('express_id', models.CharField(default='abc', max_length=50, verbose_name='快递单号')),
                ('order_date', models.DateField(auto_now=True, verbose_name='订单时间')),
                ('name', models.ForeignKey(on_delete=set, to='YunShang.Customer', verbose_name='下单用户')),
            ],
            options={
                'verbose_name': '订单信息',
                'verbose_name_plural': '订单信息',
            },
        ),
        migrations.CreateModel(
            name='Order_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='abc', max_length=50, verbose_name='商品名')),
                ('quantity', models.IntegerField(default=0, verbose_name='数量')),
                ('remark', models.IntegerField(choices=[(0, '未评价'), (1, '已评价')], default=0, verbose_name='是否评价')),
                ('user_id', models.IntegerField(default=0, verbose_name='用户')),
                ('list_date', models.DateField(auto_now=True, verbose_name='订单时间')),
                ('order', models.ForeignKey(on_delete=set, to='YunShang.Order', verbose_name='所属订单')),
            ],
            options={
                'verbose_name': '订单条目信息',
                'verbose_name_plural': '订单条目信息',
            },
        ),
        migrations.CreateModel(
            name='ProductsImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='abc', max_length=50, verbose_name='图片名')),
                ('picture', models.ImageField(upload_to='avatar/%Y/%m/%d/', verbose_name='图片源')),
            ],
            options={
                'verbose_name': 'SKU图片',
                'verbose_name_plural': 'SKU图片',
            },
        ),
        migrations.CreateModel(
            name='ProductsSKU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='abc', max_length=50, verbose_name='SKU名')),
                ('is_launched', models.BooleanField(default=False)),
                ('code', models.CharField(default='abc', max_length=50, verbose_name='sku编号')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('store', models.IntegerField(verbose_name='库存')),
                ('img', models.ForeignKey(on_delete=set, to='YunShang.ProductsImage', verbose_name='图片')),
            ],
            options={
                'verbose_name': '商品SKU',
                'verbose_name_plural': '商品SKU',
            },
        ),
        migrations.CreateModel(
            name='ProductsSPU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc_detail', models.CharField(default='abc', max_length=1000, verbose_name='详情')),
                ('category_id', models.ForeignKey(on_delete=set, to='YunShang.Category')),
            ],
            options={
                'verbose_name': '商品SPU',
                'verbose_name_plural': '商品SPU',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='abc', max_length=100, verbose_name='店铺名')),
                ('address', models.CharField(default='abc', max_length=100, verbose_name='地址')),
                ('SKU_id', models.ForeignKey(on_delete=set, to='YunShang.ProductsSKU', verbose_name='所属商品')),
            ],
            options={
                'verbose_name': '店铺信息',
                'verbose_name_plural': '店铺信息',
            },
        ),
        migrations.CreateModel(
            name='SPUspec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spu_id', models.ForeignKey(on_delete=set, to='YunShang.ProductsSPU')),
            ],
            options={
                'verbose_name': '规格',
                'verbose_name_plural': '规格',
            },
        ),
        migrations.CreateModel(
            name='SPUspecType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='abc', max_length=100, verbose_name='规格名')),
            ],
            options={
                'verbose_name': 'SPU规格类型',
                'verbose_name_plural': 'SPU规格类型',
            },
        ),
        migrations.CreateModel(
            name='SPUspecValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='abc', max_length=100, verbose_name='规格值')),
            ],
            options={
                'verbose_name': '商品SPU规格值',
                'verbose_name_plural': '商品SPU规格值',
            },
        ),
        migrations.AddField(
            model_name='spuspec',
            name='type_id',
            field=models.ForeignKey(on_delete=set, to='YunShang.SPUspecType', verbose_name='规格名'),
        ),
        migrations.AddField(
            model_name='spuspec',
            name='value_id',
            field=models.ForeignKey(on_delete=set, to='YunShang.SPUspecValue', verbose_name='规格值'),
        ),
        migrations.AddField(
            model_name='productssku',
            name='spu_id',
            field=models.ForeignKey(on_delete=set, to='YunShang.ProductsSPU'),
        ),
        migrations.AddField(
            model_name='comment',
            name='ProductsSKU_id',
            field=models.ForeignKey(on_delete=set, to='YunShang.ProductsSKU', verbose_name='商品ID'),
        ),
        migrations.AddField(
            model_name='comment',
            name='order_id',
            field=models.ForeignKey(on_delete=set, to='YunShang.Order', verbose_name='订单ID'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=set, to='YunShang.Customer', verbose_name='用户ID'),
        ),
        migrations.AddField(
            model_name='caritem',
            name='SKU_id',
            field=models.ForeignKey(on_delete=set, to='YunShang.ProductsSKU', verbose_name='购物车中产品条目'),
        ),
    ]
