from django.contrib import admin

from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_filter = ('is_read', 'time_created')
    list_display = ('id', 'subject', 'message', 'first_name', 'email', 'user', 'is_read', 'time_created',)
    list_display_links = ('subject',)


admin.site.register(Feedback, FeedbackAdmin)

