from infra.database.repository import UserRepository
from infra.database.entities.user import UserAuth




a = UserAuth(email="simeone@gmail.com",code=UserAuth.generate_code())

UserRepository().create_one(UserAuth.json())

