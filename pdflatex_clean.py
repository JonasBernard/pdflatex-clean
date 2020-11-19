import subprocess
import sys, time
import os, re

def enforce_flag_value(args, flag, value):
    pattern = re.compile(f'.*-{flag}=.*')
    i = find((match := pattern.match(arg)) for arg in args)
    if i >= 0:
        if not f"-{flag}={value}" == match.group(0):
            args[i] = f"-{flag}={value}"
    else:
        args.insert(0, f"-{flag}={value}")
    return args

def find(iterable):
    for index, elem in enumerate(iterable):
        if elem:
            return index
    return -1

def main():
    # get mutable args
    args = sys.argv[1:]

    #enforce nostop interaction mode 
    args = enforce_flag_value(args, 'interaction', 'nonstopmode')

    #enfore pdf format
    args = enforce_flag_value(args, 'output-format', 'pdf')


    #get the .tex file from args
    inputpath = None
    for arg in args:
        if arg.startswith("-"):
            continue
        inputpath = arg
        break

    # if no .tex file is found, abord
    if inputpath == None:
        print("pdflatex-clean should only be used for PDF conversion. Use regular pdflatex for everything else.")
        exit(-1)

    # .tex file can be input without the .tex file extension. To have consistent variable names, add it if missing.
    if not inputpath.endswith('.tex'):
        inputpath = inputpath + '.tex'

    # path that pdflatex will save the pdf to.
    outputpath = inputpath.replace(".tex", ".pdf")
    # generate path to temporarily save the cleaned file. (Ghostscript cannot output to its input file)
    temppath = inputpath.replace(".tex", ".cleaning.pdf")

    # give some info to the user
    print("Recongized tex file:" + inputpath)
    print("Recongized latex pdf file:" + outputpath)

    procs = [
        subprocess.Popen(['pdflatex'] + args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE),
        None
    ]

    for proc in procs:
        while True:
            returncode = proc.poll()
            if returncode is not None: # Process finished.
                # Here, `proc` has finished with return code `retcode`
                if returncode != 0:
                    try:
                        for line in iter(lambda: proc.stderr.readline(), 'b'):
                            sys.stderr.write(line.decode("UTF-8"))
                            if (line == b''):
                                break
                    except ValueError:
                        print("Some error occured while executing a process")
                    exit(returncode)
                break
            else: # The process is not done, wait a bit and check again.
                time.sleep(.1)

                for line in iter(lambda: proc.stdout.readline(), 'b'):
                    sys.stdout.write(line.decode("UTF-8"))
                    if (line == b''):
                        break

        if procs[1] == None:
            print("Finished creating latexpdf. Cleaning.")
            procs[1] = subprocess.Popen(['gs', '-dNOPAUSE',  '-sDEVICE=pdfwrite', f'-sOUTPUTFILE={temppath}', outputpath], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            procs[1].communicate(input='quit'.encode())[0]
        else:
            print(f"Cleaned PDF. It was temporarily saved under {temppath}.")

    try:
        os.remove(outputpath)
        os.rename(temppath, outputpath)
        os.remove(temppath)

        print(f"Finished. Saved {outputpath}.")
    except Exception as e:
        print(e, file=sys.stderr)

main()