from pydantic import BaseModel

class EmployeeModel(BaseModel):
    name: str
    salary: int

# type correct
employee = EmployeeModel(
    name='Bar',
    salary=1000,
)

# type error
# employee = EmployeeModel(
#     name='Bar',
#     salary='secret',
# )
