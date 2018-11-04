from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
import json
import csv
from fuzzywuzzy import process
from Levenshtein import distance
from app.world_list import world

class SuggestionView(APIView):
	def get(self, request):
		query = request.GET.get('name', None)
		res = []
		if query:
			with open('app/word_search.tsv') as tsvfile:

			  reader = csv.reader(tsvfile, delimiter='\t')
			  list_of_words = [row[0] for row in reader]
			  result = process.extract(query, list_of_words, limit=25)
			  res = [{"value":word, "match":match} for word, match in result]

		return JsonResponse(res, safe=False)


class SearchView(APIView):
	def get(self, request):
		query = request.GET.get('name', None)
		res = []
		if query:
		  result = process.extract(query, world, limit=25)
		  res = [{"value":word, "match":match} for word, match in result]
		return JsonResponse(res, safe=False)