import os
import sys

children = []

def sample_job(pid):
    print(f"Sample job is ran! Child PID: {pid}")


def main():
    global children
    jobs = [sample_job, sample_job, sample_job, sample_job] * 8000

    for job in jobs:
        _child = os.fork()
        if _child:
            children.append(_child)
        else:
            pid = os.getpid()

            print(f"Job is starting with PID: {pid}")
            job(pid)


            # DO NOT FORGET TO EXIT ! ! !
            sys.exit()

if __name__ == '__main__':
    main_pid = os.getpid()

    print(f"Starting Main process: {main_pid} ")

    main()

    # Wait for all the jobs are complete!
    for child in children:
        os.waitpid(child, 0)

    print(f"End of Main process: {main_pid}")
