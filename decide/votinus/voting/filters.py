from django.contrib.admin import SimpleListFilter


class StartedFilter(SimpleListFilter):
    title = 'started'
    parameter_name = 'started'

    def lookups(self, request, model_admin):
        return [
            ('NS', 'Not started'),
            ('S', 'Started'),
            ('R', 'Running'),
            ('F', 'Finished'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'NS':
            return queryset.filter(start_date__isnull=True)
        if self.value() == 'S':
            return queryset.exclude(start_date__isnull=True)
        if self.value() == 'R':
            return queryset.exclude(start_date__isnull=True).filter(end_date__isnull=True)
        if self.value() == 'F':
            return queryset.exclude(end_date__isnull=True)
        else:
            return queryset.all()
