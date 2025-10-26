from django.db import models
import uuid

class User(models.Model):
    # 中国省级行政区列表（省、自治区、直辖市、特别行政区）
    PROVINCE_CHOICES = (
        ('北京市', '北京市'),
        ('天津市', '天津市'),
        ('河北省', '河北省'),
        ('山西省', '山西省'),
        ('内蒙古自治区', '内蒙古自治区'),
        ('辽宁省', '辽宁省'),
        ('吉林省', '吉林省'),
        ('黑龙江省', '黑龙江省'),
        ('上海市', '上海市'),
        ('江苏省', '江苏省'),
        ('浙江省', '浙江省'),
        ('安徽省', '安徽省'),
        ('福建省', '福建省'),
        ('江西省', '江西省'),
        ('山东省', '山东省'),
        ('河南省', '河南省'),
        ('湖北省', '湖北省'),
        ('湖南省', '湖南省'),
        ('广东省', '广东省'),
        ('广西壮族自治区', '广西壮族自治区'),
        ('海南省', '海南省'),
        ('重庆市', '重庆市'),
        ('四川省', '四川省'),
        ('贵州省', '贵州省'),
        ('云南省', '云南省'),
        ('西藏自治区', '西藏自治区'),
        ('陕西省', '陕西省'),
        ('甘肃省', '甘肃省'),
        ('青海省', '青海省'),
        ('宁夏回族自治区', '宁夏回族自治区'),
        ('新疆维吾尔自治区', '新疆维吾尔自治区'),
        ('香港特别行政区', '香港特别行政区'),
        ('澳门特别行政区', '澳门特别行政区'),
        ('台湾省', '台湾省'),
    )

    GENDER_CHOICES = (
        ('male', '男'),
        ('female', '女'),
    )

    # 用户ID（UUID 主键）
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # 用户名（唯一）
    uname = models.CharField(max_length=50, unique=True, verbose_name="用户名")
    # 密码（存储加密后的值）
    upass = models.CharField(max_length=128, verbose_name="密码")
    # 区域（使用预设的省级行政区列表，默认四川省）
    uprov = models.CharField(
        max_length=50,
        choices=PROVINCE_CHOICES,  # 关联上面定义的省份选项
        default="四川省",
        verbose_name="区域"
    )
    # 年龄
    uage = models.PositiveIntegerField(verbose_name="年龄")
    # 性别（男/女）
    ugender = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name="性别")
    # 生日
    udate = models.DateField(verbose_name="生日")
    # 手机号
    utel = models.CharField(max_length=11, verbose_name="手机号")
    # 头像（上传到 user_photos 目录，允许为空）
    uphoto = models.ImageField(upload_to='user_photos/', null=True, blank=True, verbose_name="头像")
    # 个人主页（可选）
    uurl = models.URLField(blank=True, null=True, verbose_name="主页")
    # 邮箱
    uemail = models.EmailField(verbose_name="Email")
    # 喜欢的颜色（存储颜色值，如 #000000）
    ubackcolor = models.CharField(max_length=20, default="#000000", verbose_name="喜欢的颜色")
    # 服务条款同意状态
    is_agree = models.BooleanField(default=False, verbose_name="同意服务条款")
    # 创建时间
    created_at = models.DateTimeField(auto_now_add=True)
    # 更新时间
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.uname

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = "用户"



class UserInfo(models.Model):
    name=models.CharField(max_length=32)
    password=models.CharField(max_length=32)
    age=models.IntegerField()