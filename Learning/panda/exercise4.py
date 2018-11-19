import pandas as pd
import json
from flask import Flask,request
from flask_restplus import  Api, Resource,fields
from functools import wraps


def get_airline_data():
    airlines = pd.read_csv('../data/airlines.csv')
    return airlines

def get_flight_data():
    flights = pd.read_csv('../data/flights.csv')
    return flights

app=Flask(__name__)
auth={
    'apikey':{
        'type':'apiKey',
        'in':'header',
        'name': 'authTokenCheck'
    }
}
api=Api(app,authorizations=auth)

def token_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token=None
        if 'authTokenCheck' in request.headers:
            token=request.headers['authTokenCheck']
        if not token:
            return {'message':'no token given'},401
        print(token,'token')

        if token !='ashish':
            return {'message':'your token is wrong '},401

        return f(*args,**kwargs)
    return decorated

AirlineDataModel = api.model('AirlineModel', {'TAIL_NUMBER': fields.String,
                                              'ORIGIN_AIRPORT': fields.String,
                                              'DESTINATION_AIRPORT': fields.String,
                                              'AIRLINE': fields.String})

@api.route('/AirlineByName/<string:airline_name>')
class AirlineData(Resource):
    @api.marshal_with(AirlineDataModel)
    @api.doc(security='apikey')
    @token_required
    def get(self, airline_name=None):
        ds= get_flight_data()
        filteredData=ds[ds['AIRLINE']==airline_name]
        return json.loads(filteredData.head().to_json())


@api.route('/UpdateAirlineCode/<string:airline_code_old>,<string:airline_code_new>')
class UpdateAirlineCode(Resource):
    def put(self, airline_code_old=None,airline_code_new=None):
        ds = get_flight_data()
        if len(airline_code_new) == 2:
            filteredData=ds.replace(airline_code_old,airline_code_new)
            return json.loads(filteredData.head().to_json())
        else:
            return json.loads(ds.head().to_json())

#third Pending


@api.route('/getTwentyRowsbyColName/<string:colName>')
class getTwentyRowsbyColName(Resource):
    def get(self, colName=None):
        ds= get_flight_data()
        filteredData=ds[colName]
        return json.loads(filteredData.head(20).to_json())


if __name__ == "__main__":
    app.run(debug=True)

