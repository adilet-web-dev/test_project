from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="subcategories"
    )

    class Meta:
        verbose_name_plural = "subcategories"

    def __str__(self):
        return self.name


class Announcement(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField(auto_now_add=True, blank=True)
    image = models.ImageField()

    subcategory = models.ForeignKey(
        Subcategory,
        on_delete=models.CASCADE,
        related_name="announcements"
    )
