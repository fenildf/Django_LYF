from urllib.parse import urljoin

import requests

s = requests.Session()

base_url = 'http://127.0.0.1:8080'
question_compare_url = urljoin(base_url, '/questions/compare/?db_table=question_yingyuzhoubao_20160625&filter_method=random')
question_url = urljoin(base_url, '/questions/?db_table=question_yingyuzhoubao_20160625&filter_method=random')
question_pre_url = urljoin(base_url, '/questions/question_pre/21015122')

r = s.get(question_compare_url)
assert r.json()['meta']['status'] == 1
r = s.get(question_url)
assert r.json()['meta']['status'] == 1
r = s.get(question_pre_url)
assert r.json()['meta']['status'] == 1

login_url = urljoin(base_url, '/sessions/')
r = s.post(login_url, data={'username': 'your_name', 'password': 'your_password'})
assert r.json()['meta']['status'] == 0

r = s.get(question_compare_url)
assert r.json()['meta']['status'] == 0
r = s.get(question_url)
assert r.json()['meta']['status'] == 0
r = s.get(question_pre_url)
assert r.json()['meta']['status'] == 0


logout_url = urljoin(base_url, '/logout/')
r = s.get(logout_url)

r = s.get(question_compare_url)
assert r.json()['meta']['status'] == 1
r = s.get(question_url)
assert r.json()['meta']['status'] == 1
r = s.get(question_pre_url)
assert r.json()['meta']['status'] == 1
