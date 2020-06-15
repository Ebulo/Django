from django.db import models


class product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=30)
    category = models.CharField(max_length=60, default="")
    SubCategory = models.CharField(max_length=60, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=480)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name


class Contact(models.Model):
        msg_id = models.AutoField(primary_key=True)
        name = models.CharField(max_length=60)
        Email = models.CharField(max_length=60, default="")
        phone = models.CharField(max_length=20, default="")
        desc = models.CharField(max_length=1000)

        def __str__(self):
            return self.name
