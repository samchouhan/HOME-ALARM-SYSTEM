from plyer import notification
from datetime import datetime

class AlarmSystem:
    def __init__(self):
        self.armed = False
        self.logs = []

    def log_event(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] {message}"
        self.logs.append(entry)

    def arm_system(self):
        if self.armed:
            print("System is already armed.")
        else:
            self.armed = True
            print("System armed.")
            self.log_event("Alarm armed")

    def disarm_system(self):
        if not self.armed:
            print("System is already disarmed.")
        else:
            self.armed = False
            print("System disarmed.")
            self.log_event("Alarm disarmed")

    def detect_motion(self):
        if not self.armed:
            print("Motion detected, but system is disarmed.")
            self.log_event("Motion detected while disarmed")
            return

        print("\n!!! MOTION DETECTED !!!")
        self.log_event("Motion detected")

        notification.notify(
            title="Home Security Alert",
            message="Motion detected! Possible intrusion.",
            timeout=5
        )

        response = input(
            "\nFalse alarm? Enter password to disarm (1234): "
        )

        if response == "1234":
            self.disarm_system()
            self.log_event("False alarm confirmed")
            print("False alarm cleared.")
        else:
            print("\nALARM ACTIVATED!")
            self.log_event("Intrusion alarm triggered")

        def show_logs(self):
        print("\n===== EVENT LOGS =====")

        if not self.logs:
            print("No logs available.")
            return

        for log in self.logs:
            print(log)

    def main():
    alarm = AlarmSystem()

    while True:
        print("\n===== HOME ALARM SYSTEM =====")
        print("1. Arm System")

   
