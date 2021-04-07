# import requests

# url = "https://www.fast2sms.com/dev/bulkV2"

# querystring = {"authorization":"Tf0l5vJFUNs3EqRDwmVpjkIHLbYXSBtxGicuhyPQdW9nr2e178brnxh0MUt2DmlTGoPKJLEvaAYN9SW6","sender_id":"TXTIND","message":"Hello This is bunkORNER","variables_values":"12345|asdaswdx","route":"p","numbers":"7405334113"}

# headers = {
#     'cache-control': "no-cache"
# }

# response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)
# import requests

# url = "https://www.fast2sms.com/dev/bulkV2"

# payload = "message=Welcome%20to%20bunkKORNER&language=english&route=q&numbers=7383796964"
# headers = {
#     'authorization': "Tf0l5vJFUNs3EqRDwmVpjkIHLbYXSBtxGicuhyPQdW9nr2e178brnxh0MUt2DmlTGoPKJLEvaAYN9SW6",
#     'Content-Type': "application/x-www-form-urlencoded",
#     'Cache-Control': "no-cache",
#     }

# response = requests.request("POST", url, data=payload, headers=headers)

# print(response.text)
import requests

url = "https://www.fast2sms.com/dev/bulkV2"

querystring = {"authorization":"Tf0l5vJFUNs3EqRDwmVpjkIHLbYXSBtxGicuhyPQdW9nr2e178brnxh0MUt2DmlTGoPKJLEvaAYN9SW6","sender_id":"TXTIND","message":"yO BEECH","variables_values":"12345|asdaswdx","route":"dlt","numbers":"7383796964"}

headers = {
    'cache-control': "no-cache"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)