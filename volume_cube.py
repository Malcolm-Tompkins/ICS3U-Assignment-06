#!/usr/bin/env python3

# Created by Malcolm Tompkins
# Created on May 28, 2021
# Calculates the volume of a cube


def volume_cube(length, width, height):
    volume = length * width * height
    return volume


def main():
    user_input1 = (input("Enter the length of the cube (mm): "))
    user_input2 = (input("Enter the width of the cube (mm): "))
    user_input3 = (input("Enter the height of the cube (mm): "))

    try:
        user_length = int(user_input1)
        try:
            user_width = int(user_input2)
            try:
                user_height = int(user_input3)
                volume_cube(user_length, user_width, user_height)
                final_volume = volume_cube(user_length, user_width,
                                           user_height)
                print("The volume of the cube is: {} mm³".format(final_volume))
            except Exception:
                print("{} is not a dimension".format(user_input3))
            finally:
                print("Done.")
        except Exception:
            print("{} is not a dimension".format(user_input2))
    except Exception:
        print("{} is not a dimension".format(user_input1))


if __name__ == "__main__":
    main()
