from pydub import AudioSegment
import os
import sys

# Take a folder as input and return a single audio file that's all of the files in folder
# Glue(input folder, output file name, [output filetype])
def Glue(folder, output, outtype):
    spacer = AudioSegment.silent()
    sounds = []

    for root, dirs, files in os.walk(folder, topdown=False):
        for name in files:
            print(os.path.join(root, name))
            sounds.append(os.path.join(root, name))

    combined = AudioSegment.empty()
    for sound in sounds:
        try:
            intype = sound.split('.')
            if(outtype == "none"):
                outtype = intype[1]

            s = AudioSegment.from_file(sound, intype[1])
            combined = combined + s
        except:
            print(sound + " is not an audio file.")

    combined.export(folder + "\\" + output + "." + outtype, format=outtype)
    print(folder + "\\" + output + "." + outtype)


if(len(sys.argv) < 3 or len(sys.argv) > 4):
    print("Usage: python glue.py input folder output file name [output file type]")
elif(len(sys.argv) == 4):
    outtype = sys.argv[3]
else:
    outtype = "none"

Glue(sys.argv[1], sys.argv[2], outtype)
