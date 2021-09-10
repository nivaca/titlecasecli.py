import sys
from titlecase import titlecase


# -------------------------------------------------------------------
def main():
    """ Main function. """
    argv = sys.argv[1:]

    if not argv:
        sys.exit(1)
    else:
        if argv[0] == '':
            sys.exit(1)

    inputtext = ' '.join(argv)
    outputtext = titlecase(inputtext)
    print(outputtext, file=sys.stdout)


# -----------------------------------------------------------------
if __name__ == '__main__':
    main()
