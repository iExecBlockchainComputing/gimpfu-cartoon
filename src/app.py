import os
import sys
import json
import math

input_directory = os.environ['IEXEC_IN']
output_directory = os.environ['IEXEC_OUT']

filecount = 0
for filename in os.listdir(input_directory):
    if filename.endswith((".png", ".jpg")):
        filecount += 1
        filepath = os.path.join(input_directory, filename)
        propagation_iterations = str(math.ceil(float(
            (os.path.getsize(filepath) / 1024) / 1024) + 1))  # at least 1 iteration per 1Mb
        os.system("gimp -i -b '(python-fu-cartoon RUN-NONINTERACTIVE " + propagation_iterations + "\"" +
                  filepath + "\" \"" + filename + "\" \"" + output_directory + "\" )' -b '(gimp-quit 0)'")

# Append some results in /iexec_out/
with open(output_directory + '/result.txt', 'w+') as fout:
    fout.write("Processed {} file(s)".format(filecount))

# Declare everything is computed
with open(output_directory + '/computed.json', 'w+') as f:
    json.dump({"deterministic-output-path": output_directory + '/result.txt'}, f)
