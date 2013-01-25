from django.conf import settings
from django.shortcuts import render_to_response

import datetime
import exchange_rates

def conversion_form(request):
    c = exchange_rates.Calculator(filename=settings.EXCHANGE_RATE_SOURCE)

    context = {
        'currencies': c.get_currencies(),
    }

    date = datetime.date.today()

    if 'date' in request.GET:
        context.update({
            'from_currency': request.GET['from_currency'],
            'to_currency': request.GET['to_currency'],
            'amount': request.GET['amount'],
        })

        # do the conversion
        try:
            date = datetime.datetime.strptime(request.GET['date'],
                                          '%Y-%m-%d').date()
            rate = c.at(date, request.GET['from_currency'],
                 request.GET['to_currency'])
            amount = float(request.GET['amount'])
            context['converted_amount'] = '%f' % (amount * rate)
        except ValueError, e:
            context['error'] = e

    context['date'] = date
    return render_to_response('conversion_form.html', context)

