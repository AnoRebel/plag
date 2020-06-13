from flask import render_template, make_response, request, jsonify
from flask import current_app as app
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def url():
	url = request.form.get('url')
	links = {}
	images = {}
	metas = {}
	response = requests.get(url)
	if response.status_code == 200:
		soup = BeautifulSoup(response.content, 'html5lib')
		title = soup.title.text
		for meta in soup.find_all('meta'):
			metas[meta.get('name')] = meta.get('description')
			metas[meta.get('name')] = meta.get('content')
			metas[meta.get('property')] = meta.get('content')

		for image in soup.find_all('img'):
			images[image.get('alt')] = urljoin(url, image.get('src'))

		vid_temps = [urljoin(url, video.get('src')) for video in soup.find_all('video')]
		sources = [urljoin(url, source.get('src')) for source in soup.find_all('source')]
		videos = [*vid_temps, *sources]

		for link in soup.find_all('a'):
			if 'http' in link:
				links[link.get('href')] = link.get_text()
			else:
				if link.get('href') == None:
					pass
				else:
					if link.get('href').endswith('/'):
						links[urljoin(url, link.get('href'))] = link.get_text()
					else:
						links[urljoin(url + '/', link.get('href'))] = link.get_text()

		output = {
			'message': 'Success',
			'data': {
				'title': title,
				'metas': metas,
				'images': images,
				'videos': videos,
				'links': links,
				'code': response.status_code
			}
		}
	else:
		output = {
			'message': 'Failed.',
			'data': {
				'code' : response.status_code
			}
		}

	import json
	val = json.dumps(output)
	data = json.loads(val)
	return render_template("link.html", data=output)
	# return render_template("link.html", json=json, data=json.dumps(output))
	# return json.dumps(output)
	# return render_template("link.html", data=jsonify(output))


@app.errorhandler(400)
def bad_request():
    """Bad request."""
    return make_response(render_template("400.html"), 400)


@app.errorhandler(404)
def not_found():
    """Page not found."""
    return make_response(render_template("404.html"), 404)


@app.errorhandler(500)
def server_error():
    """Internal server error."""
    return make_response(render_template("500.html"), 500)
