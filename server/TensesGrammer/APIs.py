from QuestionMaking.QuestionGenerate import *

print(QuestionGenerater('I am a doctor.'))

# app = Flask(__name__)
# tense_parser = TenseParser()
#
# @app.route('/',methods=['GET','POST'])
# def cameraapi():
#     solution={}
#     if request.method=='POST':
#         image_data = request.json['image']
#         grammar = request.json["grammar"]
#         im = Image.open(BytesIO(base64.b64decode(image_data.split(',')[1])))
#         im.save("image.png")
#         text=image_to_text("image.png")
#         if (grammar == "Finder"):
#             solution['result'] = tense_parser.find_tense_simple_form_str(text)
#         elif (grammar == "Conjunction"):
#             text, explain = GrammerSolver(text)
#             solution['result'] = text
#             solution['result way'] = explain
#         else:
#             explain = QuestionGenerater(text)
#             solution['result way'] = explain
#         return solution
#     elif request.method=='GET':
#         print(request.json)
#         return 'GET'
#
# @app.route('/text',methods=['GET','POST'])
# def textapi():
#     solution={}
#     if request.method=='POST':
#         text=request.json["text"]
#         grammar=request.json["grammar"]
#         print(text,grammar)
#         if (grammar=="Finder"):
#             solution['result']=tense_parser.find_tense_simple_form_str(text)
#             print(solution['result'])
#         elif(grammar=="Conjunction"):
#             text,explain=GrammerSolver(text)
#             solution['result']=text
#             solution['result way']=explain
#         else:
#             print(QuestionGenerater(f'''{text}.'''))
#             solution['question']  = QuestionGenerater(f'''{text}.''')
#
#         return solution
#
#     elif request.method=='GET':
#         return 'Hello'
#
# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=3000)
