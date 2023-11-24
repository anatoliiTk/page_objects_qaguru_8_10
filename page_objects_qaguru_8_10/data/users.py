import dataclasses

@dataclasses.dataclass
class User:
        first_name: str
        last_name: str
        email: str
        phone_number: str
        month: str
        year: str
        day: str
        image: str
        subject: str
        address: str
        state: str
        city: str

@dataclasses.dataclass
class User_form:
        full_name: str
        email: str
        gender: str
        phone_number: str
        date_of_birth: str
        subject: str
        hobby: str
        image: str
        address: str
        city: str