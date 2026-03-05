from gsc_auth import get_gsc_service
from datetime import date, timedelta

SITE_URL = 'sc-domain:merryfair.com'

def query_gsc(service, dimensions, row_limit=10, days=28):
    end_date = date.today() - timedelta(days=3)  # GSC has ~3 day delay
    start_date = end_date - timedelta(days=days)

    response = service.searchanalytics().query(
        siteUrl=SITE_URL,
        body={
            'startDate': str(start_date),
            'endDate': str(end_date),
            'dimensions': dimensions,
            'rowLimit': row_limit,
            'orderBy': [{'fieldName': 'clicks', 'sortOrder': 'DESCENDING'}]
        }
    ).execute()
    return response.get('rows', [])

def print_table(headers, rows):
    col_widths = [max(len(str(r[i])) for r in [[*headers]] + rows) for i in range(len(headers))]
    fmt = '  '.join(f'{{:<{w}}}' for w in col_widths)
    print(fmt.format(*headers))
    print('-' * (sum(col_widths) + 2 * (len(headers) - 1)))
    for row in rows:
        print(fmt.format(*row))

if __name__ == '__main__':
    service = get_gsc_service()

    print("\n=== TOP PAGES (last 28 days) ===")
    rows = query_gsc(service, ['page'], row_limit=10)
    table = [(r['keys'][0].replace('https://www.merryfair.com',''), 
              r['clicks'], r['impressions'], f"{r['ctr']*100:.1f}%", f"{r['position']:.1f}") 
             for r in rows]
    print_table(['Page', 'Clicks', 'Impressions', 'CTR', 'Avg Position'], table)

    print("\n=== TOP KEYWORDS (last 28 days) ===")
    rows = query_gsc(service, ['query'], row_limit=10)
    table = [(r['keys'][0], r['clicks'], r['impressions'], 
              f"{r['ctr']*100:.1f}%", f"{r['position']:.1f}") 
             for r in rows]
    print_table(['Keyword', 'Clicks', 'Impressions', 'CTR', 'Avg Position'], table)

    print("\n=== COUNTRY BREAKDOWN (last 28 days) ===")
    rows = query_gsc(service, ['country'], row_limit=5)
    table = [(r['keys'][0].upper(), r['clicks'], r['impressions'],
              f"{r['ctr']*100:.1f}%", f"{r['position']:.1f}") 
             for r in rows]
    print_table(['Country', 'Clicks', 'Impressions', 'CTR', 'Avg Position'], table)
