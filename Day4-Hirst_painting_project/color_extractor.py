import colorgram

extracted_colors = colorgram.extract("colors.jpg", 50)
rgb_colors = [tuple(color.rgb) for color in extracted_colors]
print(rgb_colors)