# voting/admin.py

from django.contrib import admin
from .models import Target

class TargetAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'total_votes')
    list_filter = ('group',)

admin.site.register(Target, TargetAdmin)

from django.contrib.auth.models import Group

# グループを追加する
admin.site.unregister(Group)  # 既存のグループを削除してから再作成する
admin.site.register(Group)
