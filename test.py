import dockers

if __name__ == "__main__":
    dockers.run("ubuntu")
    print("list image images names: ", dockers.list_images_names())
    print("list image container names: ", dockers.list_containers_names())
    dockers.stop_all_containers()