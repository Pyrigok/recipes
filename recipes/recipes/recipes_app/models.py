from django.db import models


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)


class Vegetable(BaseModel):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500, null=True, blank=True)
    weight = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Vegetable"
        verbose_name_plural = "Vegetables"

    def __str__(self):
        return self.title


class Fruit(BaseModel):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500, null=True, blank=True)
    weight = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Fruit"
        verbose_name_plural = "Fruits"

    def __str__(self):
        return self.title


class Meat(BaseModel):
    class MeatType(models.TextChoices):
        Fillet = "філе"
        NECK = "шия"
        HAM = "шинка"
        TENDERLOIN = "вирізка"
        LEG = "нога"
        THIGH = "бедро"
        RIBS = "ребро"

    title = models.CharField(max_length=50)
    type = models.CharField(choices=MeatType.choices, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    weight = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Meat"
        verbose_name_plural = "Meat"

    def __str__(self):
        return self.title


class Sauce(BaseModel):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500, null=True, blank=True)
    receipt = models.TextField(max_length=500, null=True, blank=True)
    weight = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Souce"
        verbose_name_plural = "Souce"

    def __str__(self):
        return self.title


class Recipe(BaseModel):

    class RecipeType(models.TextChoices):
        SALAD = "Salad"
        SOUP = "Soup"
        MAIN_COURSE = "Main course"
        DESSERT = "Dessert"

    class CookingType(models.TextChoices):
        MIX = "Mix"
        Boil = "Boil"


    title = models.CharField(max_length=50)
    type = models.CharField(choices=RecipeType.choices)
    description = models.TextField(max_length=500, null=True, blank=True)
    vegetables = models.ManyToManyField(Vegetable, related_name="recipe", null=True, blank=True)
    fruits = models.ManyToManyField(Fruit, related_name="recipe", null=True, blank=True)
    meat = models.ManyToManyField(Meat, related_name="recipe", null=True, blank=True)
    sauce = models.ManyToManyField(Sauce, related_name="recipe", null=True, blank=True)
    cooking_type = models.CharField(choices=CookingType.choices)
    receipt = models.TextField(max_length=5000, null=True, blank=True)
    # author = models.ForeignKey(User, on_delete=models.SET_NULL)
    is_allowed_for_pregnant =  models.BooleanField(default=False)
    price = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "Dish"
        verbose_name_plural = "Dishes"

    def __str__(self):
        return self.title


class Image(BaseModel):
    receipt = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    picture = models.ImageField()

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"

    def __str__(self):
        return self.receipt.title
