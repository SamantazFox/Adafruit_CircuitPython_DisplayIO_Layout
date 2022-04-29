# import time
# import displayio
# import board
# import terminalio
# from adafruit_displayio_layout.layouts.page_layout import PageLayout
# from adafruit_display_text.bitmap_label import Label
# import vectorio
#
# display = board.DISPLAY
#
# # Make the display context
# main_group = displayio.Group()
# display.show(main_group)
#
# test_page_layout = PageLayout(x=0, y=0)
#
# page_1_lbl = Label(font=terminalio.FONT, text="Page One!", anchor_point=(0, 0), anchored_position=(10, 10), scale=3)
# page_2_lbl = Label(font=terminalio.FONT, text="Page Two!", anchor_point=(0, 0), anchored_position=(10, 10), scale=3)
# other_lbl = Label(font=terminalio.FONT, text="Something Different!", anchor_point=(0, 0), anchored_position=(10, 50), scale=3)
#
# test_page_layout.add_content(page_1_lbl, "page_1")
# test_page_layout.add_content(page_2_lbl, "page_2")
# test_page_layout.add_content(other_lbl, "page_3")
#
# #main_group.append(other_lbl)
#
# main_group.append(test_page_layout)
#
# print("showing page 1")
#
# test_page_layout.show_page(page_name="page_2")
#
#
# test_page_layout.showing_page_index = 0
#
# #print(test_page_layout.showing_page_index)
# #print(test_page_layout.showing_page_name)
#
# colors = displayio.Palette(3)
# colors[0] = 0xdddd00
# colors[1] = 0x00dddd
# colors[2] = 0x00dd00
# rect = vectorio.Rectangle(pixel_shader=colors, width=100,height=20, x=10, y=100)
#
# test_page_layout.get_page(page_index=2)["content"][0].color = 0xFF00FF
# test_page_layout.get_page(page_name="page_2")["content"].append(rect)
#
# while True:
#     time.sleep(1)
#     test_page_layout.previous_page()
#
#
#     # test_page_layout.show_page(page_name="page_1")
#     # time.sleep(1)
#     # test_page_layout.show_page(page_name="page_2")
#     # time.sleep(1)
#     pass


# SPDX-FileCopyrightText: 2022 Tim C
#
# SPDX-License-Identifier: MIT
"""
Make a PageLayout and illustrate all of it's features
"""
import time
import displayio
import board
import terminalio
from adafruit_display_text.bitmap_label import Label
from adafruit_display_shapes.rect import Rect
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.triangle import Triangle
from adafruit_displayio_layout.layouts.tab_layout import TabLayout
from adafruit_bitmap_font import bitmap_font

# built-in display
display = board.DISPLAY
# display.rotation = 90
display.rotation = 0

# create and show main_group
main_group = displayio.Group()
display.show(main_group)

font = bitmap_font.load_font("fonts/Helvetica-Bold-16.bdf")

# create the page layout
test_page_layout = TabLayout(x=0, y=0,
                             display=board.DISPLAY,
                             tab_height=28, tab_text_scale=1,
                             custom_font=font,
                             inactive_tab_spritesheet="bmps/test_bmp_6.bmp",
                             active_tab_spritesheet="bmps/test_bmp_7.bmp",
                             showing_tab_text_color=0x00aa59,
                             tab_text_color=0xeeeeee,
                             inactive_tab_transparent_indexes=(0, 1),
                             active_tab_transparent_indexes=(0, 1),
                             tab_count=4)

# make 3 pages of content
page_1_group = displayio.Group()
page_2_group = displayio.Group()
page_3_group = displayio.Group()
page_4_group = displayio.Group()

# labels
page_1_lbl = Label(
    font=terminalio.FONT,
    scale=2,
    text="This is the first page!",
    anchor_point=(0, 0),
    anchored_position=(10, 10),
)
page_2_lbl = Label(
    font=terminalio.FONT,
    scale=2,
    text="This page is the second page!",
    anchor_point=(0, 0),
    anchored_position=(10, 10),
)
page_3_lbl = Label(
    font=terminalio.FONT,
    scale=2,
    text="The third page is fun!",
    anchor_point=(0, 0),
    anchored_position=(10, 10),
)

page_4_lbl = Label(
    font=terminalio.FONT,
    scale=2,
    text="The fourth page is where it's at",
    anchor_point=(0, 0),
    anchored_position=(10, 10),
)

# shapes
square = Rect(x=20, y=70, width=40, height=40, fill=0x00DD00)
circle = Circle(50, 100, r=30, fill=0xDD00DD)
triangle = Triangle(50, 0, 100, 50, 0, 50, fill=0xDDDD00)
rectangle = Rect(x=80, y=60, width=100, height=50, fill=0x0000DD)

triangle.x = 80
triangle.y = 70

# add everything to their page groups
page_1_group.append(square)
page_1_group.append(page_1_lbl)
page_2_group.append(page_2_lbl)
page_2_group.append(circle)
page_3_group.append(page_3_lbl)
page_3_group.append(triangle)
page_4_group.append(page_4_lbl)
page_4_group.append(rectangle)

# add the pages to the layout, supply your own page names
test_page_layout.add_content(page_1_group, "One")
test_page_layout.add_content(page_2_group, "Two")
test_page_layout.add_content(page_3_group, "Thr")
test_page_layout.add_content(page_4_group, "For")
# test_page_layout.add_content(displayio.Group(), "page_5")

# add it to the group that is showing on the display
main_group.append(test_page_layout)

#test_page_layout.tab_tilegrids_group[3].x += 50

# change page with function by name
# test_page_layout.show_page(page_name="page_3")
# print("showing page index:{}".format(test_page_layout.showing_page_index))
# time.sleep(1)

# change page with function by index
test_page_layout.show_page(page_index=0)
print("showing page name: {}".format(test_page_layout.showing_page_name))
time.sleep(1)

# change page by updating the page name property
# test_page_layout.showing_page_name = "page_3"
# print("showing page index: {}".format(test_page_layout.showing_page_index))
# time.sleep(1)

# change page by updating the page index property
test_page_layout.showing_page_index = 1
print("showing page name: {}".format(test_page_layout.showing_page_name))
time.sleep(5)

another_text = Label(terminalio.FONT, text="And another thing!", scale=2, color=0x00ff00, anchor_point=(0, 0),
                     anchored_position=(100, 100))
test_page_layout.showing_page_content.append(another_text)

print("starting loop")


while True:
    time.sleep(1)
    # change page by next page function. It will loop by default
    test_page_layout.next_page()
