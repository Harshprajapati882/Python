# Interfaces in Python

# --- 1. Duck Typing (Informal Interface) ---
print("--- 1. Duck Typing (Informal Interface) ---")

# There is no formal interface class. The "contract" is simply that
# any object passed to the 'render_report' function must have a 'generate' method.

class HtmlReport:
    def generate(self):
        print("Generating an HTML report...")
        return "<html><body><h1>Report</h1></body></html>"

class CsvReport:
    def generate(self):
        print("Generating a CSV report...")
        return "id,name,value\n1,A,100\n2,B,200"

class PlainTextReport:
    # This class has a different method name
    def create(self):
        print("Creating a Plain Text report...")
        return "This is a plain text report."

def render_report(reporter):
    """
    This function relies on duck typing. It will work with any object
    that has a 'generate' method.
    """
    print("Starting report rendering...")
    try:
        report_data = reporter.generate()
        print(f"Report data: '{report_data}'")
    except AttributeError:
        print(f"Error: The object of type {type(reporter).__name__} does not have a 'generate' method.")
    print("-" * 20)

render_report(HtmlReport())
render_report(CsvReport())
render_report(PlainTextReport()) # This will fail gracefully because of our error handling.


# --- 2. Abstract Base Classes (Formal Interface) ---
print("\n--- 2. Abstract Base Classes (Formal Interface) ---")
from abc import ABC, abstractmethod

# Here we define a formal contract.
# Any class that inherits from 'ISerializable' MUST implement 'serialize'.
class ISerializable(ABC):
    @abstractmethod
    def serialize(self):
        pass

class JsonSerializable(ISerializable):
    def __init__(self, data):
        self.data = data
    
    def serialize(self):
        import json
        return json.dumps(self.data)

class XmlSerializable(ISerializable):
    def __init__(self, data):
        self.data = data

    def serialize(self):
        # A mock XML serialization
        items = "".join([f"<{k}>{v}</{k}>") for k, v in self.data.items()])
        return f"<root>{items}</root>"

# This class does NOT implement the 'serialize' method.
class BrokenSerializable(ISerializable):
    def __init__(self, data):
        self.data = data
    # Missing the serialize() method!

# Let's try to instantiate the classes.
json_obj = JsonSerializable({"name": "test", "value": 1})
xml_obj = XmlSerializable({"name": "test", "value": 1})

print(f"JSON object serializes to: {json_obj.serialize()}")
print(f"XML object serializes to: {xml_obj.serialize()}")

# This will raise a TypeError because BrokenSerializable does not
# implement the abstract method 'serialize' from the ISerializable interface.
try:
    broken_obj = BrokenSerializable({"name": "test", "value": 1})
except TypeError as e:
    print(f"\nError as expected: {e}")
