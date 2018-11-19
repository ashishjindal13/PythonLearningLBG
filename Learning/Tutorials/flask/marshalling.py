from flask import Flask
from flask_restplus import  Api, Resource,fields

print(__name__)

app = Flask(__name__) #app is the name of the object here
api = Api(app)

appLangaugeModel = api.model('LangModel', {'language': fields.String})

lstLanguage =[]
java = {'language' : 'JAVA','id' : 1}
lstLanguage.append(java)
#
@api.route('/language')
class Language(Resource):
  @api.marshal_with(appLangaugeModel)
  def get(self):
    return lstLanguage

  @api.expect(appLangaugeModel)
  def post(self):
    new_lang = api.payload
    new_lang['id'] = len(lstLanguage)+1
    lstLanguage.append(new_lang)
    return {'result': 'Language Added'}, 201
if __name__ =="__main__":
  app.run(debug=True)