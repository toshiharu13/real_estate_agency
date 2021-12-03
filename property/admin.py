from django.contrib import admin

from .models import Flat, Claim, Owner


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    list_display = ('address', 'price', 'new_building', 'construction_year',
                    'town',)
    list_editable = ['new_building']
    search_fields = ['town', 'address']
    readonly_fields = ['created_at']
    list_filter = ('new_building', 'rooms_number', 'has_balcony',)
    raw_id_fields = ('liked_by',)


@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    list_display = ['claim_author', 'flat', 'claim_text']
    raw_id_fields = ('claim_author', 'flat')


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('owner_full_name', 'owners_phonenumber',
                    'owner_pure_phone',)
    raw_id_fields = ('ownners_flats',)
