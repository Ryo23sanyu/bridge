from django.db import models
from django.urls import reverse

class Category(models.Model):
     name = models.CharField(max_length=200)
 
     def __str__(self):
         return self.name

class Product(models.Model):
    
    CHOICES = [
        ('0', '腐食'),
        ('1', '亀裂'),
        ('2', 'ゆるみ・脱落'),
        ('3', '破断'),
        ('4', '防食機能の劣化'),
        ('5', 'ひびわれ'),
        ('6', '剥離・鉄筋露出'),
        ('7', '漏水・遊離石灰'),
        ('8', '抜け落ち'),
        ('9', '補修・補強材の損傷'),
        ('10', '床版ひびわれ'),
        ('11', 'うき'),
        ('12', '遊間の異常'),
        ('13', '路面の凹凸'),
        ('14', '舗装の異常'),
        ('15', '支承部の機能障害'),
        ('16', 'その他'),
        ('17', '定着部の異常'),
        ('18', '変色・劣化'),
        ('19', '漏水・滞水'),
        ('20', '異常な音・振動'),
        ('21', '異常なたわみ'),
        ('22', '変形・欠損'),
        ('23', '土砂詰まり'),
        ('24', '沈下・移動・傾斜'),
        ('25', '洗堀'),
    ]
    name = models.CharField(max_length=200)
    damage_name = models.CharField(max_length=20, choices=CHOICES, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    picture_number = models.CharField(max_length=20)
    picture_comment = models.CharField(max_length=200, default='', blank=True)
    findings = models.CharField(max_length=200, default='', blank=True)
    # img = models.ImageField(blank=True, default='noImage.png')
    img = models.ImageField(upload_to='images/')
     
    def __str__(self):
        return self.name
    
    # 選択肢のラベルを返すメソッドを追加
    def get_damage_name_label(self):
        choices = dict(self.CHOICES)
        return choices.get(self.damage_name)
    
    def __str__(self):
         return self.name# タイトルに名前を返す
       
    # 新規作成・編集完了時のリダイレクト先
    def get_absolute_url(self):
         return reverse('list')
       

