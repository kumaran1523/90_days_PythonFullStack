# Function using **kwargs to print student details.

def my_detail(**details):
    for k,v in details.items():
        print(f"{k}:{v}")
    
my_detail(name="Kumaran",maritial_Status="No",Phone_no='80565618960')