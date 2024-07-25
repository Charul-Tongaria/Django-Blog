from django.contrib import admin
from .models import Post,Category,Tag,Comment
from django.urls import reverse
from django.contrib.auth.models import User
import csv
from django.http import HttpResponse


class UserAdmin(admin.ModelAdmin):
    actions = ["export_as_csv"]

    def export_as_csv(self,request,queryset):
        meta=self.model._meta
        field_names=[field.name for field in meta.fields]

        response=HttpResponse(content_type='text/csv')
        response['Content-Disposition']='attachment; filename={}.csv'.format(meta)
        writer=csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row=writer.writerow([getattr(obj,field)for field in field_names])
        return response

    export_as_csv.short_description="Export  Selected"


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    actions = ["export_as_csv"]
    list_display = ("author", "title","created_date","published_date",'image')
    list_filter = ('published_date',)
    view_on_site = True
    def view_on_site(self,obj):
        from django.urls import reverse
        return reverse('blog:post_detail',kwargs={'slug':obj.slug})
    pass
    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    actions = ["export_as_csv"]
    list_display = ("name", "created_date")
    list_filter = ('created_date',)

    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    actions = ["export_as_csv"]
    list_display = ("name","created_date")
    list_filter = ('created_date',)
    
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    actions = ["export_as_csv"]
    list_display = ('text', 'author', 'created_on','post')
    list_filter = ('created_on',)


class PersonAdmin(admin.ModelAdmin):
    actions = ["export_as_csv"]
    def view_on_site(self,obj):
        url=reverse('post_detail',kwargs={'slug':obj.slug})
        return 'http://127.0.0.1:8000/' + 'post/<slug:slug>/'

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
