from django.db import models


class StockStatus(models.IntegerChoices):
    IN_STOCK = 0, "In Stock"
    OUT_OF_STOCK = 1, "Out of stock"
    COMING_SOON = 2, "Coming Soon"
