# Generated by Django 4.1.7 on 2023-11-21 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0006_product_category_product_findings_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, default='noImage.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='damage_name',
            field=models.CharField(choices=[('0', '腐食'), ('1', '亀裂'), ('2', 'ゆるみ・脱落'), ('3', '破断'), ('4', '防食機能の劣化'), ('5', 'ひびわれ'), ('6', '剥離・鉄筋露出'), ('7', '漏水・遊離石灰'), ('8', '抜け落ち'), ('9', '補修・補強材の損傷'), ('10', '床版ひびわれ'), ('11', 'うき'), ('12', '遊間の異常'), ('13', '路面の凹凸'), ('14', '舗装の異常'), ('15', '支承部の機能障害'), ('16', 'その他'), ('17', '定着部の異常'), ('18', '変色・劣化'), ('19', '漏水・滞水'), ('20', '異常な音・振動'), ('21', '異常なたわみ'), ('22', '変形・欠損'), ('23', '土砂詰まり'), ('24', '沈下・移動・傾斜'), ('25', '洗堀')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='findings',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='picture_comment',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
