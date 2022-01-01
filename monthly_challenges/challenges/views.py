from django.http import response
from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect ,Http404
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.
monthly_challenges = {

    "january": "This month is january",
    "february": "This is february",
    "march": "This is march",
    "april": "This is april",
    "may": "This is may",
    "june": "This is june",
    "july": "This is july",
    "August": "This is August",
    "septemper": "This is septemper",
    "october": "This is october",
    "november": "This is november",
    "december": None,

}


def index(request):
    # list_items = ""
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })

    # for month in months:
    #     capitalized_month = month.capitalize()

    # /challenges/january
    # month_path = reverse("month-challenge", args=[month])
    # list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)


def monthly_callenge_number(request, month):

    months = list(monthly_challenges.keys())
    if month > len(months):
        redirect_month = months[month-1]
        redirect_path = reverse("month-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    else:
        return HttpResponseNotFound("This is not a valid month number")


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })
        # temp_string = render_to_string("challenges/challenge.html")
        # return HttpResponse(temp_string)
    except:
        # response_data = render_to_string("404.html")
        # return HttpResponse(response_data)
        raise Http404()
