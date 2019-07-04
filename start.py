import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import jsonify
from flask import json
from flask import Flask

cred = credentials.Certificate("./table-booking-3ab22-firebase-adminsdk-4kww0-d5eac90487.json")
firebase_admin.initialize_app(cred)
db_con = firestore.client()
app = Flask(__name__)


@app.route("/")
def getTableList():
    try:
        doc_ref = db_con.collection('tableName').stream()
        docsDict = {}
        for doc in doc_ref:
            docsDict[doc.id] = doc.to_dict()
        response = app.response_class(
            response=json.dumps(docsDict),
            status=200,
            mimetype='application/json'
        )
        return response
    except:
        print("Fillee Error")
        return "1123"


if __name__ == "__main__":
    app.run(debug=True)
