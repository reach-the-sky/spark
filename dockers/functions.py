import docker

client = docker.from_env()

def run(name):
    client.containers.run(name,detach=True)

def list_images():
    return client.images.list()

def list_containers():
    return client.containers.list()

def list_images_names():
    result = []
    for i in list_images():
        result.append(i.attrs["RepoTags"][0])
    return result

def list_containers_names():
    result = []
    for i in list_containers():
        result.append(i)
    return result

def stop_all_containers():
    for i in list_containers():
        i.stop()