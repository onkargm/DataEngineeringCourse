import json
import jsonschema.exceptions
from jsonschema import validate
from pprint import pprint

transaction_schema = {
"$schema":"http://json-schema.org/draft-04/schema#",
    "type":"object",
    "properties":{
        "InvoiceNo":{
            "type":"integer"
        },
"StockCode":{
            "type":"integer"
        },
"Description":{
            "type":"string"
        },
"Quantity":{
            "type":"integer"
        },
"InvoiceDate":{
            "type":"string"
        },
"UnitPrice":{
            "type":"number"
        },
"CustomerID":{
            "type":"integer"
        },
"Country":{
            "type":"string"
        }
    },
    "required":[
        "InvoiceNo",
        "StockCode",
        "Quantity",
        "CustomerID",
        "InvoiceDate",
        "UnitPrice"
    ]
}

#validate function

def validate_json(json_data):
    try:
        json.loads(json_data)
    except ValueError as err:
        return False
    return True

def validate_json_schema(json_data,schema):
    """REF: https://json-schema.org/"""
    schema = transaction_schema
    try:
        validate(instance=json_data,schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        print(err)
        err = "Given Json data is not valid"
        return False,err
    error_message = "Given JSON is valid"
    return True,error_message

if __name__ =='__main__':
    with open("sample_json_data") as json_file:
        data= json.load(json_file)


    #checking if the json is valid
    print(validate_json(json.dumps(data)))
    #checking if the dictionaries within json are valid
    for item in data["transaction_data"]:
        print(validate_json_schema(json_data=item,schema=transaction_schema))

