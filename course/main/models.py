from django.db import models
from django.contrib.auth.models import User, Group
from django.urls import reverse


class TypeIngredient(models.Model):
   # IDtype = models.ForeignKey(Ingredients, on_delete=models.CASCADE, primary_key=True)
    IDtype = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.IDtype)

    class Meta:
        verbose_name = 'ID Типа'
        verbose_name_plural = 'ID Типа'


class Ingredients(models.Model):
    IngredientsID = models.AutoField(primary_key=True)
    NameIngredients = models.TextField()
    Kkal = models.IntegerField()
    Proteins = models.IntegerField()
    Fats = models.IntegerField()
    Carbohydrates = models.IntegerField()
    IDtype = models.ForeignKey(TypeIngredient, on_delete=models.CASCADE, null=True, blank=True)
    # IDtype = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.NameIngredients

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'


class Category(models.Model):
    CategoryID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Img = models.ImageField(height_field=None, width_field=None, null=True, blank=True)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'pk': self.pk})


class Country(models.Model):
    CountryID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class Dictionary(models.Model):
    DictionaryID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Description = models.TextField()

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = 'Определение'
        verbose_name_plural = 'Определения'


class Recipe(models.Model):
    RecipeID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Instruction = models.TextField()
    Img = models.ImageField(height_field=None, width_field=None, null=True, blank=True)
    CreateDate = models.DateTimeField(auto_now=True)
    CountryID = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def get_absolute_url(self):
        return reverse('recipe-detail', kwargs={'pk': self.pk})


class RecipeCategory(models.Model):
    ID = models.AutoField(primary_key=True)
    RecipeID = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    CategoryID = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.ID)

    class Meta:
        verbose_name = 'ID Категории'
        verbose_name_plural = 'ID Категорий'


class IngredientsRecipe(models.Model):
    ID = models.AutoField(primary_key=True)
    RecipeID = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    IngredientsID = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    CountsOnRecipe = models.CharField(max_length=100)

    def __str__(self):
        return str(self.ID)

    class Meta:
        verbose_name = 'ID Ингредиента'
        verbose_name_plural = 'ID Ингредиентов'


class RecipeUser(models.Model):
    RecipeID = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    Userid = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.RecipeID)

    class Meta:
        verbose_name = 'Автор рецепта'
        verbose_name_plural = 'Авторы рецептов'


class Recommendation(models.Model):
    RecommendationID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Instruction = models.TextField()
    Img = models.ImageField(height_field=None, width_field=None, null=True, blank=True)
    CreateDate = models.DateTimeField(auto_now=True)
    Userid = models.ForeignKey(User, on_delete=models.CASCADE)

    def str(self):
        return f"{self.Name}, {self.CreateDate}"

    class Meta:
        verbose_name = 'Совет'
        verbose_name_plural = 'Советы'


class Rating(models.Model):
    RecipeID = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    Rating = models.IntegerField()
    CountRating = models.IntegerField()

    def str(self):
        rr = Recipe.objects.get(id=self.recipeID_recipeID)
        return f"{rr.recipeID}, {self.rating}"

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'


class EquipmentTips(models.Model):
    EquipmentTipsID = models.AutoField(primary_key=True)
    EquipmentTipsName = models.CharField(max_length=100)
    EquipmentTipsDescriptions = models.TextField()
    EquipmentTipsImg = models.ImageField(height_field=None, width_field=None, null=True, blank=True)

    def __str__(self):
        return str(self.EquipmentTipsName)

    class Meta:
        verbose_name = 'Правило'
        verbose_name_plural = 'Правила'

