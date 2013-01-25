import datetime
from xml.etree import ElementTree as ET

class Calculator:

    def __init__(self, filename='eurofxref-hist-90d.xml', base_currency='EUR'):
        self.filename = filename
        self.base_currency = base_currency
        self.currencies = set()
        
    def get_currencies(self):
        """Return list of strings representing currencies available."""

        if self.currencies:
            return self.currencies
        tree = ET.parse(self.filename)
        self.currencies = {e.attrib['currency'] for e in tree.findall('*/*/*')}
        self.currencies.add(self.base_currency)
        return self.currencies

    def at(self, date=datetime.date.today(), base_currency='EUR',
           counter_currency='GBP'):
        """Return number of counter_currency per base_currency."""

        tree = ET.parse(self.filename)
        date_string = date.strftime('%Y-%m-%d')

        if base_currency == self.base_currency:
            base_rate = 1.0
        else:
            try:
                base_rate = float(
                    tree.find('*/*[@time=\'%s\']/*[@currency=\'%s\']' %
                             (date_string, base_currency)).attrib['rate'])
            except:
                raise ValueError('No data for %s on %s' % (base_currency, date))

        if counter_currency == self.base_currency:
            counter_rate = 1.0
        else:
            try:
                counter_rate = float(
                    tree.find('*/*[@time=\'%s\']/*[@currency=\'%s\']' %
                             (date_string, counter_currency)).attrib['rate'])
            except:
                raise ValueError('No data for %s on %s' % (counter_rate, date))

        return counter_rate / base_rate

