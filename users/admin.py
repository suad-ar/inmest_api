from django.contrib import admin
from users.models import Cohort, CohortMember, IMUser

# Register your models here.

admin.site.register(IMUser)
admin.site.register(Cohort)
admin.site.register(CohortMember)