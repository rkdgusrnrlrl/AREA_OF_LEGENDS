from django.contrib import admin
from .models import Member
from .models import Skill
from .models import Status

# Register your models here.


class MemberAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Member._meta.fields]


class SkillAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Skill._meta.fields]


class StatusAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Status._meta.fields]


admin.site.register(Member, MemberAdmin)

admin.site.register(Skill, SkillAdmin)

admin.site.register(Status, StatusAdmin)
