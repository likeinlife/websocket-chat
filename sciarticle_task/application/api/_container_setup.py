from container import Container


def init_container() -> Container:
    container = Container()
    container.init_resources()
    container.wire(packages=["application.api"], modules=["application.api.main"])
    return container


def shutdown_container(container: Container) -> None:
    container.shutdown_resources()
