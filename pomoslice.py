
# pomoslice v0.1
# Tool that time boxes hours into batches of work and rest.

# @matnesis
# 2018/09/09 07:27 pm


import argparse


if __name__ == '__main__':

    POMOSLICE = """
    pomoslice v0.1
    """
    print(POMOSLICE)

    # Command line
    PARSER = argparse.ArgumentParser(
        description="tool that time boxes hours into batches of work and rest")
    PARSER.add_argument(
        "-hs",
        "--hours",
        help="hours that you wanna work",
        type=float,
        required=True)
    PARSER.add_argument(
        "-bs",
        "--batches",
        help="batches of work & rest that you wanna do",
        type=int,
        required=True)
    PARSER.add_argument(
        "-r",
        "--rest-ratio",
        help="percentage of the batch used for resting (default 25)",
        type=int,
        default=25)
    ARGS = PARSER.parse_args()

    # Arguments to data

    hours = 0 if ARGS.hours < 0 else ARGS.hours
    minutes = hours * 60
    batches = 1 if ARGS.batches < 1 else ARGS.batches
    rest_ratio = 100 if ARGS.rest_ratio > 100 else ARGS.rest_ratio
    rest_ratio = 0 if ARGS.rest_ratio < 0 else ARGS.rest_ratio

    # Pomo slicing

    minutes_per_block = round(minutes / batches)
    work_time = round(minutes_per_block * (100 - rest_ratio) / 100)
    rest_time = round(minutes_per_block * rest_ratio / 100)
    effective_minutes = work_time * batches
    effective_hours = round(effective_minutes / 60 * 10) / 10

    # Results

    print(f"In {hours} hour{'s' if hours > 1 else ''},\n"
          f"you should work {batches} batch{'es' if batches > 1 else ''} of {work_time} minutes,\n"
          f"resting {rest_time} minutes in between,\n"
          f"for a total of {effective_hours} effective hours!")

    print('\n<3')
