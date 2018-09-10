

import argparse
import os
import sys

app_name = "pomoslice v0.1"
app_file = os.path.basename(sys.argv[0])
app_description = "tool that time boxes hours into batches of work and rest"

# 2018/09/09 07:27 pm
# @matnesis


if __name__ == '__main__':

    pomoslice = f"""
    {app_name}
    """
    print(pomoslice)

    # Command line
    parser = argparse.ArgumentParser(description=app_description)
    parser.add_argument(
        "-hs",
        "--hours",
        help="hours that you wanna work",
        type=float,
        required=True)
    parser.add_argument(
        "-bs",
        "--batches",
        help="batches of work & rest that you wanna do",
        type=int,
        required=True)
    parser.add_argument(
        "-r",
        "--rest-ratio",
        help="percentage of the batch used for resting (default 25)",
        type=int,
        default=25)

    try:
        args = parser.parse_args()
    except SystemExit:
        print(f'example: {app_file} -hs 8 -bs 7')
        print(f'help: {app_file} -h')
        print(f"\n{app_description}")
        parser.exit()

    # Arguments to data

    hours = 0 if args.hours < 0 else args.hours
    minutes = hours * 60
    batches = 1 if args.batches < 1 else args.batches
    rest_ratio = args.rest_ratio
    rest_ratio = 100 if rest_ratio > 100 else rest_ratio
    rest_ratio = 0 if rest_ratio < 0 else rest_ratio

    # Pomo slicing

    minutes_per_block = round(minutes / batches)
    work_time = round(minutes_per_block * (100 - rest_ratio) / 100)
    rest_time = round(minutes_per_block * rest_ratio / 100)
    effective_minutes = work_time * batches
    effective_hours = round(effective_minutes / 60 * 10) / 10

    # Results

    print(f"In {hours} hour{'s' if hours > 1 else ''},\n"
          f"you could work {batches} batch{'es' if batches > 1 else ''} of {work_time} minutes,\n"
          f"resting {rest_time} minutes in between,\n"
          f"for a total of {effective_hours} effective hours!")

    print('\n<3')
