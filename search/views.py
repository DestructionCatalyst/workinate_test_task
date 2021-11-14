from django.http.response import JsonResponse, Http404
from django.views.decorators.http import require_GET
from search.google.google_request import google_search_api_request
from search.google.google_response_formatter import GoogleResponseFormatter
from django.http import HttpRequest


def read_get_param(request: HttpRequest, param: str):
    """
    Reads a parameter value from GET request body.
    If there is no parameter with the specified name, returns 404 error.
    :param request: request to read parameter value from
    :param param: name of the parameter
    :return: value of the specified parameter
    :raise django.http.Http404: if a request does not contain a parameter
    with the specified name
    """
    query = request.GET.get(param)
    if query is None:
        raise Http404

    return query

@require_GET
def search_yandex(request):
    query = read_get_param(request, 'query')
    return JsonResponse({"data": [query]})

@require_GET
def search_google(request):
    query = read_get_param(request, 'query')
    google_response = google_search_api_request(query)
    formatted_response = \
        GoogleResponseFormatter(google_response).get_formatted_response()
    return JsonResponse({"data": formatted_response})