from repositories.Presentation import PresentationRepository
from service.Presentation import PresentationService
from repositories.User import UserRepository
from service.User import UserService

presentation_repository = PresentationRepository()

presentation_service = PresentationService(presentation_repository)


async def get_presentation_service():
    return presentation_service


user_repository = UserRepository()

user_service = UserService(user_repository)

async def get_user_service():
    return user_service