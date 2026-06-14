import os
import time
import requests

candidates = [
    os.environ.get('BACKEND_URL'),
    'http://127.0.0.1:8000',
    'http://127.0.0.1:8001',
]
url = None
for candidate in [c for c in candidates if c]:
    try:
        resp = requests.get(candidate + '/api/v1/health', timeout=2)
        if resp.status_code == 200:
            url = candidate
            print('using backend at', url)
            break
    except requests.RequestException:
        pass

if not url:
    raise SystemExit('Backend not reachable on 8000 or 8001. Set BACKEND_URL if needed.')

print('health', requests.get(url + '/api/v1/health').json())

os.makedirs('data/uploads', exist_ok=True)
with open('data/uploads/test_dummy.mp4', 'wb') as f:
    f.write(b'\x00\x00\x00\x18ftypmp42')

with open('data/uploads/test_dummy.mp4', 'rb') as video_file:
    files = {'file': ('test_dummy.mp4', video_file, 'video/mp4')}
    resp = requests.post(url + '/api/v1/videos', files=files)

print('upload', resp.status_code, resp.text)
job_id = resp.json().get('job_id')

for i in range(10):
    r = requests.get(url + f'/api/v1/jobs/{job_id}')
    print('poll', i, r.status_code, r.text)
    if r.json().get('status') == 'done':
        break
    time.sleep(1)

final_resp = requests.get(url + f'/api/v1/jobs/{job_id}/results')
print('results', final_resp.status_code, final_resp.text)
