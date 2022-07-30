import docker

client = docker.from_env()

def list_containers():
    return client.images.list()

def list_container_names():
    result = []
    for i in list_containers():
        result.append(i.attrs["RepoTags"][0])
    return result