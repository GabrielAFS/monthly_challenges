from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": None,
}

def index(request):
    # Solution 1
    # list_items = ''.join(list(map(lambda m: f"<li><a href={reverse('month-challenge', args=[m])}>{m.capitalize()}</a></li>", months)))

    # Solution 2
    # for month in months:
    #     list_items += f"<li><a href={reverse('month-challenge', args=[month])}>{month.capitalize()}</a></li>"

    # Solution 3
    # list_items = ''.join([f"<li><a href={reverse('month-challenge', args=[m])}>{m.capitalize()}</a></li>" for m in months])
    # return HttpResponse(f"<ul>{list_items}</ul>")

    # Solution 4 with DTL
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", { "months": months })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    # build a url to the assigned name
    redirect_path = reverse("month-challenge", args=[redirect_month]) # e.g.: challenges/<month>
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        context = { "text": challenge_text, "month": month.capitalize() }
        return render(request, "challenges/challenge.html", context)

        # Solution 2
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
