from .models import Male, Female, Dewormer, Drug, Acaricide, Employee, Feed, Vaccine, Others, MSold, FSold, PreviousProfit
import datetime as dt


class Add_On_1:
    def profit(self):
        totals = self.totals()

        return int(totals[0] - totals[1])

    def totals(self):
        expenditure = [Acaricide, Dewormer, Vaccine, Feed, Drug, Others, Employee]
        incomes = [MSold, FSold]
        total_income, total_expenditure = 0, 0

        for e in expenditure:
            m = e.objects.all()
            for i in m:
                if e == Employee:
                    total_expenditure += i.salary
                else:
                    total_expenditure += i.price

        for income in incomes:
            m = income.objects.all()
            for i in m:
                total_income += i.price

        return [total_income, total_expenditure]

    def is_loss(self):
        if self.profit() < 0:
            return True
        else:
            return False

    def model_totals(_list, model):
        total = 0
        for i in _list:
            if model.lower() == "employee":
                total += i.salary
            else:
                total += i.price
        return total

    def is_balanced(self):
        if self.profit() == 0:
            return True
        else:
            return False

    def percentage(self):
        percent = 0
        if PreviousProfit.objects.filter(name="Total"):
            PP = PreviousProfit.objects.get(name="Total")
            if PP.amount != self.profit():
                percent = self.profit() / abs(PP.amount) * 100
                PP = PreviousProfit(name="Total", amount=self.profit(), percent=int(percent))
                PP.save()
        else:
            PP = PreviousProfit(name="Total", amount=self.profit())
            PP.save()
        return PP.percent

    def total_expenditure():
        models = [Acaricide, Dewormer, Vaccine, Feed, Drug, Others, Employee]
        totals = []

        for e in models:
            dict = {
                "name": f"{e.__name__}",
                "total": 0,
            }
            m = e.objects.all()
            for i in m:
                if e == Employee:
                    dict["total"] += i.salary
                else:
                    dict["total"] += i.price
            totals.append(dict)
        return totals

    def model_expenditure_choice(target):
        if target:
            if target.lower() == "acaricide":
                model = Acaricide.objects.all()
                return {
                    "name": "Acaricide",
                    "total": Add_On_1.model_totals(model, target),
                    "data": model
                }
            elif target.lower() == "vaccine":
                model = Vaccine.objects.all()
                return {
                    "name": "Vaccine",
                    "total": Add_On_1.model_totals(model, target),
                    "data": model
                }
            elif target.lower() == "employee":
                model = Employee.objects.all()
                return {
                    "name": "Employees",
                    "total": Add_On_1.model_totals(model, target),
                    "data": model
                }
            elif target.lower() == "feeds":
                model = Feed.objects.all()
                return {
                    "name": "Feeds",
                    "total": Add_On_1.model_totals(model, target),
                    "data": model
                }
            elif target.lower() == "drug":
                model = Drug.objects.all()
                return {
                    "name": "Drugs",
                    "total": Add_On_1.model_totals(model, target),
                    "data": model
                }
            elif target.lower() == "others":
                model = Others.objects.all()
                return {
                    "name": "Others",
                    "total": Add_On_1.model_totals(model, target),
                    "data": model
                }
            elif target.lower() == "dewormer":
                model = Dewormer.objects.all()
                return {
                    "name": "Dewormer",
                    "total": Add_On_1.model_totals(model, target),
                    "data": model
                }
        else:
            return None

    def exp_totals(_list):
        total = 0
        for i in _list:
            total += i["total"]
        return total

    def piechart(self):
        total_income, total_expenditure = self.totals()
        labels = ["Total Income", "Total Expenditure"]
        data = [total_income, total_expenditure]

        return labels, data
    
    def available(check_func):
        male_num = 0
        female_num = 0
        for i in Male.objects.all():
            if check_func(i.id):
                male_num += 1
        
        for i in Female.objects.all():
            if check_func(i.id):
                female_num += 1
                
        return male_num, female_num
    
    def is_pregnant():
        pregnant_num = 0
        for i in Female.objects.all():
            if i.is_pregnant:
                pregnant_num += 1
        return pregnant_num
