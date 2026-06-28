from django.db import models

class Book(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    thumbnailUrl = models.CharField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

class Branch(models.Model):
    branchName = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=20)
    phone = models.CharField(max_length=30)

    def __str__(self):
        return self.branchName

class Inventory(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.book.title} @ {self.branch.branchName}'
