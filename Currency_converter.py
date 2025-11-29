
from currency_converter import CurrencyConverter


def convert_currency(amount: float, from_curr: str, to_curr: str) -> float:
    """
    Convert amount from from_curr to to_curr.
    Raises ValueError if conversion fails.
    """
    c = CurrencyConverter()
    result = c.convert(amount, from_curr.upper(), to_curr.upper())
    return result

def main() -> None:
    print("Simple currency converter (powered by currencyconverter)\n")

    try:
        raw = input("Enter amount (e.g. 100.50): ").strip()
        amount = float(raw)
    except ValueError:
        print("❌ Invalid amount. Please enter a number like 100 or 99.95.")
        return

    from_cur = input("From currency (USD, EUR, GBP, ...): ").strip().upper()
    to_cur = input("To currency (INR, USD, ...): ").strip().upper()

    try:
        converted = convert_currency(amount, from_cur, to_cur)
    except Exception as e:
        # currencyconverter raises various exceptions for unsupported codes or unavailable rates
        print(f"❌ Conversion failed: {e}")
        return

    # clean, friendly output
    print()
    print(f"✅ {amount:,.2f} {from_cur}  →  {converted:,.2f} {to_cur}")
    print("Note: rates are fetched from the package's data source and may vary.")

if __name__=="__main__" :
    main()
    
