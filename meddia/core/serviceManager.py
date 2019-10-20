import meddia.api

SERVICES_STARTING_TIMEOUT=60
class ServiceManager:
    services = {}

    def __init__(self):
        pass

    """
    Registers and starts the service to allow the core and other plugins to use them.
    """
    def register_service(service: Service):
        service.start();
        start_time = time.monotonic();
        while(!service.is_started()):
            if((time.monotonic()-start_time) > SERVICES_STARTING_TIMEOUT):
                raise ServiceStartingTimeout
            pass
        pass

    """
    Stops and unregisters the service
    """
    def unregister_service():
        pass

