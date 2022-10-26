from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['SECRET_KEY]= 'your_secret_key'
books_ = [
    {
  'id': 1,
  'nm':'DO MIL AO MILHAO',
  'valor':'19,35',
  'autor':'THIAGO NIGRO'
  },
  {
  'id': 2,
  'nm':'O PODER DO HABITO',
  'valor':'49,90',
  'autor':'CHARLES DUHHIG'
  },
    {
  'id': 3,
  'nm':'A ARTE DA GUERRA',
  'valor':'17,89',
  'autor':'SUN TZU'
  },
  {
  'id': 4,
  'nm': 'ALAN TURING'
  'valor' : '
  }
]

@app.route("/books_", methods=['GET'])
def books():
  return jsonify(books_)
 
 @app.route("/books_/<int:id>)
 def filter_by_id(id):
  for livro in books_:
    if livro.get('id)==id:
      return jsonify(livro)
      
@app.route("/books_", methods=['POST'])
def criar_livro():
  new_book = request.get_json()
  books_.append(new_book)
  
  return jsonify(books_)
  
  
app.run(host='localhost', port=5000, debug=True)
  
