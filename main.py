
import requests
import json



# set the auth and url options

hed = {
    'x-api-key': '',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}
url = 'https://adminapi.encv-test.org/api/batch-issue'




data = json.dumps({
    "codes": [
        {
            "symptomDate": "2021-07-12",
            "testDate": "2021-07-12",
            "testType": "confirmed",
            "tzOffset": 0,
            "phone": "+12066126577",
            "smsTemplateLabel": "Default SMS template",
            "externalIssuerID": "dlorigan-dev"
        },
        {
            "symptomDate": "2021-07-13",
            "testDate": "2021-07-13",
            "testType": "confirmed",
            "tzOffset": 0,
            "phone": "+1206612",
            "smsTemplateLabel": "Default SMS template",
            "externalIssuerID": "dlorigan-dev"
        }
    ],
    "padding": "2"
})

response = requests.post(url, data=data, headers=hed)



print(response.request.headers)
print(response.request.body)
print(response.request.url)

# This returns some crazy html
print(response.text)

