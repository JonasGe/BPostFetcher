import requests, json, sys, getopt


def main(argv):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    }
    trackingnumber = ''

    try:
        opts, args = getopt.getopt(argv, 'ht:', ['trackingnr='])
    except getopt.GetoptError:
        print('bpostfetcher.py -t <trackingnumber>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('bpostfetcher.py -t <trackingnumber>')
            sys.exit()
        elif opt in ('-t', '--trackingnr'):
            trackingnumber = arg

    url = 'https://track.bpost.be/btr/api/items?itemIdentifier=' + trackingnumber
    r = requests.get(url, allow_redirects=False, headers=headers)
    data = json.loads(r.content)
    if len(data['items']) == 0:
        print('No data for trackingnumber...')
        sys.exit(2)
    processsteps = data['items'][0]['processOverview']['processSteps']
    for step in processsteps:
        if step['status'] == 'active':
            print(f'Currently { step["label"]["main"] } { step["label"]["detail"] }')


if __name__ == '__main__':  # pragma: no cover
    main(sys.argv[1:])
