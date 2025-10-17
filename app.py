from flask import Flask, send_from_directory, render_template_string

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

@app.route('/blog/how-ai-tools-are-reshaping-business-strategies')
def serve_blog_b1():
    return send_from_directory('.', 'b1.html')

@app.route('/blog/exploring-the-future-of-automation-and-intelligence')
def serve_blog_b2():
    return send_from_directory('.', 'b2.html')

@app.route('/blog/a-comprehensive-guide-for-beginners-in-intelligence')
def serve_blog_b3():
    return send_from_directory('.', 'b3.html')

@app.route('/blog/cybersecurity-and-quantum-computing')
def serve_blog_b4():
    return send_from_directory('.', 'b4.html')

@app.route('/blog/empowering-global-defense-with-ai')
def serve_blog_b5():
    return send_from_directory('.', 'b5.html')

@app.route('/blog/the-rise-of-augmented-intelligence-human-machine-collaboration')
def serve_blog_b6():
    return send_from_directory('.', 'b6.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
