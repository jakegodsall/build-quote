from django.db import models

class Address(models.Model):
    street = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    postcode = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.street}, {self.postcode}"
    

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"
    

class Spec(models.Model):
    detail = models.CharField(max_length=200)


class Job(models.Model):
    class Status(models.TextChoices):
        PENDING = 'P', 'Pending'
        IN_PROGRESS = 'I', 'In Progress'
        COMPLETE = 'C', 'Complete'
        REJECTED = 'R', 'Rejected'
    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=1, choices = Status.choices, default=Status.PENDING)
    price = models.PositiveIntegerField()
    price_includes_tax = models.BooleanField()
    quotation_date = models.DateField()
    invoice_date = models.DateField()

    def __str__(self)
        return f"{self.customer}, {self.address.postcode}"


class Quotation(models.Model):
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    job = models.OneToOneField(Job, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Quotation #{self.id} ({self.job.address.postcode})"

class Invoice(models.Model):
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    job = models.OneToOneField(Job, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Invoice #{self.id} ({self.job.address.postcode})"