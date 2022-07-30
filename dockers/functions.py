import docker

client = docker.from_env()

def run(name,ports=None,custom_name=None):
    client.containers.run(name,detach=True,ports=ports,name=custom_name)
    
def start_container(id):
    container = client.containers.get(id)
    if container:
        container.start()
        return True
    return False

def list_images():
    return client.images.list()

def list_containers():
    return client.containers.list(all=True)

def list_containers_data():
    result = []
    for i in list_containers():
        result.append({
            "Id": i.attrs["Id"],
            "Running": i.attrs["State"]["Running"], 
            "Pid": i.attrs["State"]["Pid"], 
            "Name": i.attrs["Name"], 
            "Image": i.attrs["Config"]["Image"]
        })
    return result

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

def container_logs(id) -> str:
    container = client.containers.get(id)
    if container:
        return container.logs()
    return "None"

def stop_container(id):
    container = client.containers.get(id)
    if container:
        container.stop()

def stop_all_containers():
    for i in list_containers():
        i.stop()
        
def kill_container(id):
    container = client.containers.get(id)
    if container:
        try:
            container.kill()
        except:
            pass
        # container.prune()
        return "Success"
    return "None"

def remove_container(id):
    container = client.containers.get(id)
    if container:
        try:
            container.remove()
        except:
            pass
        # container.prune()
        return "Success"
    return "None"