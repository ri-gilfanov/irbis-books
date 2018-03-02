from django.shortcuts import render
import json
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from django.http import HttpResponse
from base64 import b64decode


def book_search(request):
    context = {}

    if request.GET:
        irbis_api_url = 'http://172.16.129.131:15880/irbisapi/search'
        search_params = urlencode(request.GET)

        irbis_api_response = urlopen('%s?%s' % (irbis_api_url, search_params))
        book_list = json.loads(irbis_api_response)['Books']
        for book in book_list:
            book['url_params'] = urlencode({
                'book_db': book['db'],
                'book_id': book['pk'],
                'book_mfn': book['mfn'],
            })

        context['irbis_api_response'] = irbis_api_response
        context['book_list'] = book_list

    return render(request, 'core/base.html', context)


def book_download(request):
    irbis_pdf_url = 'http://172.16.129.33:8080/irbispdf/pdf'
    download_params = urlencode(request.GET)

    irbis_pdf_response = urlopen('%s?%s' % (irbis_pdf_url, download_params))

    file_name = b64decode(irbis_pdf_response.headers['Description'])
    file_data = irbis_pdf_response.read()

    response = HttpResponse(file_data, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="%s.pdf"' % file_name

    return response
