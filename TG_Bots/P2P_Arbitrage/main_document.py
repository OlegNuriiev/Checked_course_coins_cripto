import ccxt

def get_prices(pair):
    binance = ccxt.binance()
    bybit = ccxt.bybit()

    try:
        # Получаем цену на Binance
        binance_ticker = binance.fetch_ticker(pair)
        binance_price = binance_ticker['ask'] if binance_ticker else None

        # Получаем цену на Bybit
        bybit_ticker = bybit.fetch_ticker(pair)
        bybit_price = bybit_ticker['ask'] if bybit_ticker else None

        return binance_price, bybit_price
    except Exception as e:
        print(f"Ошибка при получении цен: {e}")
        return None, None

def calculate_spread(binance_price, bybit_price):
    if binance_price and bybit_price:
        # Рассчитываем спред в процентах
        spread_percent = ((bybit_price - binance_price) / binance_price) * 100
        return spread_percent
    return None

def fetch_all_pairs():
    binance = ccxt.binance()
    try:
        # Получаем список торговых пар на Binance
        markets = binance.load_markets()
        # Фильтруем только те, которые связаны с USDT
        usdt_pairs = [pair for pair in markets.keys() if 'USDT' in pair]
        return usdt_pairs
    except Exception as e:
        print(f"Ошибка при загрузке рынков Binance: {e}")
        return []

def main():
    pairs = fetch_all_pairs()
    if not pairs:
        print("Не удалось загрузить криптовалютные пары.")
        return

    for pair in pairs:
        # Получаем цены на Binance и Bybit
        binance_price, bybit_price = get_prices(pair)

        if binance_price is None or bybit_price is None:
            # Если цены не получены, пропускаем пару
            continue

        # Рассчитываем спред
        spread = calculate_spread(binance_price, bybit_price)

        # Если спред больше 2%, выводим информацию
        if spread is not None and abs(spread) > 2:
            # Извлекаем название криптовалюты без "USDT"
            crypto_name = pair.replace('USDT', '')

            print(f"Криптовалюта: {crypto_name}")
            print(f"Цена на Binance: {binance_price:.2f} USDT")
            print(f"Цена на Bybit: {bybit_price:.2f} USDT")
            print(f"Спред: {spread:.2f}%")

            if binance_price < bybit_price:
                print(f"Рекомендация: покупайте {crypto_name} на Binance.")
            else:
                print(f"Рекомендация: покупайте {crypto_name} на Bybit.")
            print()

if __name__ == "__main__":
    main()
