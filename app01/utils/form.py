from django import forms
from app01.models import User
import re

class UserForm(forms.ModelForm):
    # 确认密码（前端验证 + 后端二次验证）
    upass_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "请确认密码"}),
        label="确认密码",
        required=True
    )

    class Meta:
        model = User
        fields = [
            'uname', 'upass', 'upass_confirm',
            'uprov', 'uage', 'ugender',
            'udate', 'utel', 'uphoto',
            'uurl', 'uemail', 'ubackcolor',
            'is_agree'
        ]
        # 自定义前端控件属性（placeholder、类型等）
        widgets = {
            'uname': forms.TextInput(attrs={"placeholder": "请输入用户名"}),
            'upass': forms.PasswordInput(attrs={"placeholder": "请输入密码"}),
            'uprov': forms.Select(attrs={"class": "form-select"}),  # 适配 Bootstrap 样式
            'uage': forms.NumberInput(attrs={"placeholder": "年龄"}),
            'ugender': forms.RadioSelect(),  # 渲染为单选按钮
            'udate': forms.DateInput(attrs={"type": "date"}),  # 日期选择器
            'utel': forms.TextInput(attrs={"placeholder": "手机号"}),
            'uurl': forms.URLInput(attrs={"placeholder": "主页"}),
            'uemail': forms.EmailInput(attrs={"placeholder": "Email"}),
            'ubackcolor': forms.TextInput(attrs={"type": "color"}),  # 颜色选择器
            'is_agree': forms.CheckboxInput(),  # 服务条款复选框
        }

    def clean_utel(self):
        """验证手机号格式（正则匹配）"""
        utel = self.cleaned_data.get('utel')
        if not re.match(r'^1[3-9]\d{9}$', utel):
            raise forms.ValidationError("手机号格式错误（需为 11 位有效号码）")
        return utel

    def clean_uage(self):
        """验证年龄范围（0-120 岁）"""
        uage = self.cleaned_data.get('uage')
        if uage < 0 or uage > 120:
            raise forms.ValidationError("年龄必须在 0-120 岁之间")
        return uage

    def clean(self):
        """验证密码一致性"""
        cleaned_data = super().clean()
        upass = cleaned_data.get('upass')
        upass_confirm = cleaned_data.get('upass_confirm')
        if upass != upass_confirm:
            self.add_error('upass_confirm', "两次输入的密码不一致")
        return cleaned_data