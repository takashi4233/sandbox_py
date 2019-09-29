import requests

def main():
    params = {
        'q':'python',
        }
    url = 'https://qiita.com/search/'
    r = requests.get(url,params=params)
    event_info = r.json()


    for event in event_info['events']:
        print(event['title'])
#    print (event_info)

if __name__ == '__main__':
    main()
