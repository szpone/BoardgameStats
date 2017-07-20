from django.shortcuts import render, HttpResponse
from django.views import View
from stats.forms import SearchForm
from boardgamegeek import BGGClient

# Create your views here.

class SearchView(View):

    def get(self, request):
        form = SearchForm(request.GET)
        if form.is_valid():
            bgg = BGGClient()
            query = form.cleaned_data["query"]
            query = bgg.search(query)
            query = [q.data() for q in query]
            return render(request, "results.html",
                          {"query": query})
        else:
            return render(request, "main.html",
                          {"form": form})

