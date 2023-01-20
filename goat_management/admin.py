from django.contrib import admin
from .models import Female, Male, Todo, Mating, FSold, MSold, FDead, MDead, Employee
from .models import Dewormer, Drug, Acaricide, Employee, Feed, Vaccine, Others, PreviousProfit

# Register your models here.
admin.site.register(Female)
admin.site.register(Male)
admin.site.register(Todo)
admin.site.register(Mating)
admin.site.register(Employee)
admin.site.register(FSold)
admin.site.register(MSold)
admin.site.register(FDead)
admin.site.register(Dewormer)
admin.site.register(Drug)
admin.site.register(Acaricide)
admin.site.register(Feed)
admin.site.register(Vaccine)
admin.site.register(Others)
admin.site.register(PreviousProfit)
