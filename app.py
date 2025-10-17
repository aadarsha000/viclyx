from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

# Optional: serve any file by its path
@app.route('/<path:path>')
def serve_static_file(path):
    return send_from_directory('.', path)


@app.route('/blog')
def serve_blog():
    return send_from_directory('.', 'blog.html')


@app.route('/contact')
def serve_contact():
    return send_from_directory('.', 'contact-us.html')


if __name__ == '__main__':
    app.run(debug=True)
