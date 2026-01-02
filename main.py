from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon
from pybricks.robotics import DriveBase
from pybricks.tools import wait, Matrix, StopWatch


# Robot configuration
hub = PrimeHub()


left_motor = Motor(Port.F, positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E)
gripper_motor = Motor(Port.D, gears=[20, 28])
back_gripper_motor = Motor(Port.B)


hub.system.set_stop_button(Button.BLUETOOTH)
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=54, axle_track=95)


# Wait for IMU to calibrate
hub.light.on(Color.RED)
drive_base.use_gyro(True)


# hub.imu.reset_heading(0)
hub.imu.reset_heading(0)
hub.light.on(Color.MAGENTA)


# ================================ Run 1 code for Prem =======================
def run1():
    global runindex
    drive_base.stop()
    drive_base.use_gyro(True)
    drive_base.settings(900, 1000)


    drive_base.straight(640)
    drive_base.straight(-160)
    drive_base.turn(17)
    drive_base.straight(106.2)
    drive_base.straight(-26.2)
    drive_base.turn(-15)
    drive_base.straight(-8)
    wait(500)
    back_gripper_motor.run_angle(200, 100)
    back_gripper_motor.run_angle(300, -20)


    drive_base.turn(-2)
    drive_base.straight(190)
    drive_base.turn(-45)
    drive_base.straight(62)


    drive_base.use_gyro(False)
    gripper_motor.run_angle(100, 80)
    drive_base.use_gyro(True)


    drive_base.straight(-80)
    drive_base.turn(-34)
    drive_base.straight(220)
    drive_base.straight(-60)
    drive_base.turn(18)
    drive_base.straight(80)
    drive_base.straight(-15)
    drive_base.turn(-10)
    drive_base.straight(40)
    drive_base.straight(-250)
    drive_base.turn(-95)
    drive_base.straight(700)


    drive_base.stop()
    runindex += 1




# ================================ Run 2 code for Manasvi =======================
def run2():
    global runindex
    drive_base.stop()
    drive_base.use_gyro(True)
    drive_base.settings(800, 800)


    wait(500)


    drive_base.straight(537)
    drive_base.turn(23)
    drive_base.straight(-70)
    drive_base.turn(-102)
    drive_base.straight(40)
    drive_base.turn(70)
    drive_base.straight(150)
    drive_base.straight(-30)
    drive_base.turn(-25)
    drive_base.straight(390)
    drive_base.turn(115)
    drive_base.straight(280)


    drive_base.use_gyro(False)
    drive_base.turn(-45)
    drive_base.straight(10)
    drive_base.turn(-30)
    drive_base.turn(30)
    drive_base.turn(-30)


    gripper_motor.run_angle(speed=1000, rotation_angle=-1500)


    drive_base.turn(19)
    drive_base.straight(-140)
    drive_base.turn(83)
    drive_base.straight(900)


    drive_base.stop()
    runindex += 1




# ================================ Run 3 code for Sukti =======================
def run3():
    global runindex
    drive_base.stop()
    drive_base.use_gyro(True)
    drive_base.settings(900, 900)


    drive_base.straight(700)
    drive_base.turn(64)
    back_gripper_motor.run_angle(500, -200)
    drive_base.straight(110)
    back_gripper_motor.run_angle(500, 200)
    wait(1000)


    drive_base.straight(20)
    drive_base.straight(-20)
    drive_base.turn(25)
    drive_base.straight(750)
    drive_base.turn(32)
    drive_base.settings(250)
    drive_base.use_gyro(False)
    drive_base.straight(350)
    drive_base.straight(-200)
    drive_base.turn(5)
    drive_base.straight(-70)


    back_gripper_motor.run_angle(300, -180)
    back_gripper_motor.run_angle(300, 290)


    drive_base.settings(900)
    drive_base.straight(100)
    drive_base.turn(-55)
    drive_base.straight(300)
    drive_base.turn(67)
    drive_base.straight(830)


    drive_base.stop()
    runindex += 1




# ================================ Run 4 code for Stuti_1 =======================
def run4():
    global runindex
    drive_base.stop()
    drive_base.use_gyro(False)
    drive_base.settings(600, 600)


    drive_base.straight(100)
    drive_base.turn(-20)
    drive_base.straight(500)
    drive_base.turn(65)
    drive_base.straight(160)


    back_gripper_motor.run_angle(speed=500, rotation_angle=-120)
    drive_base.turn(20)
    drive_base.turn(-70)
    back_gripper_motor.run_angle(speed=500, rotation_angle=120)


    drive_base.straight(-20)
    drive_base.turn(40)
    drive_base.straight(-180)
    drive_base.turn(-38)
    drive_base.straight(217)


    drive_base.settings(straight_speed=600, straight_acceleration=600, turn_rate=1000)
    drive_base.turn(-550)
    drive_base.straight(-700)


    drive_base.stop()
    runindex += 1




