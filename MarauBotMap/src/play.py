#!env python3
import maraubotmap.loupe as loupe, maraubotmap as mbm

mbm.hello()


def main():
    ihm= loupe.Loupe()
    ihm.process()

if __name__ == "__main__":
    main()