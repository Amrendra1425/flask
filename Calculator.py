from flask import Flask, request,render_template

obj=Flask(__name__)

@obj.route('/cal',methods=["GET"])
def math_operator():
    operation = request.json["operation"]
    num1=request.json["num1"]
    num2=request.json["num2"]

    if operation =="add":
        result=num1+num2
    elif operation =="subtract":
        result= num1-num2
    elif operation == "multiply":
        result=num1*num2
    else:
        result=num1/num2
    return result

if __name__=='__main__':
    obj.run(debug=True)
