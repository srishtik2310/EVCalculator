from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import math

GRAVITY = 9.81
continuous_motor_rating = 0

# <---------------Motor Rating calculation-------------->
def motor_rating(output):
    global weight, wheel_diameter, max_speed, gradient, gear_ratio, max_acceleration, drag_coefficient, frontal_area, \
        resistance_coefficient, efficiency_gearbox, WHEEL_RPM,LINEAR_ACC_FORCE, ROLLING_RESISTANCE_FORCE, GRADIENT_FORCE, \
        AERODYNAMIC_FORCE, TOTAL_FORCE_MAX, TOTAL_TORQUE_MAX, TOTAL_TORQUE_MIN, MOTOR_TORQUE_MAX, MOTOR_TORQUE_MIN,\
        MOTOR_POWER_MAX, MOTOR_POWER_MIN, WEIGHT, RADIUS, ANGULAR_VELOCITY, MOTOR_RPM, MAX_SPEED, TOTAL_FORCE_MIN, radius

    try:
        weight = float(weight_entry.get())
        wheel_diameter = float(wheel_diameter_entry.get())
        max_speed = float(max_speed_entry.get())
        max_acceleration = float(max_acceleration_entry.get())
        resistance_coefficient = float(resistance_coefficient_entry.get())
        gradient = float(gradient_entry.get())
        gear_ratio = float(gear_ratio_entry.get())
        drag_coefficient = float(drag_coefficient_entry.get())
        frontal_area = float(frontal_area_entry.get())
        efficiency_gearbox = float(efficiency_gearbox_entry.get())

        if clicked_weight.get() == units_weight[0]:
            pass
        elif clicked_weight.get() == units_weight[1]:
            weight = weight * 1000
        elif clicked_weight.get() == units_weight[2]:
            weight = weight * 0.453592

        if clicked_diameter.get() == units_diameter[0]:
            pass
        elif clicked_diameter.get() == units_diameter[1]:
            wheel_diameter = wheel_diameter / 100
        elif clicked_diameter.get() == units_diameter[2]:
            wheel_diameter = wheel_diameter * 0.0254

        if clicked_speed.get() == units_speed[0]:
            max_speed = max_speed * (5 / 18)
        elif clicked_speed.get() == units_speed[1]:
            pass
        elif clicked_speed.get() == units_speed[2]:
            max_speed = max_speed * 0.44704

        if clicked_gradient.get() == units_gradient[0]:
            gradient = gradient * (math.pi / 180)
        elif clicked_gradient.get() == units_gradient[1]:
            gradient = gradient / 100
            gradient = math.atan(gradient)

        radius = wheel_diameter / 2

        angular_velocity = max_speed / radius
        motor_rpm = ((angular_velocity * gear_ratio) * 60) / (2 * math.pi)
        wheel_rpm = motor_rpm/gear_ratio

        linear_acc_force = weight * max_acceleration
        rolling_resistance_force = weight * 9.81 * resistance_coefficient
        gradient_force = weight * GRAVITY * (math.sin(gradient))
        drag_force = 0.5 * 1.225 * (max_speed ** 2) * drag_coefficient * frontal_area

        total_force_max = linear_acc_force + rolling_resistance_force + gradient_force + drag_force
        total_force_min = linear_acc_force + rolling_resistance_force + drag_force
        total_torque_max = total_force_max * radius
        total_torque_min = total_force_min * radius
        motor_torque_max = (total_torque_max / gear_ratio)/(efficiency_gearbox/100)
        motor_torque_min = (total_torque_min / gear_ratio)/(efficiency_gearbox/100)

        angular_speed_motor = (motor_rpm * 2 * math.pi) / 60
        motor_power_max = motor_torque_max * angular_speed_motor
        motor_power_min = motor_torque_min * angular_speed_motor

    except:
        if len(weight_entry.get()) == 0:
            messagebox.showwarning(message="Please enter the weight of the vehicle")
            weight_entry.focus()
        elif len(wheel_diameter_entry.get()) == 0:
            messagebox.showwarning(message="Please enter the wheel diameter of the vehicle")
            wheel_diameter_entry.focus()
        elif len(max_speed_entry.get()) == 0:
            messagebox.showwarning(message="Please enter the Maximum speed of the vehicle")
            max_speed_entry.focus()
        elif len(max_acceleration_entry.get()) == 0:
            messagebox.showwarning(message="Please enter the Maximum acceleration of the vehicle")
            max_acceleration_entry.focus()
        elif len(resistance_coefficient_entry.get()) == 0:
            messagebox.showwarning(message="Please enter the rolling resistance coefficient")
            resistance_coefficient_entry.focus()
        elif len(gradient_entry.get()) == 0:
            messagebox.showwarning(message="Please enter the maximum gradient that vehicle has to go through")
            gradient_entry.focus()
        elif len(gear_ratio_entry.get()) == 0:
            messagebox.showwarning(message="Please enter the gear ratio of the gear box")
            gear_ratio_entry.focus()
        elif len(efficiency_gearbox_entry.get()) == 0:
            messagebox.showwarning(message="Please enter the efficiency of gearbox")
            efficiency_gearbox_entry.focus()
        elif len(drag_coefficient_entry.get()) == 0:
            messagebox.showwarning(message="Please enter the drag coefficient of the vehicle")
            drag_coefficient_entry.focus()
        elif len(frontal_area_entry.get()) == 0:
            messagebox.showwarning(message="Please enter the frontal area of the vehicle")
            frontal_area_entry.focus()
        elif radius == 0 or gear_ratio == 0:
            messagebox.showwarning(message="Radius or gear ratio cannot be 0")
        else:
            messagebox.showwarning(message="Please enter correct values. Note that all values must be float. "
                                        "Avoid entering commas instead of dot for the float values and also dont enter "
                                        "characters instead of float")

    else:

        WEIGHT = round(weight, 2)
        RADIUS = round(radius, 4)
        ANGULAR_VELOCITY = round(angular_velocity, 2)
        MOTOR_RPM = round(motor_rpm, 2)
        WHEEL_RPM = round(wheel_rpm, 2)
        LINEAR_ACC_FORCE = round(linear_acc_force, 2)
        ROLLING_RESISTANCE_FORCE = round(rolling_resistance_force, 2)
        GRADIENT_FORCE = round(gradient_force, 2)
        AERODYNAMIC_FORCE = round(drag_force, 2)
        TOTAL_FORCE_MAX = round(total_force_max, 2)
        TOTAL_TORQUE_MAX = round(total_torque_max, 2)
        TOTAL_TORQUE_MIN = round(total_torque_min, 2)
        MOTOR_TORQUE_MAX = round((motor_torque_max)*(efficiency_gearbox/100), 2)
        MOTOR_TORQUE_MIN = round((motor_torque_min)*(efficiency_gearbox/100), 2)
        MOTOR_POWER_MAX = round_power(motor_power_max)
        MOTOR_POWER_MIN = round_power(motor_power_min)
        MAX_SPEED = round(max_speed, 2)
        TOTAL_FORCE_MIN = round(total_force_min, 2)


        if output == True:
            messagebox.showinfo(message=f"Motor Rating of the EV \n\n"
                                        f"Power Rating:\n"
                                        f"Pmax = {round_power(motor_power_max)} W\n"
                                        f"Pmin = {round_power(motor_power_min)} W\n\n"
                                        f"Torque Rating:\n"
                                        f"Tmax = {round(motor_torque_max, 2)} Nm\n"
                                        f"Tmin = {round(motor_torque_min, 2)} Nm\n")

        else:
            pass


