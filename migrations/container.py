from dependency_injector import containers, providers
from app.data.repository.user_profile_repository import UserRepository
from app.services.user_service import UserService


class Container(containers.DeclarativeContainer):
    user_repository = providers.Singleton(UserRepository)
    user_service = providers.Factory(UserService, user_repository = user_repository)





container = Container()
container.wire(modules=[__name__])