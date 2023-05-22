import sys
import getopt
import requests
import json
from rich.console import Console
from rich.table import Table
from rich import box


def main(argv):
    console = Console()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    }
    trackingnumber = ''
    postalcode = ''

    try:
        opts, args = getopt.getopt(argv, 'ht:p:', ['trackingnr=', 'postalcode='])
    except getopt.GetoptError:
        console.print('[red]Error:[/red] bpostfetcher.py -t <trackingnumber> -p <postalcode>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            console.print('bpostfetcher.py -t <trackingnumber> -p <postalcode>')
            sys.exit()
        elif opt in ('-t', '--trackingnr'):
            trackingnumber = arg
        elif opt in ('-p', '--postalcode'):
            postalcode = arg

    if not postalcode:
        console.print('[red]Error:[/red] Please enter a postal code with the -p flag')
        sys.exit(2)

    url = f'https://track.bpost.cloud/track/items?itemIdentifier={trackingnumber}&postalCode={postalcode}'
    r = requests.get(url, allow_redirects=False, headers=headers)
    data = json.loads(r.content)
    if len(data['items']) == 0:
        console.print(f'[red]Error:[/red] No data for trackingnumber {trackingnumber}')
        sys.exit(2)

    events = data['items'][0]['events']
    events = sorted(events, key=lambda x: x['date'] + x['time'], reverse=False)
    table = Table(title=f'Tracking information for {trackingnumber}', box=box.SIMPLE_HEAVY)
    table.add_column('Date', style='cyan')
    table.add_column('Time', style='magenta')
    table.add_column('Event', style='green')
    for event in events:
        table.add_row(event['date'], event['time'], event['key']['NL']['description'])
    console.print(table)

if __name__ == '__main__':
    main(sys.argv[1:])