from robot_control_class import RobotControl 
robotcontrol = RobotControl() 

list_laser = robotcontrol.get_laser_full()

dictionary_laser = {}

for key, objet in enumerate(list_laser):
    dictionary_laser[key] = objet

for i in dicionario_laser:
    print ('Position', i, dictionary_laser[i])
