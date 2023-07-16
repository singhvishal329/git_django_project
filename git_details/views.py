from django.http import HttpResponse
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

def home(request):
    return render(request, 'index.html')

def details(request):
    if (request.method == "POST"):
        id = request.POST["userid"]

        # Beautiful soup
        url = f"https://github.com/{id}?tab=repositories"
        urls = f"https://github.com/{id}"
        data = requests.get(url)
        soup = BeautifulSoup(data.content, "html.parser")
        
        repo = soup.find_all("a",{"itemprop":"name codeRepository"})
        mode = soup.find_all("span",{"class":"Label Label--secondary v-align-middle ml-1 mb-1"})
        lang = soup.find_all("span", {"itemprop":"programmingLanguage"})


        context = {}
        for i,j,k,l in zip(range(1, len(repo)), repo, lang, mode):
            context[i] = {"repo": j.text.strip(), "lang":k.text.strip(), "link": f"{urls}/{j.text.strip()}", "mode": l.text.strip()}

    return render(request, 'index.html', {"dct":context})