# ================================ Run 5 code for Stuti_2 =======================
def run5():
    global runindex
    drive_base.stop()
    drive_base.settings(300, 300)


    drive_base.straight(250)
    wait(10)


    for _ in range(2):
        gripper_motor.run_angle(speed=1000, rotation_angle=300)
        gripper_motor.run_angle(speed=1000, rotation_angle=-200)


    gripper_motor.run_angle(speed=1000, rotation_angle=400)
    gripper_motor.run_angle(speed=1000, rotation_angle=-200)


    drive_base.straight(-400)
    drive_base.stop()
    runindex += 1




# ================================ Run 6 code for Justin =======================
def run6():
    global runindex
    drive_base.stop()
    drive_base.use_gyro(True)
    drive_base.settings(900, 900)


    drive_base.straight(200)
    drive_base.turn(-47)
    drive_base.straight(240)
    drive_base.turn(-33)
    drive_base.straight(-49)
    drive_base.turn(-35)
    drive_base.straight(315)
    drive_base.turn(90)
    drive_base.straight(60)


    back_gripper_motor.run_angle(40, -20)
    drive_base.straight(-200)
    drive_base.straight(130)
    drive_base.turn(-33)


    drive_base.straight(440)
    back_gripper_motor.run_angle(350, 230)
    drive_base.straight(-130)
    drive_base.turn(59)
    drive_base.straight(390)
    drive_base.turn(-108)


    drive_base.use_gyro(False)
    drive_base.straight(100)
    gripper_motor.run_angle(400, 220)
    drive_base.turn(-38)
    drive_base.straight(-150)
    drive_base.straight(90)
    drive_base.turn(45)
    gripper_motor.run_angle(speed=200, rotation_angle=-100)


    drive_base.stop()
    runindex += 1




# ================================ Image bitmaps ================================
digits = [
    Matrix([
        [0,1,1,1,0],
        [0,1,0,1,0],
        [0,1,0,1,0],
        [0,1,0,1,0],
        [0,1,1,1,0]
    ]) * 100,


    Matrix([
        [0,0,1,0,0],
        [0,1,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,1,1,1,0]
    ]) * 100,


    Matrix([
        [0,1,1,1,0],
        [0,0,0,1,0],
        [0,1,1,1,0],
        [0,1,0,0,0],
        [0,1,1,1,0]
    ]) * 100,


    Matrix([
        [0,1,1,1,0],
        [0,0,0,1,0],
        [0,1,1,1,0],
        [0,0,0,1,0],
        [0,1,1,1,0]
    ]) * 100,


    Matrix([
        [0,1,0,1,0],
        [0,1,0,1,0],
        [0,1,1,1,0],
        [0,0,0,1,0],
        [0,0,0,1,0]
    ]) * 100,


    Matrix([
        [0,1,1,1,0],
        [0,1,0,0,0],
        [0,1,1,1,0],
        [0,0,0,1,0],
        [0,1,1,1,0]
    ]) * 100,


    Matrix([
        [0,1,1,1,0],
        [0,1,0,0,0],
        [0,1,1,1,0],
        [0,1,0,1,0],
        [0,1,1,1,0]
    ]) * 100
]




# ================================ Master program ================================
runindex: int = 0


runs = [
    [digits[1], run1],
    [digits[2], run2],
    [digits[3], run3],
    [digits[4], run4],
    [digits[5], run5],
    [digits[6], run6],
]


numruns: int = len(runs)


hub.speaker.beep(900, 100)




def debounce_button_press():
    """Wait for button release to prevent multiple presses."""
    wait(200)
    while any(hub.buttons.pressed()):
        pass




while True:
    hub.light.on(Color.GREEN)
    hub.display.icon(runs[runindex][0])


    buttons = []
    while not any(buttons):
        buttons = hub.buttons.pressed()


    if Button.CENTER in buttons:
        hub.speaker.beep(1100, 50)
        debounce_button_press()
        hub.light.on(Color.WHITE)
        hub.display.off()
        try:
            runs[runindex][1]()
            hub.speaker.beep(800, 50)
        except Exception as e:
            print("Error:", e)


        debounce_button_press()
        wait(500)


    elif Button.RIGHT in buttons:
        runindex = (runindex + 1) % numruns
        hub.speaker.beep(600, 50)
        wait(500)


    elif Button.LEFT in buttons:
        runindex = (runindex + numruns - 1) % numruns
        hub.speaker.beep(550, 50)
        wait(500)



