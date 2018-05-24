from flask import *
import pandas as pd
app = Flask(__name__)

@app.route("/tables")
def show_tables():
    data = pd.read_csv('file.csv')
    data.set_index(['chk'], inplace=True)
    data.index.name=None
    return render_template('view.html', tables = [data.to_html()], titles = ['na'])

if __name__ == "__main__":
    app.run(debug=True)