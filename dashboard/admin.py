from django.contrib import admin

# Register your models here.
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    def job_duration(self, obj):
        date_format = "%H:%M:%S"
        if obj.start_at and obj.complete_at:
            total_seconds = (obj.complete_at - obj.start_at).total_seconds()
            hours, remainder = divmod(total_seconds,60*60)
            minutes, seconds = divmod(remainder,60)
            duration = ''
            if hours > 0:
                return '{}h {}m {}s'.format(int(hours),int(minutes),int(seconds))
            else:
                if minutes > 0:
                    return '{}m {}s'.format(int(minutes),int(seconds))
                else:
                    return '{}s'.format(int(seconds))
                
    empty_value_display = ''
    fields = ('test_report',)
    readonly_fields = ('test_report',)
    list_display = ('name', 'status', 'start_at', 'complete_at', 'job_duration')
