from django.http.response import JsonResponse, Http404, HttpResponseServerError
from django.views.decorators.http import require_GET
from django.http import HttpRequest
from search.api_request import ApiRequest
from search.google.google_request import google_api_request
from search.yandex.yandex_request import yandex_api_request
from search.base_response_formatter import BaseResponseFormatter
from search.google.google_response_formatter import GoogleResponseFormatter
from search.yandex.yandex_response_formatter import YandexResponseFormatter
from search.yandex.yandex_exceptions import YandexException
from search.google.google_exceptions import GoogleException



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

def get_formatted_api_response(query: str,
                     api_request: ApiRequest,
                     formatter: BaseResponseFormatter):
    api_response = api_request.request(query)
    formatted_response = formatter(api_response).get_formatted_response()
    return JsonResponse({"data": formatted_response})


@require_GET
def search_yandex(request):
    query = read_get_param(request, 'query')
    try:
        return get_formatted_api_response(query,
                                          yandex_api_request,
                                          YandexResponseFormatter)
    except YandexException as e:
        return HttpResponseServerError(str(e))

@require_GET
def search_google(request):
    query = read_get_param(request, 'query')
    try:
        return get_formatted_api_response(query,
                                      google_api_request,
                                      GoogleResponseFormatter)
    except GoogleException as e:
        return HttpResponseServerError(str(e))
