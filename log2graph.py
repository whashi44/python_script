# import matplotlib.pyplot as plt
from bokeh.plotting import figure, output_file, show, save
from bokeh.io import export_png
import numpy as np


def main():
    file_name = "log.lammps"
    step = []
    temperature = []
    volume = []
    press = []
    totEng = []
    potEng = []
    kinEng = []
    E_pair = []
    E_bond = []
    enthalpy = []
    parameters = [step, temperature, volume, press, totEng, potEng, kinEng, E_pair, E_bond, enthalpy]
    counter = 0
    with open(file_name, 'r') as read_file:
        for line in read_file:
            if line.startswith("Step") and (line.endswith("Enthalpy\n") or line.endswith("Enthalpy \n")):
                counter += 1
                if counter >= 2:
                    current = next(read_file)
                    while not current.startswith("Loop"):
                        current = current.strip().split()
                        # Step Temp Volume Press TotEng PotEng KinEng E_pair E_bond Enthalpy
                        for index, item in enumerate(parameters):
                            item.append(float(current[index]))
                        # step.append(float(current[0]))
                        # temperature.append(float(current[1]))
                        # volume.append(float(current[2]))
                        # press.append(float(current[3]))
                        # totEng.append(float(current[4]))
                        # potEng.append(float(current[5]))
                        # enthalpy.append(float(current[9]))
                        current = next(read_file)

    for item in parameters:
        item = np.array(item)
    # step = np.array(step)
    # temperature = np.array(temperature)
    # volume = np.array(volume)
    # press = np.array(press)
    # totEng = np.array(totEng)
    # potEng = np.array(potEng)
    # enthalpy = np.array(enthalpy)
    # data = np.vstack((step, temperature))
    # data = np.transpose(data)
    # breakpoint()
    # left = np.amax(step)
    # right = max(step)
    target = press
    # bottom = min(target)
    # top = max(target)
    #
    # print(left, right, bottom, top)

    # with open('temp.txt','a') as write_file: #append file with bytes mode
    #     np.savetxt(write_file,data, fmt="%s")
    parameter_names = ['ste','temperature', 'volume', 'press', 'totEng', 'potEng', 'kinEng', 'E_pair', 'E_bond', 'enthalpy']
    for item, name in zip(parameters[1:], parameter_names[1:]):
        output_file(f"{name}.html")
        p = figure(title=f'step vs {name}', x_axis_label='step', y_axis_label=name)
        p.line(step, item, line_width=1)
        save(p)
    # p = figure(title='time vs temperature', x_axis_label = 'x', y_axis_label='y', x_range=(0,160000000), y_range=(600,1200))
    # p = figure(title='time vs temperature', x_axis_label = 'x', y_axis_label='y', x_range=(left,right), y_range=(bottom,top))
    # p = figure(title='time vs temperature', x_axis_label='x', y_axis_label='y')
    # p.line(step, target, line_width=1)
    # show(p)
    # fix, axs = plt.subplots()
    # axs.plot(step,temperature)
    # plt.show()


if __name__ == '__main__':
    main()
