from django.db import models
from django.utils.datetime_safe import datetime
import datetime as dt

# Create your models here.
kinds_male = [("nnume", "nnume"), ("ndaawo", "ndaawo"), ("kalume", "kalume")]
kinds_female = [("mugongo", "mugongo"), ("nduusi",
                                         "nduusi"), ("kaluusi", "kaluusi")]
genders = [("M", "Male"), ("F", "Female")]


class Male(models.Model):
    id = (models.CharField(max_length=255, primary_key=True))
    mother = models.ForeignKey(
        "Female", on_delete=models.SET_NULL, null=True, default=None, blank=True)
    father = models.ForeignKey(
        "Male", on_delete=models.SET_NULL, null=True, default=None, blank=True)
    dob = models.DateField(auto_now=False, null=True)
    category = models.CharField(max_length=10, choices=kinds_male)

    def get_class_name(self):
        return self.__class__.__name__

    def save(self):
        if Male.objects.filter(id=self.id):
            self.category = self.category
            self.father = self.father
            self.mother = self.mother
            self.dob = self.dob
            super(Male, self).save()
        else:
            self.id = f"G-M-{self.dob.year}-JPR-" + self.id
            if Male.objects.filter(id=self.id):
                raise Exception("Pk already exists")
            super(Male, self).save()

        if self.father and self.mother:
            mate = Mating(male=self.father, female=self.mother)
            mate.save()
        elif self.father:
            mate = Mating(male=self.father)
            mate.save()
        elif self.mother:
            mate = Mating(female=self.mother)
            mate.save()
        else:
            print("Failed")


class Female(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    mother = models.ForeignKey(
        "Female", on_delete=models.SET_NULL, null=True, default=None, blank=True)
    father = models.ForeignKey(
        "Male", on_delete=models.SET_NULL, null=True, default=None, blank=True)
    is_pregnant = models.BooleanField(default=False)
    dob = models.DateField(auto_now=False, null=True)
    estDob = models.DateField(
        auto_now=False, null=True, blank=True, default=None)
    gestdate = models.DateField(
        auto_now=False, null=True, blank=True, default=dt.datetime.now())
    category = models.CharField(max_length=10, choices=kinds_female)

    def get_class_name(self):
        return self.__class__.__name__

    def save(self):
        if Female.objects.filter(id=self.id):
            self.is_pregnant = self.is_pregnant
            self.category = self.category
            self.father = self.father
            self.mother = self.mother
            self.dob = self.dob
            if self.is_pregnant:
                self.estDob = dt.timedelta(hours=3600) + self.gestdate
            else:
                self.estDob = None
                self.gestdate = None
            super(Female, self).save()
        else:
            self.id = f"G-F-{self.dob.year}-JPR-" + self.id
            if Female.objects.filter(id=self.id):
                raise Exception("Pk already exists")
            if self.is_pregnant:
                self.estDob = dt.timedelta(hours=3600) + self.gestdate
                print(self.estDob)
            super(Female, self).save()

        if self.father and self.mother:
            mate = Mating(male=self.father, female=self.mother)
            mate.save()
        elif self.father:
            mate = Mating(male=self.father)
            mate.save()
        elif self.mother:
            mate = Mating(female=self.mother)
            mate.save()
        else:
            print("Failed")


class Todo(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    complete = models.BooleanField(default=False)


class Mating(models.Model):
    male = models.ForeignKey(Male, on_delete=models.CASCADE, blank=True)
    female = models.ForeignKey(Female, on_delete=models.CASCADE, blank=True)

    def check_dead(self):
        if MDead.objects.filter(m_id=self.male.id) and FDead.objects.filter(f_id=self.female.id):
            return "Both"
        if MDead.objects.filter(m_id=self.male.id):
            return 'Male'
        if FDead.objects.filter(f_id=self.female.id):
            return "Female"
        return False


class Employee(models.Model):
    name = models.CharField(max_length=50)
    salary = models.IntegerField()
    last_payment = models.DateField(
        auto_now=False, blank=True, null=True, default=dt.date.today())
    salary_paid = models.BooleanField()

    def due(self):
        if self.salary_paid:
            self.last_payment = dt.date.today()
            self.salary_paid = False

        if (dt.date.today() - self.last_payment) >= dt.timedelta(days=30):
            self.due_date = self.last_payment + dt.timedelta(hours=720)

        self.save()

    def get_class_name(self):
        return self.__class__.__name__

    def price(self):
        return self.salary


class MSold(models.Model):
    m_id = models.ForeignKey(Male, on_delete=models.CASCADE, primary_key=True)
    price = models.IntegerField()
    DoS = models.DateField(auto_now=False, null=True, blank=True)


class FSold(models.Model):
    f_id = models.ForeignKey(
        Female, on_delete=models.CASCADE, primary_key=True)
    price = models.IntegerField()
    DoS = models.DateField(auto_now=False, null=True, blank=True)


class MDead(models.Model):
    m_id = models.ForeignKey(Male, models.CASCADE, primary_key=True)
    DoD = models.DateField(auto_now=False, blank=True, null=True)

    def get_class_name(self):
        return self.__class__.__name__


class FDead(models.Model):
    f_id = models.ForeignKey(Female, models.CASCADE, primary_key=True)
    DoD = models.DateField(auto_now=False, blank=True, null=True)

    def get_class_name(self):
        return self.__class__.__name__


class Dewormer(models.Model):
    name = models.CharField(max_length=250)
    amount = models.IntegerField()
    price = models.IntegerField()
    date = models.DateField(auto_now=False, blank=True, null=True)

    def get_class_name(self):
        return self.__class__.__name__


class Acaricide(models.Model):
    name = models.CharField(max_length=250)
    amount = models.IntegerField()
    price = models.IntegerField()
    date = models.DateField(auto_now=False, blank=True, null=True)

    def get_class_name(self):
        return self.__class__.__name__


class Vaccine(models.Model):
    name = models.CharField(max_length=250)
    amount = models.IntegerField()
    price = models.IntegerField()
    date = models.DateField(auto_now=False, blank=True, null=True)

    def get_class_name(self):
        return self.__class__.__name__


class Feed(models.Model):
    name = models.CharField(max_length=250)
    amount = models.IntegerField()
    price = models.IntegerField()
    date = models.DateField(auto_now=False, blank=True, null=True)

    def get_class_name(self):
        return self.__class__.__name__


class Drug(models.Model):
    name = models.CharField(max_length=250)
    amount = models.IntegerField()
    price = models.IntegerField()
    date = models.DateField(auto_now=False, blank=True, null=True)

    def get_class_name(self):
        return self.__class__.__name__


class Others(models.Model):
    name = models.CharField(max_length=250)
    amount = models.IntegerField()
    price = models.IntegerField()
    date = models.DateField(auto_now=False, blank=True, null=True)

    def get_class_name(self):
        return self.__class__.__name__


class PreviousProfit(models.Model):
    name = models.CharField(max_length=250, primary_key=True)
    amount = models.IntegerField()
    percent = models.IntegerField(default=0)

    def get_class_name(self):
        return self.__class__.__name__
