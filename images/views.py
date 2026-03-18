
from django.shortcuts import render

from .models import Property, OffplanProject, ContactEnquiry, PropertyListingRequest, Community, Insight
from django.core.paginator import Paginator
from django.db.models import Q


def index(request):

    properties = Property.objects.filter(is_featured=True).order_by("-created_at")[:6]

    communities = Community.objects.filter(featured=True)[:6]

    insights = Insight.objects.order_by("-created_at")[:3]

    context = {
        "properties": properties,
        "communities": communities,
        "insights": insights
    }

    return render(request, "index.html", context)

def abooutus(request):
    return render(request, 'abooutus.html')
from django.db.models import Q


from django.core.paginator import Paginator

def buy(request):

    properties = Property.objects.filter(listing_type="buy")

    keyword = request.GET.get("keyword")
    property_type = request.GET.get("property_type")
    price = request.GET.get("price")
    beds = request.GET.get("beds")
    size = request.GET.get("size")
    sort = request.GET.get("sort")
    insights = Insight.objects.order_by("-created_at")[:3]

    if keyword:
        properties = properties.filter(
            Q(title__icontains=keyword) |
            Q(location__icontains=keyword) |
            Q(property_type__icontains=keyword)
        )

    if property_type:
        properties = properties.filter(property_type=property_type)

    if price:
        properties = properties.filter(price__lte=price)

    if beds:
        properties = properties.filter(bedrooms__gte=beds)

    if size:
        properties = properties.filter(area_sqft__gte=size)

    if sort == "price_low":
        properties = properties.order_by("price")

    elif sort == "price_high":
        properties = properties.order_by("-price")

    else:
        properties = properties.order_by("-created_at")


    # PAGINATION
    paginator = Paginator(properties, 6)  # show 6 properties per page
    page_number = request.GET.get("page")
    properties = paginator.get_page(page_number)


    context = {
        "properties": properties,
        "insights": insights
    }

    return render(request, "buy.html", context)


def communities(request):

	communities = Community.objects.all()

	featured_community = Community.objects.filter(featured=True).first()

	return render(request, "communities.html", {
		"communities": communities,
		"featured_community": featured_community
	})


def contactus(request):

	if request.method == "POST":

		full_name = request.POST.get("full_name")
		email = request.POST.get("email")
		phone = request.POST.get("phone")
		interest = request.POST.get("interest")
		location = request.POST.get("location")
		message = request.POST.get("message")

		ContactEnquiry.objects.create(
			full_name=full_name,
			email=email,
			phone=phone,
			interest=interest,
			location=location,
			message=message
		)

	return render(request, "contactus.html")

def listwithus(request):

	if request.method == "POST":

		full_name = request.POST.get("full_name")
		email = request.POST.get("email")
		phone = request.POST.get("phone")
		property_location = request.POST.get("property_location")
		property_type = request.POST.get("property_type")
		details = request.POST.get("details")

		PropertyListingRequest.objects.create(
			full_name=full_name,
			email=email,
			phone=phone,
			property_location=property_location,
			property_type=property_type,
			details=details
		)

	return render(request, "listwithus.html")


def properties(request, id):

    property = Property.objects.get(id=id)

    return render(request, "properties.html", {
        "property": property
    })

def rent(request):

    properties = Property.objects.filter(listing_type="rent")

    keyword = request.GET.get("keyword")
    property_type = request.GET.get("property_type")
    price = request.GET.get("price")
    beds = request.GET.get("beds")
    size = request.GET.get("size")
    sort = request.GET.get("sort")

    if keyword:
        properties = properties.filter(
            Q(title__icontains=keyword) |
            Q(location__icontains=keyword) |
            Q(property_type__icontains=keyword)
        )

    if property_type:
        properties = properties.filter(property_type=property_type)

    if price:
        properties = properties.filter(price__lte=price)

    if beds:
        properties = properties.filter(bedrooms__gte=beds)

    if size:
        properties = properties.filter(area_sqft__gte=size)

    if sort == "price_low":
        properties = properties.order_by("price")

    elif sort == "price_high":
        properties = properties.order_by("-price")

    else:
        properties = properties.order_by("-created_at")


    # PAGINATION
    paginator = Paginator(properties, 6)   # 6 properties per page
    page_number = request.GET.get("page")
    properties = paginator.get_page(page_number)
    insights = Insight.objects.order_by("-created_at")[:3]


    context = {
        "properties": properties,
   		"insights": insights

    }

    return render(request, "rent.html", context)

# offplan 

def offplan(request):

	projects = OffplanProject.objects.all()
	insights = Insight.objects.order_by("-created_at")[:3]
	keyword = request.GET.get("keyword")
	min_price = request.GET.get("min_price")
	max_price = request.GET.get("max_price")
	unit_types = request.GET.get("unit_types")
	development_type = request.GET.get("development_type")
   		 


	if keyword:
		projects = projects.filter(
			Q(title__icontains=keyword) |
			Q(location__icontains=keyword) |
			Q(developer__icontains=keyword)
		)

	if min_price:
		projects = projects.filter(starting_price__gte=min_price)

	if max_price:
		projects = projects.filter(starting_price__lte=max_price)

	if unit_types:
		projects = projects.filter(unit_types__icontains=unit_types)

	if development_type:
		projects = projects.filter(development_type=development_type)

	projects = projects.order_by("-created_at")

	return render(request, "offplan.html", {
		"projects": projects,
        "insights": insights
	})

def offplan_details(request, id):

	project = OffplanProject.objects.get(id=id)

	return render(request, "offplandetails.html", {
		"project": project
	})


def insights(request):

    posts = Insight.objects.all().order_by("-created_at")

    return render(request, "insights.html", {
        "posts": posts
    })

def insight_detail(request, slug):

    post = Insight.objects.get(slug=slug)

    return render(request, "insight_detail.html", {
        "post": post
    })