from flask import Flask , request , jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restplus import Api , fields, Resource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['SECRET_KEY']='password'
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api()
api.init_app(app)

# Database Model
class Hero(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    fname = db.Column(db.String)
    lname = db.Column(db.String)
    password = db.Column(db.String)

# Schema of database
class HeroSchema(ma.Schema):
    class Meta:
        fields = ('id','fname','lname','password')


model = api.model("User management Web API ",{
    'fname': fields.String('Enter Hero First Name'),
    'lname': fields.String('Enter Hero Last Name'),
    'password': fields.String('Enter password')
})

heros_schema = HeroSchema(many=True)


@api.route('/get')
class getdata(Resource):
    def get(self):
        data = Hero.query.all()
        if data is None:
            return {'message': 'No records found in the database'}
        data_json = heros_schema.dump(data)
        return jsonify(data_json)

@api.route('/post')
class postdata(Resource):
    @api.expect(model)
    def post(self):
        data = Hero(fname=request.json['fname'],lname=request.json['lname'],password=request.json['password'])
        db.session.add(data)
        db.session.commit()
        return {'message': 'Data added to database'}

@api.route('/put/<int:id>')
class putdata(Resource):
    @api.expect(model)
    def put(self, id):
        data = Hero.query.get(id)
        if data is None:
            return {'message': 'No such record is present in the database'}
        data.fname = request.json['fname']
        data.lname = request.json['lname']
        data.password = request.json['password']
        db.session.commit()
        return {'message': 'Data is updated to database'}

@api.route('/delete/<int:id>')
class deletedata(Resource):    
    def delete(self, id):
        data = Hero.query.get(id)
        if data is None:
            return {'message': 'No such record is present in the database'}
        db.session.delete(data)
        db.session.commit()
        return {'message': 'Data is deleted from database'}


