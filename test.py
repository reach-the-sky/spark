import dockers

if __name__ == "__main__":
    dockers.run("docker/getting-started")
    print("list images names: ", dockers.list_images_names())
    print("list container names: ", dockers.list_containers_names())
    print("list container data: ", dockers.list_containers_data())
    dockers.stop_all_containers()
    # dockers.stop_container(input())