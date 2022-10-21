import subprocess
import os


class Fan:

    preamble = '10110010110010010010'
    frequency_mhz = '304128000'
    zero_length_ns = '333'
    one_wvl_ns = '333'
    repeat = '8'
    pause_ns = '10000'
    bit_bang = '/home/lilsqueaks/Documents/rpitx/sendook'
    ceiling = {
        "light_toggle": '0100100100100101100',
        "fan_off": '0100100100101100100',
        "fan_fwd_rev_toggle": "0100100101100100100",
        "fan_hi": "1100100100100100100",
        "fan_med": "0101100100100100100",
        "fan_low": "0100101100100100100",
    }

    def __init__(self):
        self.build_command()

    def build_command(self):
        self.commands = {}
        for button, binary in self.ceiling.items():
            self.commands[button] = f'sudo {self.bit_bang} -f {self.frequency_mhz} -0 {self.zero_length_ns} -1 {self.one_wvl_ns} -r {self.repeat} -p {self.pause_ns} {self.preamble}{binary}'.split(
                ' ')
        return self.commands

    def toggle_light(self):
        cmd = self.commands['light_toggle']
        print(cmd)
        subprocess.run(cmd)
        return cmd

    def set_fan_off(self):
        cmd = self.commands['fan_off']
        print(cmd)
        subprocess.run(cmd)
        return cmd

    def set_fan_hi(self):
        cmd = self.commands['fan_hi']
        print(cmd)
        subprocess.run(cmd)
        return cmd

    def set_fan_med(self):
        cmd = self.commands['fan_med']
        print(cmd)
        subprocess.run(cmd)
        return cmd

    def set_fan_low(self):
        cmd = self.commands['fan_low']
        print(cmd)
        subprocess.run(cmd)
        return cmd

    def set_fan_fwd_rev_toggle(self):
        cmd = self.commands['fan_fwd_rev_toggle']
        print(cmd)
        subprocess.run(cmd)
        return cmd


# bedroom_fan = Fan()
# for each in bedroom_fan:
#     print(each)

# print(vars(bedroom_fan))
# bedroom_fan.toggle_light()
# bedroom_fan.toggle_light()
# bedroom_fan.set_fan_off()
# bedroom_fan.set_fan_hi()
# bedroom_fan.set_fan_med()
# bedroom_fan.set_fan_low()
# bedroom_fan.set_fan_fwd_rev_toggle()

# subprocess.run(light_on_cmd)
# if __name__ == '__main__':
#   build_command()
