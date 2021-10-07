from django.contrib import admin
from .models import GnmUser
# Register your models here.

@admin.register(GnmUser)
class UserAdmin(admin.ModelAdmin):
    list_display=('user', 'userType','city', 'pincode')

    def userType(self, obj):
        return obj.get_user_type_display()
    userType.short_description='User Type'

    # def showGender(self, obj):
    #     return obj.get_gender_display()
    # showGender.short_description='Gender'

