from flask import Blueprint, request, jsonify
from src.services.QaService import QaService
from src.models.qaModel import Qa

mainQa = Blueprint('Qa_blueprint', __name__)


@mainQa.route('/',methods=['GET'])

def get_qa():
    list_qa=QaService.get_qa()
    print("Consola: Preguntas obtenidas.")

    return jsonify([qa.__dict__ for qa in list_qa])
    

@mainQa.route('/post',methods=['POST'])

def post_qa():

    question = request.json ['question']
    answer= request.json ['answer']
    
    qa= Qa(0,question,answer)


    if QaService.post_qa(qa):
        print('Consola:Pregunta insertada: ', qa)
        return 'Pregunta creada.'
    
    return 'Página: Ok'

@mainQa.route('/put', methods=['PUT'])

def put_qa():
    
    id_qa = request.json['id_qa']
    question = request.json ['question']
    answer= request.json ['answer']
    
    updateqa= Qa(id_qa,question,answer)
    
    QaService.put_qa(id_qa, updateqa)
    print('Consola: Pregunta actualizada: ')
    return 'Página: Pregunta actualizada.'
   
       
@mainQa.route('/delete', methods=['DELETE'])
def delete_qa():     
    id_qa = request.json['id_qa']
    QaService.delete_qa(id_qa)
    print('Consola: Pregunta eliminada.')
    return 'Página: Pregunta eliminada.'

