from django.contrib import admin
from blog.models import Post, Comment, Category, Email


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("posted", "edited")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "comment", "post", "created", "active")
    list_filter = ("created", "active")
    search_fields = ("name", "email", "comment")
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class EmailAdmin(admin.ModelAdmin):
    list_display = ("email", "subbed",)
    list_filter = ("subbed",)
    search_fields = ("email", "subbed",)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Email, EmailAdmin)