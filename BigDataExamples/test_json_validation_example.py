import pytest
import json
from jsonschema import validate
from jsonschemaexample import validate_json
from jsonschemaexample import validate_json_schema
from jsonschemaexample import transaction_schema

#Example for pytest

class Test_JsonValidation:

    def test_validate_json_Should_return_True_when_valid_json_string(self):
        json_string = '{"a":"b","c":123}'
        result = validate_json(json_data=json_string)
        assert result

    def test_validate_json_Should_return_False_when_invalid_json_string(self):
        json_string = '{"a":"b","c"=123}'
        result = validate_json(json_data=json_string)
        assert (not result)
    def test_validate_json_Should_return_False_when_valid_json_schema(self):
        json_sample = """
                           {
            "InvoiceNo":"ABC863563",
            "StockCode":"18768767",
            "Quantity":"40",
            "CustomerID":"1002",
            "InvoiceDate":"04-04-2023",
            "UnitPrice":"233.5"
        }"""
        result = validate_json_schema(json_data=json.loads(json_sample),schema=transaction_schema)
        assert (not result[0])

    def test_validate_json_Should_return_True_when_valid_json_Schema(self):
        json_sample = """
                           {
                       "InvoiceNo":8001,
                       "StockCode":456,
                       "Quantity":40,
                       "CustomerID":1001,
                       "InvoiceDate":"04-04-2023",
                       "UnitPrice":233.5
                   }"""
        result = validate_json_schema(json_data=json.loads(json_sample), schema=transaction_schema)
        assert result[0]

    def run_validate_json_Should_return_True_when_valid_json_Schema(self):
        json_sample = """
                           {
                       "InvoiceNo":8001,
                       "StockCode":456,
                       "Quantity":40,
                       "CustomerID":1001,
                       "InvoiceDate":"04-04-2023",
                       "UnitPrice":233.5
                   }"""
        result = validate_json_schema(json_data=json.loads(json_sample), schema=transaction_schema)
        assert result[0]