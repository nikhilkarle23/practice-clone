import django_tables2 as tables

from complaint_app.models import Complaint


class ComplaintTable(tables.Table):

    class Meta:
        model = Complaint
        template_name = "django_tables2/bootstrap5.html"
        fields = (
            'pk',
            'title',
            'status',
            'created_date',
            'solved_by',
            'solved_date',
        )