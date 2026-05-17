from django.contrib import admin
from .models import CarMake, CarModel


# Inline model: allows CarModel to appear inside CarMake admin page
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1


# Admin view for CarModel (standalone view in admin)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year')
    list_filter = ('type', 'year', 'car_make')
    search_fields = ('name',)


# Admin view for CarMake (includes inline CarModel editing)
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines = [CarModelInline]


# Register models
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)