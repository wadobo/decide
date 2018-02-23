from django.contrib import admin

from .models import QuestionOption
from .models import Question
from .models import Voting


class QuestionOptionInline(admin.TabularInline):
    model = QuestionOption


class QuestionAdmin(admin.ModelAdmin):
    inlines = [QuestionOptionInline]


class VotingAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date')
    readonly_fields = ('start_date', 'end_date', 'pub_key')


admin.site.register(Voting, VotingAdmin)
admin.site.register(Question, QuestionAdmin)
