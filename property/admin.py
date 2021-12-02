from django.contrib import admin

from .models import Flat, Claim


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    list_display = ['address', 'price', 'new_building', 'construction_year',
                    'town']
    list_editable = ['new_building']
    search_fields = ['town', 'address']
    readonly_fields = ['created_at']
    list_filter = ('new_building', 'rooms_number', 'has_balcony',)


@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    list_display = ['claim_author', 'flat', 'claim_text']
    raw_id_fields = ('claim_author', 'flat')
