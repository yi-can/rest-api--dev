from flask import Flask, request
import logging as logger


app=Flask(__name__)


@app.route("/Read",methods=["GET"])
def Read():
  sozluk={ 0: {
    "id": "3136e3cd-c90c-48bb-b9a9-60ca68382ad7",
    "title": "Say hello with python",
    "problem": "Print hello world in Python using print",
    "point": 1,
    "level": "beginner",
    "language": "python",
    "input": "",
    "expected_output": "Hello World"
  }, 1: {
    "id": "1ff26d62-e748-4907-bccf-cf2eec4ec06b",
    "title": "Arithmetic Operators - Sum",
    "problem": "Sum two numbers",
    "point": 2,
    "level": "beginner",
    "language": "python",
    "input": "5,6",
    "expected_output": "11"
  }, 2:   {
    "id": "d07cb6ee-af91-4d0f-abd7-efe1693a8d3f",
    "title": "Loops",
    "problem": "Print the square of each number in the loop step",
    "point": 2,
    "level": "beginner",
    "language": "python",
    "input": "4",
    "expected_output": "0,1,4,9"
  }
  }
  logger.debug("Inisde the get method of Task") 
  return sozluk

@app.route("/Add",methods=["GET","POST"])
def Add():
  sozluk={ 0: {
    "id": "3136e3cd-c90c-48bb-b9a9-60ca68382ad7",
    "title": "Say hello with python",
    "problem": "Print hello world in Python using print",
    "point": 1,
    "level": "beginner",
    "language": "python",
    "input": "",
    "expected_output": "Hello World"
  }, 1: {
    "id": "1ff26d62-e748-4907-bccf-cf2eec4ec06b",
    "title": "Arithmetic Operators - Sum",
    "problem": "Sum two numbers",
    "point": 2,
    "level": "beginner",
    "language": "python",
    "input": "5,6",
    "expected_output": "11"
  }, 2:   {
    "id": "d07cb6ee-af91-4d0f-abd7-efe1693a8d3f",
    "title": "Loops",
    "problem": "Print the square of each number in the loop step",
    "point": 2,
    "level": "beginner",
    "language": "python",
    "input": "4",
    "expected_output": "0,1,4,9"
  }
  }
  if request.method=="GET":
    logger.debug("Inisde the get method of Task")
    return sozluk
  else:
    for i in range(3):
        sozluk[i]["-----------------------------------------------------------------------------------"]=True
    return sozluk


@app.route("/Update",methods=["GET","PUT"])
def Update():
  sozluk={ 0: {
    "id": "3136e3cd-c90c-48bb-b9a9-60ca68382ad7",
    "title": "Say hello with python",
    "problem": "Print hello world in Python using print",
    "point": 1,
    "level": "beginner",
    "language": "python",
    "input": "",
    "expected_output": "Hello World"
  }, 1: {
    "id": "1ff26d62-e748-4907-bccf-cf2eec4ec06b",
    "title": "Arithmetic Operators - Sum",
    "problem": "Sum two numbers",
    "point": 2,
    "level": "beginner",
    "language": "python",
    "input": "5,6",
    "expected_output": "11"
  }, 2:   {
    "id": "d07cb6ee-af91-4d0f-abd7-efe1693a8d3f",
    "title": "Loops",
    "problem": "Print the square of each number in the loop step",
    "point": 2,
    "level": "beginner",
    "language": "python",
    "input": "4",
    "expected_output": "0,1,4,9"
  }
  }
  if request.method=="GET":
    logger.debug("Inisde the get method of Task")
    return sozluk
  else:
    return {"message" : "Ne yapacağımı bilemedim"}

@app.route("/Delete",methods=["GET","DELETE"])
def Delete():
  sozluk={ 0: {
    "id": "3136e3cd-c90c-48bb-b9a9-60ca68382ad7",
    "title": "Say hello with python",
    "problem": "Print hello world in Python using print",
    "point": 1,
    "level": "beginner",
    "language": "python",
    "input": "",
    "expected_output": "Hello World"
  }, 1: {
    "id": "1ff26d62-e748-4907-bccf-cf2eec4ec06b",
    "title": "Arithmetic Operators - Sum",
    "problem": "Sum two numbers",
    "point": 2,
    "level": "beginner",
    "language": "python",
    "input": "5,6",
    "expected_output": "11"
  }, 2:   {
    "id": "d07cb6ee-af91-4d0f-abd7-efe1693a8d3f",
    "title": "Loops",
    "problem": "Print the square of each number in the loop step",
    "point": 2,
    "level": "beginner",
    "language": "python",
    "input": "4",
    "expected_output": "0,1,4,9"
  }
  }
  if request.method=="GET":
    logger.debug("Inisde the get method of Task")
    return sozluk
  else:
    del sozluk[2]
    return sozluk

if __name__=="__main__":

    app.run(host="0.0.0.0",port=5000,debug=True,use_reloader=True)


