#***(1)Returns all Pacients from customer table
pacients = Pacient.objects.all()

#***(2)Returns first customer in table
firstCustomer = Pacient.objects.first()

#***(3)Returns last customer in table
lastCustomer = Pacient.objects.last()

#***(4)Returns single customer by name
pacientByName = Pacient.objects.get(name='Peter Piper')

#***(5)Returns single customer by id
pacientById = Pacient.objects.get(id=4)

#***(6)Returns all orders related to customer (firstCustomer variable set above)
firstPacient.order_set.all()

#***(7)***Returns orders customer name: (Query parent model values)
order = Order.objects.first()
parentName = order.customer.name

#***(8)***Returns consults from consults table with value of "Out Door" in category attribute
consults = Consult.objects.filter(category="Agendada")

#***(9)***Order/Sort Objects by id
leastToGreatest = Consult.objects.all().order_by('id')
greatestToLeast = Consult.objects.all().order_by('-id')


#***(10)***Bonus
#*Q**Returns the total count of Doctor consults
doctorOrders = Doctor.objects.first()

#*Q**Returns total count for each consult status
allConsultas = {}

for order in firstCustomer.order_set.all():
    if order.consult.name in allOrders:
        allOrders[order.consult.name] += 1
    else:
        allOrders[order.consult.name] = 1

#Returns: allOrders: {'remedio1': 1, 'dorlfex': 2}

#RELATED SET EXAMPLE
class ParentModel(models.Model):
    name = models.CharField(max_length=200, null=True)

class ChildModel(models.Model):
    parent = models.ForeignKey(ParentModel)
    name = models.CharField(max_length=200, null=True)

parent = ParentModel.objects.first()
#Returns all child models related to parent
parent.childmodel_set.all()