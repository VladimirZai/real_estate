from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    model = Flat.owned_by.through
    raw_id_fields = ('owner', 'flat')
    list_display = ('owner')

@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', )
    readonly_fields = ["created_at"]
    list_display = ('address', 'price', 'new_building', 'construction_year', )
    list_editable = ('new_building', )
    list_filter = ('new_building', 'rooms_number', 'has_balcony', )
    raw_id_fields = ('liked_by', )
    inlines = [OwnerInline]

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat', )


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phonenumber', )
    exclude = ('owned_flats', )
    inlines = [OwnerInline]
