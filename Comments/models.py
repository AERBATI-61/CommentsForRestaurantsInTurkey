from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

week_days ={
    ("Pazartesi", "Pazartesi"),
    ("Salı", "salı"),
    ("Çarşamba", "çarşamba"),
    ("Perşembe", "Perşembe"),
    ("Cuma", "Cuma"),
    ("Cumartesi", "Cumartesi"),
    ("Pazar", "Pazar"),
}



mekan_types = {
    ("Kafe", "Kafe"),
    ("Restorant", "Restorant"),
    ("Sokak Yemekleri", "Sokak Yemekleri"),
    ("Akşam yemek restorantları", "Akşam yemek restorantları"),
    ("Fast-Casual Restoranlar", "Fast-Casual Restoranlar"),
}









class City(models.Model):
    destination                   = models.ForeignKey('Destination', on_delete=models.CASCADE, blank=False, null=False)
    sehir_name                    = models.CharField(max_length=64, blank=False, null=False)

    def __str__(self):
        return self.sehir_name


    class Meta:
        verbose_name = "District"






class Destination(models.Model):
    destination                 = models.CharField(max_length=64, blank=False, null=False)

    def __str__(self):
        return self.destination

    class Meta:
        verbose_name = "City"




class Food(models.Model):
    restaurant           = models.ForeignKey('Restaurants', on_delete=models.CASCADE, blank=False, null=False)
    name                 = models.CharField(max_length=64, blank=False, null=False)
    price                = models.IntegerField(blank=False, null=False)
    image                = models.ImageField(upload_to='static/assets/images/all/', blank=False, null=False)
    description          = models.TextField()

    def __str__(self):
        return f'{self.name}-{self.restaurant.destination.destination}'



class Restaurants(models.Model):
    restaurant_name             = models.CharField(max_length=64, blank=True, null=True)
    image                       = models.ImageField(upload_to='static/assets/images/all/', blank=False, null=False)
    destination                 = models.ForeignKey(Destination, on_delete=models.CASCADE, blank=False, null=False)
    city                        = models.ForeignKey(City, on_delete=models.CASCADE, blank=False, null=False)
    service                     = models.BooleanField(blank=True, null=True)
    active_date                 = models.TimeField()
    inactive_date               = models.TimeField()
    inactive_day                = models.CharField(max_length=64, blank=True, null=True, choices=week_days)
    mekan_type                  = models.CharField(max_length=64, blank=True, null=True, choices=mekan_types)
    description                 = models.TextField()



    def __str__(self):
        return f'{self.restaurant_name} - {self.destination.destination}'




class Comment(models.Model):
    restaurant              = models.ForeignKey(Restaurants, on_delete=models.CASCADE, blank=False, null=False)
    name                    = models.CharField(max_length=64, blank=False, null=False)
    email                   = models.EmailField(max_length=128, blank=False, null=False)
    description             = models.TextField()
    date                    = models.DateTimeField(auto_now_add=True)
    waiter                  = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    park                    = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    comfortable             = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    air_condition           = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    cleaning                = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    flavor                  = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    price                   = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    menu_variety            = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])


    def __str__(self):
        return f'{self.name} - {self.email}'



class AboutMe(models.Model):
    name                = models.CharField(max_length=128, blank=False, null=False)
    lastname            = models.CharField(max_length=128, blank=False, null=False)
    department          = models.CharField(max_length=128, blank=False, null=False)
    age                 = models.IntegerField()
    phone               = models.CharField(max_length=32, blank=False, null=False)
    email               = models.EmailField(max_length=64, blank=False, null=False)
    image               = models.ImageField(upload_to='static/assets/images/all/')
    description         = models.TextField()
    address             = models.TextField()

    def __str__(self):
        return f'{self.name} - {self.lastname} - {self.email}'