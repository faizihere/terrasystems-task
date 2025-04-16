from django.db import models

"""
# A MIGRATIONS WITH A E
# REMEMBER TO KEEP 0007,0008 INSTANCES ELSE THE HOME PAGE WILL LOOK EMPTY UNTIL WE ADD SOME CONTENT THROUGH EDIT PAGE.
"""

# PURPOSE : TO MANAGE THE CONTENTS OF THE LANDING PAGE/HOMEPAGE
class HomePageContent(models.Model):
    # Hero Section
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    cta_button = models.CharField(max_length=100)

    # Feature Section
    feature_title = models.CharField(max_length=200)
    feature_description = models.CharField(max_length=500)
    feature_button = models.CharField(max_length=100)
    
    # Footer
    footer_tagline = models.CharField(max_length=500)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20)

    def __str__(self):
        return "Homepage Content"

# PURPOSE : TO MANAGE THE CONTENTS OF THE PRICING PLANS
class PricingPlan(models.Model):
    title = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    features = models.CharField(max_length=500)

    def __str__(self):
        return self.title
