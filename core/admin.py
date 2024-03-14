from django.contrib import admin
from .models import Aspirant, VotingRecord, ElectionsDate


@admin.register(Aspirant)
class AspirantsTable(admin.ModelAdmin):
    list_display = ['name', 'aspirant_dp', 'post', 'total_votes']


@admin.register(VotingRecord)
class CastedVotesTable(admin.ModelAdmin):
    list_display = ['voter', 'elected_post']


@admin.register(ElectionsDate)
class ElectionsTable(admin.ModelAdmin):
    list_display = ['election_date', 'is_done']
