import csv

with open("frames.csv", "a") as file:

    unit = input("Unit: ")
    profile = input("Profile: ")
    frameset = input("Frameset: ")
    component = input("Component: ")
    label = input("Label: ")
    swage = input("Swage: ")
    service_hole = input("Service Hole: ")
    dimple = input("Dimple: ")

    writer = csv.writer(file)
    writer.writerow(["UNIT",unit])
    writer.writerow(["PROFILE",profile,"StandardProfile"])
    writer.writerow(["FRAMESET",frameset])
    writer.writerow(["COMPONENT",component,"LABEL_NRM",label,"SERVICE_HOLE",service_hole,"DIMPLE",dimple])
    writer.writerow(["COMPONENT",component,"LABEL_NRM",label,"SERVICE_HOLE",service_hole,"DIMPLE",dimple])
    writer.writerow(["COMPONENT",component,"LABEL_NRM",label,"SERVICE_HOLE",service_hole,"DIMPLE",dimple])
    writer.writerow(["COMPONENT",component,"LABEL_NRM",label,"SERVICE_HOLE",service_hole,"DIMPLE",dimple])

