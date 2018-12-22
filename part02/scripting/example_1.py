import platform
version = platform.python_version()

snake_string = """
Welcome to Python{}!

             ____
            / . .\\
            \  ---<
             \  /
   __________/ /
-=:___________/

<3, Q10Viking
""".format(version)

how_many_snakes = 1
print(snake_string * how_many_snakes)