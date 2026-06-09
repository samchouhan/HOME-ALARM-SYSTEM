#Software system design code for the Home Alarm System (H_A_S)


if motion_detected and alarm_armed:
    print("INTRUDER DETECTED!")

class HomeAlarmSystem:

    def __init__(self):
        self.armed = False

    def arm(self):
        self.armed = True

    def disarm(self):
        self.armed = False

    def detect_motion(self):
        if self.armed:
            print("ALARM ACTIVATED!")


#Add desktop notification system

    
