from flask import Flask, request, render_template
from flask.views import View


class ApiTestView(View):

    def dispatch_request(self, *args, **kw):
        method = request.method
        url = request.url
        headers = request.headers
        cookies = request.cookies
        remote_addr = request.remote_addr

        return render_template(
            'msg.html',
            method=method, url=url, remote_addr=remote_addr,
            cookies=cookies, headers=headers
        )


app = Flask(__name__)
app.add_url_rule(r'/test/', view_func=ApiTestView.as_view('test_handler'))
