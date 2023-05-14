import pygal_maps_world.maps

wm = pygal_maps_world.maps.World()
wm.title = "North, Central, and South America"

wm.add("North America",{'ca':34126000,'mx':309349000,'us':113426000})
wm.add("Central America",['bz','cr','gt','hn','ni','pa','sv'])
wm.add("Sout America",['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf','gy', 'pe', 'py', 'sr', 'uy', 've'])


wm.render_to_file(r"2_Python_Crash_Course\15_17_data_visualization\img\Americas.svg")










