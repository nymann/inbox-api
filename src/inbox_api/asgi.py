from inbox_api.api import Api
from inbox_api.core.config import Config
from inbox_api.core.service_container import ServiceContainer

config = Config()
service_container = ServiceContainer(config=config)
api = Api(config=config, service_container=service_container).api
