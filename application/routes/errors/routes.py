from flask import current_app as app
from flask.templating import render_template
from application.Utils import Map, create_blueprint

error_bp = create_blueprint('error_bp', __name__)

@app.errorhandler(404)
@app.errorhandler(405)
@app.errorhandler(500)
def pageNotFound(error):
    map = Map()
    print("routed as should")
    map.put("error", error)
    return render_template('error.html', map=map)