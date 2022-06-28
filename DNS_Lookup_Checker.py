import requests
import simplejson as simplejson
import json
domain_f ="https://core.securityforeveryone.com/api/solidarity/start"
domain_s ="https://core.securityforeveryone.com/api/solidarity/report"
slug_f=input("Yapmak istediginiz tarama türünü yazınız Ex:a-record-lookup.   ")
domain_a=input("Tarama yapmak istediginiz domaini giriniz Ex: securityforeveryone.com.   ")
headers = {'Content-Type': 'application/json','accept':'application/json'}
data_f = { "slug":slug_f, "asset": domain_a,'token':'IQFgQd5ohak6GcAfpqKOuq9fk5rGfhOtG2jz3jSet0tiH9zi8AdkLKvhGfNXmy5H7aczRgx4qlJEiF7K_VWtkQ'}
r = requests.post(domain_f, data=simplejson.dumps(data_f), headers=headers)
json_object = json.loads(r.text)
anl_s=json_object["value"]["analysis_slug"]
job_s=json_object["value"]["job_slugs"][0]
data_s = { "analysis_slug": anl_s, "job_slug": job_s,'token':'IQFgQd5ohak6GcAfpqKOuq9fk5rGfhOtG2jz3jSet0tiH9zi8AdkLKvhGfNXmy5H7aczRgx4qlJEiF7K_VWtkQ'}
r = requests.post(domain_s, data=json.dumps(data_s), headers=headers)
print(r.text)
