import subprocess
import sys, time

args = sys.argv
index = 1

if not "-interaction=nonstopmode" in args:
    args[0] = "-interaction=nonstopmode"
    index = 0

for arg in args:
    if arg.startswith("-"):
        continue
    inputpath = arg
    break

if not inputpath.endswith('.tex'):
    inputpath = inputpath + '.tex'

pdfpath = inputpath.replace(".tex", ".pdf")

outputpath = inputpath.replace(".tex", "_clean.pdf")

print("Recongized tex file:" + inputpath)
print("Recongized latex pdf file:" + pdfpath)
print("Recongized cleaned pdf file:" + outputpath)

procs = [
    subprocess.Popen(['pdflatex'] + args[index:], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE),
    None
]

for proc in procs:
    while True:
        returncode = proc.poll()
        if returncode is not None: # Process finished.
            # Here, `proc` has finished with return code `retcode`
            if returncode != 0:
                for line in iter(lambda: proc.stderr.readline(), 'b'):
                    sys.stderr.write(line.decode("UTF-8"))
                    if (line == b''):
                        break 
                exit(returncode)
            break
        else: # No process is done, wait a bit and check again.
            time.sleep(.1)

            for line in iter(lambda: proc.stdout.readline(), 'b'):
                sys.stdout.write(line.decode("UTF-8"))
                if (line == b''):
                    break 

    if procs[1] == None:
        print("Finished creating latexpdf. Cleaning.")
        procs[1] = subprocess.Popen(['gs', '-dNOPAUSE',  '-sDEVICE=pdfwrite', f'-sOUTPUTFILE={outputpath}', pdfpath], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        procs[1].communicate(input='quit'.encode())[0]
    else:
        print(f"Cleaned PDF. It was saved under {outputpath}")