def round_power(num):
    mul = (num//10)+1
    return (mul*10)

def battery_calculator():
    global battery_image, continuous_motor_rating_entry, clicked_rating, clicked_speed_avg, average_speed_entry, \
        battery_voltage_entry, units_motor_rating, units_average_speed, expected_range_entry, time, current, \
        battery_capacity_ah, battery_capacity_kwh, continuous_motor_rating, average_speed, battery_voltage, \
        expected_range

    continuous_motor_rating = float(continuous_motor_rating_entry.get())
    average_speed = float(average_speed_entry.get())
    battery_voltage = float(battery_voltage_entry.get())
    expected_range = float(expected_range_entry.get())

    if clicked_rating.get() == units_motor_rating[0]:
        pass
    elif clicked_rating.get() == units_motor_rating[1]:
        continuous_motor_rating = continuous_motor_rating * 1000
    elif clicked_rating.get() == units_motor_rating[2]:
        continuous_motor_rating = continuous_motor_rating * 746

    if clicked_speed_avg.get() == units_average_speed[0]:
        pass
    elif clicked_speed_avg.get() == units_average_speed[1]:
        average_speed = (average_speed)*(18/5)


    time = expected_range/average_speed
    current = continuous_motor_rating/battery_voltage

    battery_capacity_ah = current*time
    battery_capacity_kwh = (continuous_motor_rating*time)/1000

    messagebox.showinfo(message=f"Battery capacity = {round(battery_capacity_ah, 1)} Ah \n"
                                f"Battery capacity = {round(battery_capacity_kwh, 1)} kWh")

def calculate_battery():
    global battery_image, continuous_motor_rating_entry, clicked_rating, clicked_speed_avg, average_speed_entry, \
        battery_voltage_entry, units_motor_rating, units_average_speed, expected_range_entry
    new_window = Toplevel(window)
    new_window.config(bg="white", padx=30)
    new_window.geometry("600x630+420+250")
    new_window.title("Battery size calculator")
    new_window.resizable(False, False)
    battery_canvas = Canvas(new_window, width= 350, height=250, highlightthickness=0)
    battery_image = PhotoImage(file="battery.png")
    battery_canvas.create_image(175, 125, image=battery_image)
    battery_canvas.grid(row=0, column=0, columnspan=2)


    battery_info_label = Label(new_window, text="Enter the Battery calculations parameters", fg="#6AC8FE",
                                   font=("Courier", 18, "bold"), pady=10, padx=10)
    battery_info_label.grid(row=1, column=0, sticky="W", columnspan=2)

    continuous_motor_rating_label = Label(new_window, text="1) Continouos rating of the motor:")
    continuous_motor_rating_label.grid(row=3, column=0, sticky="W")

    units_motor_rating = ["W", "kW", "HP"]

    clicked_rating = StringVar()
    clicked_rating.set(units_motor_rating[0])
    drop_rating = OptionMenu(new_window, clicked_rating, *units_motor_rating)
    drop_rating.grid(row=3, column=0, sticky="E")

    continuous_motor_rating_entry = Entry(new_window, width=5)
    continuous_motor_rating_entry.grid(row=3, column=1, sticky="E")
    continuous_motor_rating_entry.focus()

    average_speed_label = Label(new_window, text="2) Average speed of the vehicle:")
    average_speed_label.grid(row=4, column=0, sticky="W")

    units_average_speed = ["km/h", "m/s"]

    clicked_speed_avg = StringVar()
    clicked_speed_avg.set(units_average_speed[0])
    drop_avg_speed = OptionMenu(new_window, clicked_speed_avg, *units_average_speed)
    drop_avg_speed.grid(row=4, column=0, sticky="E")

    average_speed_entry = Entry(new_window, width=5)
    average_speed_entry.grid(row=4, column=1, sticky="E")

    battery_voltage_label = Label(new_window, text="3) Enter the nominal voltage of the battery Voltage:")
    battery_voltage_label.grid(row=5, column=0, sticky="W")

    battery_voltage_entry = Entry(new_window, width=5)
    battery_voltage_entry.grid(row=5, column=1, sticky="E")

    expected_range_label = Label(new_window, text="4) Expected Range (in km):")
    expected_range_label.grid(row=6, column=0, sticky="W")

    expected_range_entry = Entry(new_window, width=5)
    expected_range_entry.grid(row=6, column=1, sticky="E")

    battery_calculate_button = Button(new_window, text="Calculate battery capacity", font=("Courier", 18, "bold"),
                                        command=battery_calculator,
                                        highlightbackground='#A5A5A5', fg="black")
    battery_calculate_button.grid(row=7, column=0, columnspan=2, pady=20)

def generate_report():
    try:
        motor_rating(False)
        replace_dict = {"Max_speed": str(MAX_SPEED), "Radius": str(RADIUS),
                        "Angular_velocity": str(ANGULAR_VELOCITY), "Wheel_rpm": str(WHEEL_RPM),
                        "Motor_rpm": str(MOTOR_RPM),
                        "Linear_acc_force": str(LINEAR_ACC_FORCE),
                        "Rolling_resistance_force": str(ROLLING_RESISTANCE_FORCE),
                        "Gradient_force": str(GRADIENT_FORCE), "Aerodynamic_force": str(AERODYNAMIC_FORCE),
                        "Total_force_max": str(TOTAL_FORCE_MAX), "Total_torque_max": str(TOTAL_TORQUE_MAX),
                        "Motor_torque_max": str(MOTOR_TORQUE_MAX), "Total_force_min": str(TOTAL_FORCE_MIN),
                        "Total_torque_min": str(TOTAL_TORQUE_MIN), "Motor_torque_min": str(MOTOR_TORQUE_MIN),
                        "Motor_power_max": str(MOTOR_POWER_MAX), "Motor_power_min": str(MOTOR_POWER_MIN)}

    except NameError:
        pass

    else:
        path = filedialog.asksaveasfilename()
        with open(path, mode = "w") as l:
            s = open("report_template.txt")
            w = s.read()
            l1 = w.replace("Weight", str(WEIGHT))
            for key, value in replace_dict.items():
                l1 = l1.replace(key, value)

            l.write(l1)
            s.close()
        messagebox.showinfo(message = f"Your Report is saved at\n {path}")

def generate_report_battery():
    if continuous_motor_rating == 0:
        messagebox.showwarning(message="Please calculate motor and battery ratings first using "
                                       " 'Calculate Motor Rating' and 'Calculate battery capacity' button first")
    else:
        replace_dict = {"Max_speed": str(MAX_SPEED), "Radius": str(RADIUS),
                        "Angular_velocity": str(ANGULAR_VELOCITY), "Wheel_rpm": str(WHEEL_RPM),
                        "Motor_rpm": str(MOTOR_RPM),
                        "Linear_acc_force": str(LINEAR_ACC_FORCE),
                        "Rolling_resistance_force": str(ROLLING_RESISTANCE_FORCE),
                        "Gradient_force": str(GRADIENT_FORCE), "Aerodynamic_force": str(AERODYNAMIC_FORCE),
                        "Total_force_max": str(TOTAL_FORCE_MAX), "Total_torque_max": str(TOTAL_TORQUE_MAX),
                        "Motor_torque_max": str(MOTOR_TORQUE_MAX), "Total_force_min": str(TOTAL_FORCE_MIN),
                        "Total_torque_min": str(TOTAL_TORQUE_MIN), "Motor_torque_min": str(MOTOR_TORQUE_MIN),
                        "Motor_power_max": str(MOTOR_POWER_MAX), "Motor_power_min": str(MOTOR_POWER_MIN),
                        "Continuous_motor_rating":str(round((continuous_motor_rating/1000), 2)),
                        "Average_speed":str(round(average_speed, 2)),
                        "Nominal_voltage":str(round(battery_voltage, 2)), "Expected_range":str(round(expected_range, 2)),
                        "Time_running":str(round(time, 2)), "Current":str(round(current, 2)),
                        "Battery_capacity_Ah":str(round(battery_capacity_ah, 2)),
                        "Battery_capacity_kWh":str(round(battery_capacity_kwh, 2))
                        }

        path = filedialog.asksaveasfilename()
        with open(path, mode="w") as l:
            s = open("report_with_battery.txt")
            w = s.read()
            l1 = w.replace("Weight", str(WEIGHT))
            for key, value in replace_dict.items():
                l1 = l1.replace(key, value)

            l.write(l1)
            s.close()
        messagebox.showinfo(message=f"Your Report is saved at\n {path}")



# <------------------ UI configuration ----------------------->
window = Tk()
window.geometry("600x1000+420+0")
window.config(bg="white", padx=30)
window.title("EV calculator")
window.minsize(400, 400)
canvas = Canvas(width=500, height=210, highlightthickness=0)
ev_image = PhotoImage(file="ev.png")
canvas.create_image(200, 100, image=ev_image)
canvas.grid(row=0, column=0, columnspan=2)

parameters_label = Label(text="Mention the parameters of the EV", fg="#0000ff", font=("Courier", 22, "bold"))
parameters_label.grid(row=1, column=0, columnspan=2)

linear_acc_force_label = Label(text="Force required for linear acceleration", fg="#6AC8FE",
                               font=("Courier", 18, "bold"), pady=10, padx=10)
linear_acc_force_label.grid(row=2, column=0, sticky="W")

weight_Label = Label(text="1) Dead Weight of Vehicle:")
weight_Label.grid(row=3, column=0, sticky="W")

units_weight = ["kg", "tons", "pounds"]

clicked_weight = StringVar()
clicked_weight.set(units_weight[0])
drop_weight = OptionMenu(window, clicked_weight, *units_weight)
drop_weight.grid(row=3, column=0)

weight_entry = Entry(width=5)
weight_entry.focus()
weight_entry.grid(row=3, column=1, sticky="W")

wheel_diameter_label = Label(text="2) Wheel diameter:")
wheel_diameter_label.grid(row=4, column=0, sticky="W")

units_diameter = ["m", "cm", "inches"]

clicked_diameter = StringVar()
clicked_diameter.set("m")
drop_diameter = OptionMenu(window, clicked_diameter, *units_diameter)
drop_diameter.grid(row=4, column=0)

wheel_diameter_entry = Entry(width=5)
wheel_diameter_entry.grid(row=4, column=1, sticky="W")

max_speed_label = Label(text="3) Max speed:")
max_speed_label.grid(row=5, column=0, sticky="W")

units_speed = ["km/h", "m/s", "miles/h"]

clicked_speed = StringVar()
clicked_speed.set("km/h")
drop_speed = OptionMenu(window, clicked_speed, *units_speed)
drop_speed.grid(row=5, column=0)

max_speed_entry = Entry(width=5)
max_speed_entry.grid(row=5, column=1, sticky="W")

max_acceleration_label = Label(text="4) Max acceleration:")
max_acceleration_label.grid(row=6, column=0, sticky="W")

units_acc = ["m/s2"]
clicked_acc = StringVar()
clicked_acc.set("m/s2")
drop_speed = OptionMenu(window, clicked_acc, *units_acc)
drop_speed.grid(row=6, column=0)

max_acceleration_entry = Entry(width=5)
max_acceleration_entry.grid(row=6, column=1, sticky="W")

rolling_force_label = Label(text="Force to Overcome rolling resistance", fg="#6AC8FE",
                            font=("Courier", 18, "bold"), pady=10, padx=10)
rolling_force_label.grid(row=7, column=0, sticky="W")

rolling_resitance_label = Label(text="5) Co-efficient of rolling resistance:")
rolling_resitance_label.grid(row=8, column=0, sticky="W")

resistance_coefficient_entry = Entry(width=5)
resistance_coefficient_entry.grid(row=8, column=1, sticky="W")

gradient_force_label = Label(text="Force to Overcome Gradient", fg="#6AC8FE",
                             font=("Courier", 18, "bold"), pady=10, padx=10)
gradient_force_label.grid(row=9, column=0, sticky="W")

gradient_label = Label(text="6) Maximum gradient:")
gradient_label.grid(row=10, column=0, sticky="W")

units_gradient = ["Degree", "percentage"]

clicked_gradient = StringVar()
clicked_gradient.set("Degree")
drop_gradient = OptionMenu(window, clicked_gradient, *units_gradient)
drop_gradient.grid(row=10, column=0)

gradient_entry = Entry(width=5)
gradient_entry.grid(row=10, column=1, sticky="W")

gear_ratio_label = Label(text="7) Gear ratio of gear box:")
gear_ratio_label.grid(row=11, column=0, sticky="W")

gear_ratio_entry = Entry(width=5)
gear_ratio_entry.grid(row=11, column=1, sticky="W")

efficiency_gearbox_label = Label(text="8) Efficiency of the gearbox (in percentage):")
efficiency_gearbox_label.grid(row=12, column=0, sticky="W")

efficiency_gearbox_entry = Entry(width=5)
efficiency_gearbox_entry.grid(row=12, column=1, sticky="W")

aerodynamic_force_label = Label(text="Force to Overcome Aerodynamic drag", fg="#6AC8FE",
                                font=("Courier", 18, "bold"), pady=10, padx=10)
aerodynamic_force_label.grid(row=13, column=0, sticky="W")

drag_coefficient_label = Label(text="8) Drag co-efficient of vehicle:")
drag_coefficient_label.grid(row=14, column=0, sticky="W")

drag_coefficient_entry = Entry(width=5)
drag_coefficient_entry.grid(row=14, column=1, sticky="W")

frontal_area_label = Label(text="9) frontal area of the vehicle:")
frontal_area_label.grid(row=15, column=0, sticky="W")

frontal_area_entry = Entry(width=5)
frontal_area_entry.grid(row=15, column=1, sticky="W")

l = Label(text=" ")
l.grid(row=16, column=0)

calculate_button = Button(window, text="Calculte Motor Rating", font=("Courier", 18, "bold"),
                          command=lambda: motor_rating(True),
                          highlightbackground='#A5A5A5', fg="black")
calculate_button.grid(row=17, column=0, padx=10, columnspan=2, pady=2.5)

calculate_battery_button = Button(window, text="Calculate battery rating", font=("Courier", 18, "bold"),
                                command= calculate_battery,
                                highlightbackground='#A5A5A5', fg="black")
calculate_battery_button.grid(row=18, column=0, columnspan=2, pady=2.5)

generate_report_button = Button(window, text="Generate Report", font=("Courier", 18, "bold"),
                                command= generate_report,
                                highlightbackground='#A5A5A5', fg="black")
generate_report_button.grid(row=19, column=0, columnspan=2, pady=2.5)

generate_report_battery_button = Button(window, text="Generate Report with battery", font=("Courier", 18, "bold"),
                                command= generate_report_battery,
                                highlightbackground='#A5A5A5', fg="black")

generate_report_battery_button.grid(row=20, column=0, columnspan=2, pady=2.5)

window.mainloop()
