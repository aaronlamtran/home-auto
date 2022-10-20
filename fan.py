import subprocess
import os

ceiling = {
    "light_toggle": '0100100100100101100',
    "fan_off": '0100100100101100100',
    "fan_fwd_rev_toggle": "0100100101100100100",
    "fan_hi": "1100100100100100100",
    "fan_med": "0101100100100100100",
    "fan_low": "0100101100100100100",
}

preamble = '10110010110010010010'
frequency_mhz = '304128000'
zero_length_ns = '333'
one_wvl_ns = '333'
repeat = '8'
pause_ns = '10000'
bit_bang = '/home/lilsqueaks/Documents/rpitx/sendook'

commands = {}

def build_command():
  for button, binary in ceiling.items():
    commands[button] = f'sudo {bit_bang} -f {frequency_mhz} -0 {zero_length_ns} -1 {one_wvl_ns} -r {repeat} -p {pause_ns} {preamble}{binary}'.split(' ')
  for command in commands.items():
    print(command)
    # pass

# subprocess.run(light_on_cmd)
if __name__ == '__main__':
  build_command()
