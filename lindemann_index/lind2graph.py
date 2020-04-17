
import re
from matplotlib import pyplot as plt
from matplotlib.ticker import FormatStrFormatter

def read_text(file):
    content = []
    with open(file, "r") as f:
        for line in f:
            if not line.startswith("Lindemann"):
                content.append(line.strip())
    return content


def main():
    file = 'lindemann.txt'
    lindemann = []
    temperature = []
    content = read_text(file)
    for line in content:
        file_name = line.split(":")[0]
        lindemann.append(float(line.split(":")[1]))
        temperature.append(float(re.findall(r'\d+', file_name)[0]))

    print(lindemann)
    print(temperature)
    fig, axs = plt.subplots()
    # axs.yaxis.set_major_formatter(FormatStrFormatter('%2d'))
    # axs.ylim([0.1,0.4])
    axs.plot(temperature, lindemann)
    plt.show()


if __name__ =='__main__':
    main()
