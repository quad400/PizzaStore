from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import (
            Category, Product, 
            Gallery, Image, 
            Slideshow,Bookings, 
            NewsLetter,Settings,
            AboutUs, Team,
            History, IconClassic,
            UserProfile,Comment,
            Cart, Order
)


class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = 'title'
    list_display = ['tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count', 'image_tag']
    list_display_links = ['indented_title']
    prepopulated_fields = {'slug': ('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(qs, Product, 
                        'category', 'products_cumulative_count', cumulative=True)
        
        qs = Category.objects.add_related_count(qs, Product, 
                        'category', 'products_count', cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price', 'image_tag']
    readonly_fields = ('image_tag',)
    prepopulated_fields = {'slug': ('title',)}


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    # list_display = ['title', 'image']

class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag']
    inlines = [ImageInline]


class BookingAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['topic', 'sub_topic', 'image_tag']

class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'post', 'image_tag']

class IconClassicAdmin(admin.ModelAdmin):
    list_display = ['title', 'desc']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'subject']


admin.site.register(Category,CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Bookings, BookingAdmin)
admin.site.register(Slideshow)
admin.site.register(NewsLetter)
admin.site.register(Settings)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(IconClassic, IconClassicAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(History)
admin.site.register(UserProfile)
admin.site.register(Cart)
admin.site.register(Order)
