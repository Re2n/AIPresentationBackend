from repositories.Presentation import PresentationRepository
from service.Presentation import PresentationService

presentation_repository = PresentationRepository()

presentation_service = PresentationService(presentation_repository)


async def get_presentation_service():
    return presentation_service
