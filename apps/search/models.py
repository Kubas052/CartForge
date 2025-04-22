from django.db import models
from apps.accounts.models import UserProfile
from apps.catalog.models import Product

class SearchQuery(models.Model):
    user = models.ForeignKey(UserProfile, null=True, blank=True, on_delete=models.SET_NULL)
    query = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    results_count = models.PositiveIntegerField()

class SearchClick(models.Model):
    search = models.ForeignKey(SearchQuery, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    position = models.PositiveIntegerField()