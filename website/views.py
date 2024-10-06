from math import ceil
from django.shortcuts import render
from .models import Propertie

def index(request):
    allProp = []
    
    # Get distinct property types to categorize properties
    property_types = Propertie.objects.values('property_type').distinct()

    for prop_type in property_types:
        # Filter properties based on the current property type
        properties = Propertie.objects.filter(property_type=prop_type['property_type'])
        
        n = len(properties)  # Count of properties in this category
        nSlides = n // 4 + ceil((n / 4) - (n // 4))  # Calculate number of slides
        allProp.append([properties, nSlides])  # Append properties and number of slides

    params = {'allProp': allProp}
    
    return render(request, "index.html", params)