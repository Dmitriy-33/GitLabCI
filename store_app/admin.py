from django.contrib import admin
from .models import Product


@admin.action(description="Увеличить цену на 10%")
def increase_price_10(modeladmin, request, queryset):
    for product in queryset:
        product.price = product.price * 1.1
        product.save()
    modeladmin.message_user(
        request,
        "Цены на выбранные товары увеличены на 10%"
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'description')
    actions = [increase_price_10]

    # Дополнительные настройки формы в админке
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'price')
        }),
    )

    def get_queryset(self, request):
        return super().get_queryset(request)


admin.site.register(Product, ProductAdmin)