from django.contrib import admin
from admin_cus.models import sample

@admin.register(sample)
@admin.action(description='Mark selected stories as published')
class Show_detail(admin.ModelAdmin):
    def name_count(self, obj):  
        return obj.email.count('@')

    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):
        queryset.update(is_sample=False)
    export_as_csv.short_description = "Export Selected"

    actions = ["sample"]
    def sample(self, request, queryset):
        queryset.update(is_sample=True)
    

    list_display = ('name', 'is_sample', 'name_count', 'phone', 'email',)
    list_filter = ('is_sample',)
    actions = ('sample', 'export_as_csv')

    
 

# admin.site.register(sample, Show_detail)
admin.site.site_header = "Kanhaiya Admin" #
admin.site.site_title = "Kanhaiya Admin Portal"
admin.site.index_title = "Welcome To Kanhaiya Admin"


# Register your models here.
