Coding test to make a library for exchange rate calculations along with a web interface.

Not happy with this at all. It was supposed to be a Ruby test but they let me do it in
Python. It just seems so awkward. The library was supposed to be accessed by eg.
ExchangeRate.at(date, 'USD', 'GBP') which just seems weird to me.

The library is `lib/exchange_rates.py`.

The django app is based on djappengine: <https://github.com/potatolondon/djappengine>.

This code is deployed at <https://fxulike.appspot.com>.
