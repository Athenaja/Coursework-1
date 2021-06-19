from django.db import models


class Ingredients(models.Model):
    IngredientsID = models.AutoField(primary_key=True)
    NameIngredients = models.TextField()
    Kkal = models.IntegerField()
    Proteins = models.IntegerField()
    Fats = models.IntegerField()
    Carbohydrates = models.IntegerField()

    def __str__(self):
        return self.NameIngredients

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'


class Category(models.Model):
    CategoryID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Country(models.Model):
    CountryID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class Recipe(models.Model):
    RecipeID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Instruction = models.TextField()
    Img = models.ImageField(height_field=None, width_field=None, null=True, blank=True)
    CreateDate = models.DateTimeField(auto_now=True)
    CountryID = models.ForeignKey(Country, on_delete=models.CASCADE)
    CategoryID = models.ForeignKey(Category, on_delete=models.CASCADE)
    IngredientsID = models.ForeignKey(Ingredients, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Name}, {self.Instruction}"

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'


class RecipeUser(models.Model):
    RecipeID = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    # Userid = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Автор рецепта'
        verbose_name_plural = 'Авторы рецептов'


class Recommendation(models.Model):
    RecommendationID = models.AutoField(primary_key=True)
    # UserID = models.ForeignKey(, on_delete=models.CASCADE)

    def str(self):
        return

    class Meta:
        verbose_name = 'Совет'
        verbose_name_plural = 'Советы'


class RecommendationUser(models.Model):
    RecommendationID = models.ForeignKey(Recommendation, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Instruction = models.TextField()
    Img = models.ImageField(height_field=None, width_field=None, null=True, blank=True)
    CreateDate = models.DateTimeField(auto_now=True)

    def str(self):
        return f"{self.Name}, {self.CreateDate}"

    class Meta:
        verbose_name = 'Автор совета'
        verbose_name_plural = 'Авторы совета'


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