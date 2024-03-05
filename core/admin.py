from django.contrib import admin
from .models import Aspirant, VotingRecord


@admin.register(Aspirant)
class AspirantsTable(admin.ModelAdmin):
    list_display = ['name', 'aspirant_dp', 'post', 'total_votes']


@admin.register(VotingRecord)
class CastedVotesTable(admin.ModelAdmin):
    list_display = ['voter', 'elected_post']
